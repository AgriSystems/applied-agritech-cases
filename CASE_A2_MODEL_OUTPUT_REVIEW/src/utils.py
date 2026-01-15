from __future__ import annotations

import pandas as pd
import numpy as np


def assert_required_columns(df: pd.DataFrame, required: list[str], name: str) -> None:
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"{name}: missing required columns: {missing}")


def sanity_check_soc_timeseries(df: pd.DataFrame) -> dict:
    """
    Basic checks:
    - required columns
    - non-negative SOC
    - continuity (no extreme jumps)
    """
    assert_required_columns(
        df,
        ["year", "scenario", "total_soc_tCha", "delta_soc_tCha_per_yr"],
        "soc_timeseries",
    )

    out = {}
    out["min_soc"] = float(df["total_soc_tCha"].min())
    out["max_soc"] = float(df["total_soc_tCha"].max())
    out["has_negative_soc"] = bool((df["total_soc_tCha"] < 0).any())

    # Extreme year-to-year jumps heuristic (synthetic guardrail)
    # SOC change > 2.0 tC/ha/yr is suspicious in many arable contexts (not universal).
    out["extreme_delta_count"] = int((df["delta_soc_tCha_per_yr"].abs() > 2.0).sum())

    return out


def pool_consistency_check(pools_df: pd.DataFrame, soc_df: pd.DataFrame) -> pd.DataFrame:
    """
    For each scenario/year compare pools sum to total SOC.
    Returns a table with absolute and relative differences.
    """
    assert_required_columns(pools_df, ["year", "scenario", "soc_tCha"], "soc_pools")
    assert_required_columns(soc_df, ["year", "scenario", "total_soc_tCha"], "soc_timeseries")

    pools_sum = pools_df.groupby(["scenario", "year"])["soc_tCha"].sum().reset_index()
    merged = pools_sum.merge(soc_df[["scenario", "year", "total_soc_tCha"]], on=["scenario", "year"], how="left")
    merged["abs_diff"] = (merged["soc_tCha"] - merged["total_soc_tCha"]).abs()
    merged["rel_diff"] = merged["abs_diff"] / merged["total_soc_tCha"].replace(0, np.nan)
    return merged.sort_values(["scenario", "year"])
