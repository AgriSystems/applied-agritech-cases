#!/usr/bin/env python3
"""
Generate synthetic datasets for CASE_02 (RothC output review under uncertainty).

Outputs (written to data/synthetic/):
- soc_timeseries.csv
- soc_pools.csv
- sensitivity_results.csv

Policy:
- Synthetic only (no site/project data)
- Derived from plausible EU ranges (documented in docs/assumptions.md)
- Reproducible via fixed random seed
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class ScenarioConfig:
    seed: int = 42
    start_year: int = 2000
    end_year: int = 2025  # exclusive
    climate_regime: str = "temperate_eu"
    soil_texture_class: str = "loam_to_clay_loam"
    system: str = "rainfed_arable"
    # SOC stock in topsoil (0–30cm) plausible envelope (t C / ha)
    initial_soc_range: Tuple[float, float] = (40.0, 75.0)
    # Baseline annual SOC change (t C/ha/yr): near zero, small drift
    baseline_mu: float = 0.02
    baseline_sigma: float = 0.12
    # Project effect on annual change (t C/ha/yr): modest positive shift
    project_delta_mu: float = 0.18
    project_delta_sigma: float = 0.06
    # Measurement / reporting noise (t C/ha): small observation-like noise
    obs_noise_sigma: float = 0.20


def _ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def _piecewise_management_effect(years: np.ndarray, change_year: int) -> np.ndarray:
    """
    Smoothly ramps management effect after change_year.
    """
    t = years - change_year
    effect = np.zeros_like(years, dtype=float)
    # ramp over 3 years
    ramp = np.clip(t / 3.0, 0.0, 1.0)
    effect = ramp
    return effect


def generate_soc_timeseries(cfg: ScenarioConfig) -> pd.DataFrame:
    rng = np.random.default_rng(cfg.seed)

    years = np.arange(cfg.start_year, cfg.end_year)
    n = len(years)

    # Initial SOC stock
    soc0 = rng.uniform(*cfg.initial_soc_range)

    # Baseline increments
    baseline_incr = rng.normal(loc=cfg.baseline_mu, scale=cfg.baseline_sigma, size=n)

    # Project scenario: apply a management change around mid-horizon
    change_year = int(np.median(years))
    ramp = _piecewise_management_effect(years, change_year=change_year)

    project_delta = rng.normal(loc=cfg.project_delta_mu, scale=cfg.project_delta_sigma, size=n)
    project_incr = baseline_incr + ramp * project_delta

    # Integrate to SOC levels
    baseline_soc = soc0 + np.cumsum(baseline_incr)
    project_soc = soc0 + np.cumsum(project_incr)

    # Add small observation-like noise to mimic operational variability (still synthetic)
    baseline_soc_obs = baseline_soc + rng.normal(0.0, cfg.obs_noise_sigma, size=n)
    project_soc_obs = project_soc + rng.normal(0.0, cfg.obs_noise_sigma, size=n)

    # Prevent negative SOC (hard safety)
    baseline_soc_obs = np.clip(baseline_soc_obs, 1.0, None)
    project_soc_obs = np.clip(project_soc_obs, 1.0, None)

    df = pd.DataFrame(
        {
            "year": years,
            "scenario": "baseline",
            "total_soc_tCha": baseline_soc_obs,
            "management_change_year": change_year,
        }
    )
    df2 = pd.DataFrame(
        {
            "year": years,
            "scenario": "project",
            "total_soc_tCha": project_soc_obs,
            "management_change_year": change_year,
        }
    )
    out = pd.concat([df, df2], ignore_index=True)

    # Derived metrics (ΔSOC year-on-year)
    out["delta_soc_tCha_per_yr"] = out.groupby("scenario")["total_soc_tCha"].diff()

    return out


def generate_soc_pools(cfg: ScenarioConfig, soc_timeseries: pd.DataFrame) -> pd.DataFrame:
    """
    Create internally consistent RothC-like pool allocations for each scenario/year.

    Pools:
    - DPM, RPM, BIO, HUM, IOM

    Strategy:
    - Define plausible fractions with small randomness
    - Ensure fractions sum to 1 per row
    - Compute pool SOC as fraction * total SOC
    """
    rng = np.random.default_rng(cfg.seed + 1)

    pools = ["DPM", "RPM", "BIO", "HUM", "IOM"]

    # Base fractions (roughly RothC typical ordering; still synthetic)
    base = np.array([0.03, 0.20, 0.04, 0.55, 0.18], dtype=float)

    rows = []
    for _, r in soc_timeseries.iterrows():
        total = float(r["total_soc_tCha"])

        # jitter fractions slightly
        jitter = rng.normal(0.0, 0.01, size=len(pools))
        fracs = np.clip(base + jitter, 0.001, None)

        # scenario: project has slightly higher HUM share after change year (plausible direction)
        if r["scenario"] == "project" and int(r["year"]) >= int(r["management_change_year"]):
            fracs[pools.index("HUM")] += 0.01
            fracs[pools.index("RPM")] -= 0.005
            fracs[pools.index("DPM")] -= 0.005
            fracs = np.clip(fracs, 0.001, None)

        fracs = fracs / fracs.sum()

        for p, f in zip(pools, fracs):
            rows.append(
                {
                    "year": int(r["year"]),
                    "scenario": r["scenario"],
                    "pool": p,
                    "fraction": float(f),
                    "soc_tCha": float(total * f),
                }
            )

    pools_df = pd.DataFrame(rows)

    # Add consistency check columns (helpful downstream)
    totals = pools_df.groupby(["scenario", "year"])["soc_tCha"].sum().rename("pools_sum_tCha")
    pools_df = pools_df.merge(totals.reset_index(), on=["scenario", "year"], how="left")
    return pools_df


def generate_sensitivity_results(cfg: ScenarioConfig) -> pd.DataFrame:
    """
    Create a synthetic sensitivity ranking consistent with typical RothC drivers.

    impact: normalized to sum to 1 (relative influence).
    """
    # Plausible drivers in this context
    params = [
        "carbon_input_rate",
        "clay_content",
        "temperature_response",
        "moisture_modifier",
        "decomposition_rate_modifier",
    ]

    # Deterministic but could be randomized; keep stable for clarity
    impacts = np.array([0.34, 0.28, 0.16, 0.12, 0.10], dtype=float)
    impacts = impacts / impacts.sum()

    df = pd.DataFrame({"parameter": params, "impact": impacts})
    df["rank"] = df["impact"].rank(ascending=False, method="dense").astype(int)
    df = df.sort_values("rank")
    return df


def main() -> None:
    cfg = ScenarioConfig()

    root = Path(__file__).resolve().parents[1]
    out_dir = root / "data" / "synthetic"
    _ensure_dir(out_dir)

    soc_ts = generate_soc_timeseries(cfg)
    soc_pools = generate_soc_pools(cfg, soc_ts)
    sens = generate_sensitivity_results(cfg)

    soc_ts.to_csv(out_dir / "soc_timeseries.csv", index=False)
    soc_pools.to_csv(out_dir / "soc_pools.csv", index=False)
    sens.to_csv(out_dir / "sensitivity_results.csv", index=False)

    print(f"[OK] Wrote: {out_dir/'soc_timeseries.csv'}")
    print(f"[OK] Wrote: {out_dir/'soc_pools.csv'}")
    print(f"[OK] Wrote: {out_dir/'sensitivity_results.csv'}")


if __name__ == "__main__":
    main()
