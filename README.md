# Stage-Resolved Tracking Benchmark Public Materials

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20340321.svg)](https://doi.org/10.5281/zenodo.20340321)

This repository contains the public companion package for the manuscript:

Stage-resolved bottlenecks from track finding to fitting in layered detectors

Archived release DOI: https://doi.org/10.5281/zenodo.20340321

Concept DOI for all versions: https://doi.org/10.5281/zenodo.20340320

## Scope

This is not the full internal reproducibility package. It is a public-safe package prepared for manuscript review and open documentation while permission for redistributing the original benchmark generator and dataset remains unconfirmed.

Included materials:

- Final manuscript figure assets in PDF and PNG format.
- Frozen aggregate result tables used to document the reported stage-level anchors.
- Sanitized Stage-II summary tables with restricted source identifiers removed.
- Calibration-audit summary tables and supporting figures added for the revised Stage-II claims.
- Lightweight scripts for listing files and checking the public package.
- Documentation describing what is included, what is excluded, and how to interpret the release.

Excluded materials:

- The original Runge-Kutta generator notebook.
- Any cleaned or converted generator code derived from the original notebook.
- The canonical SiHits_3D dataset.
- Headerless Stage-I working copies derived from the canonical dataset.
- Stage-II near-window data files derived from the canonical dataset.
- Per-track or per-event diagnostic tables derived from restricted data.
- Trained model-weight files.
- Internal project plans, review prompts, working notes, draft manuscripts, private paths, and exploratory outputs.

The excluded generator and data materials were provided to the project by the project supervisor. They are not redistributed in this public package because explicit permission for public redistribution has not yet been confirmed.

## Directory Layout

```text
figures/
  final_manuscript_pdf/      Final figure assets used in the manuscript.
  R2_stats/                  Supporting figures for the Stage-II handoff audit.
  R7_stats/                  Five supporting figure sets for the calibration audit.
results/
  fit_readiness/             Aggregate fit-readiness summary tables.
  stage2/                    Aggregate Stage-II summary and diagnostic tables.
  R2_stats/                  Public-safe aggregate R2 audit tables.
  R7_stats/                  Public-safe aggregate R7 calibration-audit tables.
scripts/
  check_public_package.py    Public-safe verification script.
  list_release_files.py      Utility for listing release contents.
docs/
  public_release_policy.md   Data and redistribution policy for this package.
  revision_support_inventory_2026-07-06.md
  checksums_sha256.txt       SHA256 checksums for included files.
LICENSE                      MIT License for code.
LICENSE-DATA                 CC BY 4.0 for included documentation, result tables, and figures.
```

## Quick Check

Run:

```bash
python scripts/check_public_package.py
```

Expected final line:

```text
status: ok
```

This check verifies that the public package does not contain the restricted generator, canonical dataset, derived working copies, per-track diagnostic exports, trained model weights, private paths, or submission-process notes.

## Data Availability Language

For the revised manuscript, use:

A public companion package for this manuscript is archived on Zenodo (DOI: 10.5281/zenodo.20340321) and mirrored in the GitHub repository `stage-resolved-tracking-benchmark-public`. It contains final PDF figures, aggregate result tables, sanitized Stage-II summaries, documentation, and public-safe verification scripts. The revised public package also includes the calibration-audit summaries and supporting figures used to trace the revised Stage-II audit claims. The original benchmark generator, the canonical SiHits_3D dataset, derived working copies, near-window data, per-track diagnostic exports, and trained model weights are not publicly redistributed because permission for public redistribution has not been confirmed. Data and code supporting the full internal analyses are available from the authors upon reasonable request, subject to applicable permission constraints.

## License

Code in this package is released under the MIT License. Included result tables, figure assets, and documentation are released under Creative Commons Attribution 4.0 International (CC BY 4.0), subject to the exclusions described above.
