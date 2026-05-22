# Public Release Policy

This public package follows a conservative redistribution policy.

## Publicly Included

- Aggregate result tables that summarize manuscript-level diagnostics.
- Sanitized summary tables with restricted source-file identifiers removed.
- Final PDF figure assets used in the manuscript.
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

These materials are excluded because permission for public redistribution from the original provider has not yet been confirmed. The absence of a response is not treated as permission.

## Reproducibility Interpretation

This package supports inspection of aggregate results, figure assets, and documentation. It does not enable full end-to-end rerunning of the original benchmark pipeline. Full reproduction requires access to the restricted benchmark generator/data and, for trained-model checks, the corresponding model weights.

## Recommended Manuscript Statement

Data and code supporting this work are available from the authors upon reasonable request.

If this public package is cited separately, make clear that it is a public companion package containing aggregate result tables, final figures, and documentation, not a full redistribution of the original benchmark data and generator.
