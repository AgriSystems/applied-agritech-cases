# CASE_A2 — RothC Output Review under Uncertainty

This repository documents an applied case focused on the **review of RothC soil carbon model outputs under uncertainty**, in the context of carbon farming and verification-driven environments.

The case is designed to simulate a **realistic internal workflow** where model outputs are evaluated for **fitness-for-use**, rather than for numerical optimisation or academic performance.

The emphasis is on:
- agronomic plausibility
- uncertainty interpretation
- audit and verification readiness
- decision-making under data constraints

To know more about the case studies that we decided to analyze, go to [this link](https://www.notion.so/AgriSystems-Working-Notes-2e9168327fcb807ba693cad820d0785e?source=copy_link)

---

## Scope

This case covers:
- inspection of synthetic RothC output time series
- review of SOC trajectories and pool dynamics
- sensitivity analysis interpretation
- uncertainty framing
- go / no-go decisions for reporting and verification

This case does **not** include:
- model calibration or parameter optimisation
- site-specific or project-specific data
- carbon credit issuance calculations
- performance benchmarking of RothC itself

---

## Synthetic Data Policy

All datasets used in this case are **synthetic or derived representations** constructed to reflect **plausible ranges observed in public datasets**, including but not limited to:

- Copernicus / ERA5 (climate variables)
- ISRIC SoilGrids (soil properties)
- FAOSTAT / Eurostat (land use context)

No real project data, farm-level observations, or proprietary datasets are used.

Synthetic data are generated to:
- stress-test decision logic under uncertainty
- preserve internal consistency (SOC totals vs pools)
- remain fully reproducible

---

## 🌱 Repository Structure

``` case_a2_rothc_output_review/
├── 📘 README.md                 # Project overview & navigation
├── 📦 requirements.txt          # Python dependencies
├── 🚫 .gitignore                # Git hygiene

├── 📊 data/
│   ├── raw/                     # Empty – no real data committed 🔒
│   └── synthetic/               # Synthetic CSV data for reproducibility 🧪

├── 📓 notebooks/
│   └── case_A2_rothc_output_review.ipynb
│       # Main analysis notebook: RothC outputs, diagnostics & uncertainty

├── 🧾 docs/
│   ├── assumptions.md           # Modelling assumptions & boundary conditions
│   ├── uncertainty_notes.md     # Sources of uncertainty & interpretation
│   └── limitations.md           # Known limits of the analysis ⚠️

├── 🛠️ src/
│   ├── generate_synthetic_data.py  # Synthetic data generator (public-friendly)
│   └── utils.py                    # Shared utilities & helper functions

```


---

## Notebook Description

The notebook `case_02_rothc_output_review.ipynb` performs the following steps:

1. Loads synthetic RothC output datasets
2. Executes basic sanity and consistency checks
3. Reviews SOC temporal dynamics for agronomic plausibility
4. Inspects pool-level behaviour
5. Reviews sensitivity analysis results
6. Frames uncertainty as a decision variable
7. Concludes with a **fitness-for-use decision matrix**

The notebook is intentionally **decision-oriented**, not instructional.

---

## How to Run

### 1. Environment setup

Create a virtual environment and install dependencies:

``` 
pip install -r requirements.txt 
```

### 2. Generate synthetic data
``` 
python src/generate_synthetic_data.py
```
This will populate the ` data/synthetic/`  directory.

### 3. Run the notebook

Open and execute:

``` 
jupyter notebook notebooks/case_02_rothc_output_review.ipynb
```
Run all cells from top to bottom to ensure reproducibility.

## 🗣️ Intended Audience
This case is intended for:

- environmental and soil carbon modellers
- MMRV and verification teams
- technical reviewers and auditors
- interdisciplinary teams working at the interface of agronomy, data science, and carbon markets


It assumes familiarity with:
- soil carbon concepts
- process-based modelling
- uncertainty analysis
- verification-oriented workflows

## ⚠️ Disclaimer

**This repository is provided for illustrative and analytical purposes only. This case as the others among this organization's repositories are part of the project *AgriSystems*. To discover more about our project, please [click on this link](https://www.notion.so/AgriSystems-Working-Notes-2e9168327fcb807ba693cad820d0785e?source=copy_link)**

Results produced here:

- are not site-specific

- are not suitable for carbon credit issuance

- should not be used for operational or financial decisions

The case demonstrates how to reason about model outputs, not how to deploy models in production.

## License

This repository is shared for educational and analytical use.
No warranty is provided regarding correctness, completeness, or fitness for any specific purpose.