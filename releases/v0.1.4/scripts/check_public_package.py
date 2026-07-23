"""Check that the companion package contains only releasable materials."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_DIRS = {"data", "generator", "model_weights", "__pycache__", "drafts"}
FORBIDDEN_SUFFIXES = {".pth", ".pt", ".ckpt", ".pkl", ".pickle", ".ipynb"}
FORBIDDEN_NAME_PARTS = {"rungekutta", "headerless", "model_weight"}

FORBIDDEN_CONTENT_MARKERS = {"F:" + "\\", "C:" + "\\", ".pth", ".pt", ".ckpt", "model_weights"}

CONTENT_SCAN_SUFFIXES = {".txt", ".md", ".csv", ".json", ".py", ".cff", ".yml", ".yaml"}
CONTENT_SCAN_ROOTS = {"results", "figures"}

ALLOWED_STAGE2_TABLES = {
    "b2_ng2d_regime_summary_2026-04-10.csv",
    "b2_ng2d_target_summary_2026-04-10.csv",
    "ekf_validity_envelope_grid.csv",
    "kappa_threshold_rule_summary.csv",
    "observability_gramian_analysis.csv",
    "replacement_protocol_v1__baseline_vs_replacement_v1__full_dataset__summary.csv",
    "replacement_protocol_v1__baseline_vs_replacement_v1__full_matched__per_family_bootstrap_ci.csv",
    "replacement_protocol_v1__baseline_vs_replacement_v1__full_matched__summary.csv",
    "replacement_protocol_v1__baseline_vs_replacement_v1__near_window_2400tracks_2026_04_04_matched_slice__per_family_bootstrap_ci.csv",
    "replacement_protocol_v1__baseline_vs_replacement_v1__near_window_2400tracks_2026_04_04_matched_slice__summary.csv",
}

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "LICENSE-DATA",
    "CITATION.cff",
    ".zenodo.json",
    "docs/data_access_note.md",
    "docs/supplementary_materials_guide.md",
    "docs/checksums_sha256.txt",
    "scripts/list_release_files.py",
]


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def scan_text_content(path: Path) -> None:
    if path.suffix.lower() not in CONTENT_SCAN_SUFFIXES:
        return
    rel = path.relative_to(ROOT)
    if not rel.parts or rel.parts[0] not in CONTENT_SCAN_ROOTS:
        return
    try:
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
    except OSError as exc:
        fail(f"could not read file for content scan: {rel.as_posix()} ({exc})")
    for marker in FORBIDDEN_CONTENT_MARKERS:
        if marker.lower() in text:
            fail(f"restricted content marker {marker!r} present in {rel.as_posix()}")


def main() -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            fail(f"missing required file: {rel}")

    files = [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]

    for path in files:
        rel = path.relative_to(ROOT)
        parts = set(rel.parts)
        if parts & FORBIDDEN_DIRS:
            fail(f"restricted directory present: {rel.as_posix()}")
        if path.suffix in FORBIDDEN_SUFFIXES:
            fail(f"restricted file suffix present: {rel.as_posix()}")
        if any(marker.lower() in path.name.lower() for marker in FORBIDDEN_NAME_PARTS):
            fail(f"restricted file name present: {rel.as_posix()}")
        scan_text_content(path)

    stage2_dir = ROOT / "results/stage2"
    if stage2_dir.is_dir():
        actual_stage2 = {p.name for p in stage2_dir.glob("*.csv")}
        unexpected = actual_stage2 - ALLOWED_STAGE2_TABLES
        missing = ALLOWED_STAGE2_TABLES - actual_stage2
        if unexpected:
            fail("unexpected Stage-II table(s): " + ", ".join(sorted(unexpected)))
        if missing:
            fail("missing expected Stage-II table(s): " + ", ".join(sorted(missing)))

    figure_count = len(list((ROOT / "figures/final_manuscript_pdf").glob("*.pdf")))
    support_tables = len(list((ROOT / "results/stage2_support").glob("*.csv")))
    calibration_tables = len(list((ROOT / "results/calibration_support/csv").glob("*.csv")))
    calibration_figures = len(list((ROOT / "figures/calibration_support").glob("*.pdf")))
    stage2_tables = len(list((ROOT / "results/stage2").glob("*.csv")))
    fit_tables = len(list((ROOT / "results/fit_readiness").glob("*.csv")))

    print(f"files_checked: {len(files)}")
    print(f"final_pdf_figures: {figure_count}")
    print(f"stage2_csv_tables: {stage2_tables}")
    print(f"fit_readiness_csv_tables: {fit_tables}")
    print(f"stage2_support_csv_tables: {support_tables}")
    print(f"calibration_support_csv_tables: {calibration_tables}")
    print(f"calibration_support_pdf_figures: {calibration_figures}")
    print("source_data_and_model_weights: absent")
    print("status: ok")


if __name__ == "__main__":
    main()
