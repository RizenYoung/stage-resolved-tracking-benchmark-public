# Stage-Resolved Tracking Benchmark Public Materials

This repository contains a restricted public companion package for the manuscript:

Stage-resolved bottlenecks from track finding to fitting in layered detectors

## Scope

This is not the full internal reproducibility package. It is a public-safe package prepared for manuscript review and open documentation while permission for redistributing the original benchmark generator and dataset remains unconfirmed.

Included materials:

- Final manuscript figure assets in PDF format.
- Frozen aggregate result tables used to document the reported stage-level anchors.
- Sanitized Stage-II summary tables with restricted source-file identifiers removed.
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
  final_manuscript_pdf/      Final PDF figure assets used in the manuscript.
results/
  fit_readiness/             Aggregate fit-readiness summary tables.
  stage2/                    Aggregate Stage-II summary and diagnostic tables.
scripts/
  check_public_package.py    Public-safe verification script.
  list_release_files.py      Utility for listing release contents.
docs/
  public_release_policy.md   Data and redistribution policy for this package.
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

This check verifies that the public package does not contain the restricted generator, canonical SiHits_3D data, derived data copies, per-track diagnostic exports, or model-weight files.

## Data Availability Language

For the manuscript, the safest current data availability statement is:

Data and code supporting this work are available from the authors upon reasonable request.

If referring specifically to this public package, use wording such as:

Aggregate result tables, figure assets, and public documentation are available in the public companion repository. The original benchmark generator, canonical SiHits_3D dataset, derived working copies, and model weights are not publicly redistributed because permission for public redistribution has not yet been confirmed.

## License

Code in this package is released under the MIT License. Included result tables, figure assets, and documentation are released under Creative Commons Attribution 4.0 International (CC BY 4.0), subject to the exclusions described above.
