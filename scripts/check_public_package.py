"""Check that the public companion package does not contain restricted files.

This script is intentionally conservative. It verifies that the package includes
only public-safe materials: aggregate result tables, final PDF figures,
documentation, metadata, and lightweight scripts.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_DIRS = {"data", "generator", "model_weights", "__pycache__"}
FORBIDDEN_SUFFIXES = {".pth", ".pt", ".ckpt", ".pkl", ".pickle", ".ipynb"}
FORBIDDEN_NAME_PARTS = {
    "SiHits_3D",
    "RungeKuttaEventsVtx",
    "data_aoran_headerless",
    "data_lu_headerless",
    "data_wang_headerless",
    "baseline_manifest",
    "non_gaussian_validation",
}

FORBIDDEN_CONTENT_TOKENS = {
    "SiHits_3D",
    "RungeKuttaEventsVtx",
    "data_aoran_headerless",
    "data_lu_headerless",
    "data_wang_headerless",
    "dataset_file",
    "source_file",
    ".pth",
    ".pt",
    ".ckpt",
    "model_weights",
}

CONTENT_SCAN_DIRS = {
    "results",
    "figures",
}

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
    "docs/public_release_policy.md",
    "docs/checksums_sha256.txt",
    "scripts/list_release_files.py",
]


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def protected_content_file(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return bool(rel.parts and rel.parts[0] in CONTENT_SCAN_DIRS)


def scan_text_content(path: Path) -> None:
    if not protected_content_file(path):
        return
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError as exc:
        fail(f"could not read file for content scan: {path.relative_to(ROOT).as_posix()} ({exc})")
    for token in FORBIDDEN_CONTENT_TOKENS:
        if token in text:
            fail(f"restricted content token {token!r} present in {path.relative_to(ROOT).as_posix()}")


def main() -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            fail(f"missing required file: {rel}")

    files = [p for p in ROOT.rglob("*") if p.is_file()]

    for path in files:
        rel = path.relative_to(ROOT)
        parts = set(rel.parts)
        if parts & FORBIDDEN_DIRS:
            fail(f"restricted directory present: {rel.as_posix()}")
        if path.suffix in FORBIDDEN_SUFFIXES:
            fail(f"restricted file suffix present: {rel.as_posix()}")
        if any(token in path.name for token in FORBIDDEN_NAME_PARTS):
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
    stage2_tables = len(list((ROOT / "results/stage2").glob("*.csv")))
    fit_tables = len(list((ROOT / "results/fit_readiness").glob("*.csv")))

    print(f"files_checked: {len(files)}")
    print(f"final_pdf_figures: {figure_count}")
    print(f"stage2_csv_tables: {stage2_tables}")
    print(f"fit_readiness_csv_tables: {fit_tables}")
    print("restricted_generator_data_weights: absent")
    print("status: ok")


if __name__ == "__main__":
    main()
