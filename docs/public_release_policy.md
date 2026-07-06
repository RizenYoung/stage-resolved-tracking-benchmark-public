# Public Release Policy

This public package follows a conservative redistribution policy.

## Publicly Included

- Aggregate result tables that summarize manuscript-level diagnostics.
- Sanitized summary tables with restricted source identifiers removed.
- Final PDF and PNG figure assets used in the manuscript.
- Supporting calibration-audit figures and aggregate tables for the revised Stage-II claims.
- Public-safe scripts that inspect this package.
- Documentation and metadata for citation and reuse.

## Not Publicly Redistributed

The following materials are intentionally excluded:

- The original Runge-Kutta event generator notebook.
- Any cleaned or translated generator implementation derived from the original notebook.
- The canonical SiHits_3D benchmark dataset.
- Headerless working copies derived from the canonical dataset.
- Near-window enrichment data derived from the canonical dataset.
- Per-track or per-event diagnostic exports derived from restricted data.
- Trained model weights.
- Private file paths, working prompts, draft text, and local audit scratch files.

These materials are excluded because permission for public redistribution from the original provider has not yet been confirmed. The absence of a response is not treated as permission.

## Reproducibility Interpretation

This package supports inspection of aggregate results, figure assets, and documentation. It does not enable full end-to-end rerunning of the original benchmark pipeline. Full reproduction requires access to the restricted benchmark generator/data and, for trained-model checks, the corresponding model weights.

## Recommended Manuscript Statement

A public companion package for this manuscript is archived on Zenodo (DOI: 10.5281/zenodo.20340321) and mirrored in the GitHub repository `stage-resolved-tracking-benchmark-public`. It contains final PDF figures, aggregate result tables, sanitized Stage-II summaries, documentation, and public-safe verification scripts. The revised public package also includes the calibration-audit summaries and supporting figures used to trace the revised Stage-II audit claims. The original benchmark generator, the canonical SiHits_3D dataset, derived working copies, near-window data, per-track diagnostic exports, and trained model weights are not publicly redistributed because permission for public redistribution has not been confirmed. Data and code supporting the full internal analyses are available from the authors upon reasonable request, subject to applicable permission constraints.
