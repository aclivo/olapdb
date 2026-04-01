# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## Project Overview
olapdb is a Python OLAP reference study project in early development.

Current package metadata (from `pyproject.toml`):
- Name: `olapdb`
- Version: `0.1.0`
- Python requirement: `>=3.14`
- Build backend: `uv_build`
- Runtime dependencies: none (currently)
- Dev dependencies group: `pytest`, `pytest-cov`

## Commands

Current useful commands:
- **Run all tests:** `uv run pytest`
- **Run tests with coverage:** `uv run pytest --strict --durations 5 --verbose -r A --tb auto --cov --cov-report=term`

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

## Output
- Return code first. Explanation after, only if non-obvious.
- No inline prose. Use comments sparingly - only where logic is unclear.
- No boilerplate unless explicitly requested.

## Code Rules
- Simplest working solution. No over-engineering.
- No abstractions for single-use operations.
- No speculative features or "you might also want..."
- Read the file before modifying it. Never edit blind.
- No docstrings or type annotations on code not being changed.
- No error handling for scenarios that cannot happen.
- Three similar lines is better than a premature abstraction.

## Review Rules
- State the bug. Show the fix. Stop.
- No suggestions beyond the scope of the review.
- No compliments on the code before or after the review.

## Debugging Rules
- Never speculate about a bug without reading the relevant code first.
- State what you found, where, and the fix. One pass.
- If cause is unclear: say so. Do not guess.

## Simple Formatting
- No em dashes, smart quotes, or decorative Unicode symbols.
- Plain hyphens and straight quotes only.
- Natural language characters (accented letters, CJK, etc.) are fine when the content requires them.
- Code output must be copy-paste safe.