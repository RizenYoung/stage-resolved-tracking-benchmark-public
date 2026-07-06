# R7 Public Calibration-Audit Tables

This directory contains aggregate calibration-audit tables used to support the revised Stage-II discussion.

Included tables:

- `csv/R7_1_charge_flip_leakage.csv`
- `csv/R7_2_pull_mechanism.csv`
- `csv/R7_2_pull_policy_path_summary.csv`
- `csv/R7_3_extreme_tail_profile.csv`
- `csv/R7_3_top_tail_tracks.csv`
- `csv/R7_4_false_rejection_risk.csv`
- `csv/R7_4_pit_coverage.csv`
- `csv/R7_5_tail_family_comparison.csv`
- `csv/R7_6_tau_l_coverage.csv`
- `csv/R7_6_tau_l_coverage_summary.csv`
- `csv/R7_7_kdim3_empirical_corr.csv`

Interpretation summary:

- Pull widening is the dominant curvilinear-pull mechanism in the tested sample; bias dominance is not supported.
- Top pull tails are not confined to the most extreme transport-invalid regime.
- PIT and coverage checks show conservative behavior with shape departures.
- Tail-family behavior is stratum-specific rather than universal.
- The scale scan does not support a universal 0.80 rescaling recommendation.

The symbolic covariance note is stored as `R7_7_kdim3_covariance_structure.md`. Related figures are stored in `figures/R7_stats/`.
