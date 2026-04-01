# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

OlapDB is a Python OLAP reference study project in early development.

Current package metadata (from `pyproject.toml`):
- Name: `olapdb`
- Version: `0.1.0`
- Python requirement: `>=3.14`
- Build backend: `uv_build`
- Runtime dependencies: none (currently)
- Dev dependencies group: `pytest`, `pytest-cov`

## Development Setup

Use a local virtual environment (example shown with `.venv`):
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
pip install pytest pytest-cov
```

Alternative (if using `uv`):
```bash
uv sync --dev
```

## Commands

Current useful commands:
- **Run all tests:** `pytest`
- **Run one test file:** `pytest tests/test_connection.py`
- **Run one test case:** `pytest tests/test_connection.py::TestConnection::test_connect`
- **Run tests with coverage:** `pytest --cov=olapdb --cov-report=term-missing`

If using `uv`, prefix with `uv run` (example: `uv run pytest`).

## Architecture

Current minimal architecture:

- Package entrypoint: `src/olapdb/__init__.py` re-exports `connect`.
- Connection module: `src/olapdb/connection.py` defines:
	- `connect() -> Connection`: factory function returning a `Connection` instance.
	- `Connection`: placeholder connection class (currently empty).
- Tests: `tests/test_connection.py` verifies `connect()` returns a non-`None` connection object.

Notes:
- The package is intentionally minimal right now.
- As new modules are added, keep this section updated with concrete components and their responsibilities.
