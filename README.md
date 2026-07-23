# Stage-Resolved Tracking Benchmark: Public Companion Materials

This package accompanies the manuscript *Stage-resolved bottlenecks from track finding to fitting in layered detectors*.

Zenodo concept DOI: https://doi.org/10.5281/zenodo.20340320  
GitHub repository: https://github.com/RizenYoung/stage-resolved-tracking-benchmark-public

## Current Package

The current manuscript support package is provided in `releases/v0.1.4/`. The root-level v0.1.3 materials are retained for version traceability.

## Contents

- Final manuscript figure assets in PDF and PNG formats.
- Aggregate result tables for fit readiness and Stage-II analyses.
- Supporting calibration tables and five calibration figures.
- Documentation, citation metadata, licenses, and a package-validation script.

## Scope

The package supports inspection of the reported aggregate results, figure assets, and supporting calibration summaries. The original benchmark generator, the canonical `SiHits_3D` dataset, source-level event and track data, and trained model weights are not included because permission for their public redistribution has not been confirmed.

## Layout

```text
figures/
  final_manuscript_pdf/      Figure assets used in the manuscript.
  stage2_support/            Supporting Stage-II figures.
  calibration_support/       Five calibration-support figures.
results/
  fit_readiness/             Aggregate fit-readiness tables.
  stage2/                    Aggregate Stage-II tables.
  stage2_support/            Supporting Stage-II tables.
  calibration_support/       Calibration-support tables.
scripts/
  check_public_package.py    Package validation utility.
docs/
  data_access_note.md        Scope and redistribution note.
  supplementary_materials_guide.md
  checksums_sha256.txt       SHA-256 checksums for included files.
```

## Verification

Run:

```bash
python scripts/check_public_package.py
```

The expected final line is `status: ok`.

## Data Availability Statement

Figure assets, aggregate result tables, documentation, and supporting calibration summaries are available in the public companion package archived on Zenodo (concept DOI: 10.5281/zenodo.20340320) and mirrored in the GitHub repository `stage-resolved-tracking-benchmark-public`. The original benchmark generator, the canonical `SiHits_3D` dataset, and related source-level materials are not redistributed because permission for public redistribution has not been confirmed. Additional materials may be available from the corresponding author upon reasonable request, subject to applicable permission constraints.

## License

Code is released under the MIT License. Included result tables, figure assets, and documentation are released under CC BY 4.0.
