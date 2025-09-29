
## `Project Documentation`

### CIDACS-PHDC — Project Documentation

This project organizes and publishes documentation for the **ETL pipeline** that maps **gestational syphilis** data to the **OMOP Common Data Model (CDM) v5.4**. It follows **OHDSI** community best practices, describing data sources, transformation rules, and target CDM tables with a focus on reproducibility and auditability.

### Goal
Harmonize clinical/epidemiological data for pregnant women and newborns into the standardized **OMOP CDM**, enabling:
- reproducible, comparable analyses across studies,
- integration with standard vocabularies,
- traceability of ETL business rules.

### Scope and key mappings
The ETL covers the core CDM entities relevant to gestational syphilis:

- **`PERSON`**: identifies pregnant women and newborns (when applicable).
- **`OBSERVATION_PERIOD`**: per-person observation windows.
- **`VISIT_OCCURRENCE`**: prenatal care, delivery, and other encounters.
- **`CONDITION_OCCURRENCE`**: clinical conditions (e.g., gestational syphilis) with standardized `condition_concept_id`.
- **`MEASUREMENT`**: pertinent lab results (e.g., VDRL/RPR, treponemal tests)
- **`DRUG_EXPOSURE`**: therapies/antibiotics (e.g., penicillin)
- **`PROCEDURE_OCCURRENCE`**: procedures in maternal–infant care.
- **`FACT_RELATIONSHIP`**: **mother–infant** links, preserving relationships across records.

> When local codes exist, they are mapped to **standard concepts** via OMOP vocabulary tables; source codes remain in `*_source_value`/`*_source_concept_id` for traceability.

### Rules and data quality
- Clear documentation of transformation rules (filtering, date derivations, source precedence).
- Preference for standard concepts; use `concept_relationship` to find equivalences.
- Basic checks (key consistency, presence of dates, mother–infant coherence).
- Outputs validated against **CDM v5.4** target tables.

---

### PDF Reference

### Download

{download}`OHDSI ETL CDM v5.4 — Mapping Dataset Gestational Syphillis (PDF) <PDF_DOCUMENTATION/OHDSI_ETL_CDM_V5.4_Mapping_Dataset_Gestational_Syphillis.pdf>`

> If the inline viewer does not work in your browser, use “Open in a new tab”.

**Open in a new tab:**  
<a href="PDF_DOCUMENTATION/OHDSI_ETL_CDM_V5.4_Mapping_Dataset_Gestational_Syphilis.pdf" target="_blank" rel="noopener">
  OHDSI ETL CDM v5.4 — Mapping Dataset Gestational Syphilis
</a>





