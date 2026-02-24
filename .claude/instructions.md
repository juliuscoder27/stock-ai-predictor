# Claude Code Instructions

## Source of Truth

Read README.md before starting any non-trivial task. It is the authoritative reference for project architecture and intent.

## Constraints

- **Python environment:** This project uses Python via Miniconda (`/opt/miniconda3`). No conda environment has been created yet — do not assume `stockai` or any other environment exists.
- **Data files:** The `data/` directory contains CSV files that must never be committed. They are already covered by `.gitignore` (`/data/*.csv`), but never stage or commit anything from `data/`.
- **Environment definition:** `environment.yml` defines the intended environment. When an environment is needed, create it with `conda env create -f environment.yml`.

## Out of Scope

- Do not modify files in `data/` — treat them as read-only inputs.
- Do not push to GitHub without explicit instruction.
