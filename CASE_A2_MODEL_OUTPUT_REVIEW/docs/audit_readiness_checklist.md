# ⚙️ Audit Readiness Checklist
## Modelling Outputs — Verification-Oriented Review

---

## Purpose

This checklist is used to assess whether modelling outputs are **fit for external use** in verification-driven contexts (e.g. carbon accounting, reporting, audit).

It is designed to support:
- internal quality control
- technical review
- audit-facing documentation
- go / no-go decisions

This checklist does **not** certify compliance with any specific standard.
It evaluates **readiness and defensibility**.

---

## How to Use

- Complete this checklist **after model execution**
- Use it **before** sharing results externally
- Treat any unchecked critical item as a **blocking issue**

For each section:
- ☐ = not satisfied  
- ☑ = satisfied  
- ⚠ = partially satisfied / requires caveat  

---

## 1. Data Integrity & Provenance

☐ / ☑ / ⚠ All input data sources are clearly identified  
☐ / ☑ / ⚠ Synthetic or derived data are explicitly labelled  
☐ / ☑ / ⚠ No proprietary or site-specific data are used without authorisation  
☐ / ☑ / ⚠ Data transformations are documented  
☐ / ☑ / ⚠ Versioning of input datasets is traceable  

**Blocking if:** data origin or transformation is unclear.

---

## 2. Model Applicability

☐ / ☑ / ⚠ Model choice is appropriate for the agro-ecological context  
☐ / ☑ / ⚠ Model limitations are explicitly acknowledged  
☐ / ☑ / ⚠ Known non-applicable contexts are identified  
☐ / ☑ / ⚠ No implicit extrapolation beyond model validity  

**Blocking if:** model is applied outside its defensible scope.

---

## 3. Assumptions Transparency

☐ / ☑ / ⚠ All key assumptions are explicitly documented  
☐ / ☑ / ⚠ Assumptions are consistent across scenarios  
☐ / ☑ / ⚠ Assumptions are scientifically defensible  
☐ / ☑ / ⚠ No assumptions are hidden in code or defaults  

**Blocking if:** assumptions cannot be reconstructed by a reviewer.

---

## 4. Numerical Sanity & Internal Consistency

☐ / ☑ / ⚠ No physically or agronomically implausible values  
☐ / ☑ / ⚠ Temporal dynamics are coherent and continuous  
☐ / ☑ / ⚠ Aggregate indicators align with component behaviour  
☐ / ☑ / ⚠ No unexplained discontinuities  

**Blocking if:** numerical stability is confused with scientific validity.

---

## 5. Plausibility & Domain Coherence

☐ / ☑ / ⚠ Outputs align with known agronomic principles  
☐ / ☑ / ⚠ Management effects are plausible in magnitude and timing  
☐ / ☑ / ⚠ No counterintuitive trends remain unexplained  

**Blocking if:** results cannot be justified through domain reasoning.

---

## 6. Sensitivity & Uncertainty

☐ / ☑ / ⚠ Key uncertainty sources are identified  
☐ / ☑ / ⚠ Sensitivity analysis targets relevant parameters  
☐ / ☑ / ⚠ Dominant sensitivities are scientifically reasonable  
☐ / ☑ / ⚠ Uncertainty is propagated to decision-relevant indicators  

**Blocking if:** uncertainty is ignored or minimised.

---

## 7. Fitness-for-Use Decision

☐ / ☑ / ⚠ Intended use case is explicitly stated  
☐ / ☑ / ⚠ Outputs are appropriate for this use case  
☐ / ☑ / ⚠ Limitations are aligned with use constraints  
☐ / ☑ / ⚠ Downscaling or exclusion applied where needed  

**Blocking if:** outputs are used beyond their justified scope.

---

## 8. Documentation Quality

☐ / ☑ / ⚠ Assumptions are documented  
☐ / ☑ / ⚠ Limitations are documented  
☐ / ☑ / ⚠ Uncertainty interpretation is documented  
☐ / ☑ / ⚠ Documentation is readable by an external reviewer  

**Blocking if:** a reviewer cannot reconstruct the reasoning.

---

## 9. Audit & Review Preparedness

☐ / ☑ / ⚠ Rationale for key decisions is documented  
☐ / ☑ / ⚠ Known weaknesses are explicitly disclosed  
☐ / ☑ / ⚠ No overclaiming or implicit guarantees  
☐ / ☑ / ⚠ Clear escalation path if results are challenged  

**Blocking if:** results rely on trust rather than explanation.

---

## 10. Final Status

### Overall Assessment

☐ Audit-ready  
☐ Reporting with explicit caveats  
☐ Internal use only  
☐ Not fit for use  

### Key Blocking Issues (if any)

- …
- …
- …

### Reviewer Notes

- …

---

## Core Principle

> In verification-driven contexts,  
> **the ability to explain why results should NOT be used**  
> is as important as producing the results themselves.

---

## Versioning

- Checklist version: 1.0  
- Applicable to: process-based models, synthetic or real data  
- Intended reuse: across multiple applied cases
