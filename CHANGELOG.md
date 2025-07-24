# Changelog

All notable changes to this project will be documented in this file, grouped by Added, Fixed, Changed, and Removed.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] -

### Added

### Fixed

### Changed
- replaced flake8 and black with ruff formatter and linter

### Removed

## [1.0.0] - 18th July 2025

### Added
- Repository name structure check, to ensure best practice

### Fixed

### Changed
- point readme towards govcookiecutter-lite, added section on original govcookiecutter
- Restructured setup questions to ask project name then org handle.

### Removed
- Project version from setup, default is 0.0.1
- locked down setup question, not needed as commit hooks have been removed
- removed all R files, not included in lite version
- removed overview setup question, a placeholder has been inserted into readme and project toml
- removed repo name question, instead derived from project name question
- hosting platform setup question, PR templates not included in lite version
- organisation name setup question, replaced with HMG in licence and code of conduct
- framework setup question, default aqa plan is replaced with framework from GDS


[1.0.0]: https://github.com/best-practice-and-impact/govcookiecutter-lite/tree/v1.0.0
