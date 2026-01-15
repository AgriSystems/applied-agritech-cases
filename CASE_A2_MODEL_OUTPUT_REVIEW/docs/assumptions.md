# Assumptions — CASE_A2 RothC Output Review

## Purpose of this Document

This document records the **explicit assumptions** used to construct and review synthetic RothC model outputs in CASE_02.

Its purpose is to:
- make modelling and review assumptions transparent
- support reproducibility
- clarify the boundaries within which results can be interpreted

This document is intended for **internal technical review and audit-facing contexts**.

---

## Scenario Envelope

The case assumes a **generic, non-site-specific European agricultural context**, defined as follows:

- Climate: temperate European climate
- System: rainfed arable cropping system
- Soil texture: loam to clay loam
- Depth of interest: topsoil (0–30 cm)
- Time horizon: multi-year baseline and project scenario
- Management change (project scenario):
  - reduced tillage
  - increased residue retention

These assumptions are intentionally broad and representative, not optimized for any specific location.

---

## Model Context

- Model type: process-based soil carbon model
- Reference model: RothC
- Use: post-processing and output review
- Calibration: assumed completed prior to this case
- Scope of this case:
  - output inspection
  - plausibility checks
  - uncertainty framing
  - decision fitness

No model calibration or parameter optimisation is performed within this case.

---

## Synthetic Data Generation Approach

All datasets used in this case are **synthetic**, generated to reflect **plausible ranges observed in public datasets**, without reproducing any real site or project.

Public sources used to inform ranges and distributions include:
- Copernicus / ERA5 (climate statistics)
- ISRIC SoilGrids (SOC stocks and texture fractions)
- FAOSTAT / Eurostat (land use context)

Synthetic data are generated using:
- bounded random sampling
- simple stochastic processes
- fixed random seeds for reproducibility

The objective is **internal coherence**, not empirical accuracy.

---

## Key Modelling Assumptions

- Initial SOC stocks fall within typical EU agricultural ranges
- SOC changes are gradual and continuous over time
- Pool distributions are internally consistent with total SOC
- Management effects are expressed as small but persistent changes
- No abrupt regime shifts are simulated

These assumptions are chosen to avoid unrealistic behaviour while preserving uncertainty.

---

## Assumption Boundaries

The following are explicitly **out of scope**:

- Representation of specific farms or parcels
- Use of measured SOC time series
- Spatial heterogeneity across landscapes
- Climate extremes or disturbance events
- Carbon credit issuance logic

Any interpretation beyond these boundaries is invalid.

---

## Reproducibility

All synthetic data generation steps are scripted and reproducible.
Re-running the data generation script with the same seed produces identical outputs.

---

## Summary

This case uses simplified, transparent assumptions to enable **robust reasoning about model outputs under uncertainty**, without claiming empirical validity.

Assumptions are documented to support auditability, not to imply precision.
