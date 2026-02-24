# Decisions

<!-- Record architectural, tooling, and convention decisions as they are made.
     Append new entries — never edit existing ones.
     Format: date, short title, one-line Decision, detailed Rationale. -->

## 2025-04-17 — Initial stack selection

**Decision:** Use Python with conda for environment management, Jupyter notebooks for exploration, and a src/ module structure for reusable code.

**Rationale:** Conda provides reproducible environments with pinned dependencies. Separating notebooks (exploration) from src/ (production code) keeps the codebase clean as the project grows. This matches standard ML project conventions.
