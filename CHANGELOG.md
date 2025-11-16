# Changelog

[![Keep a Changelog](https://img.shields.io/badge/Keep%20a%20Changelog-1.0.0-orange)](https://keepachangelog.com/en/1.0.0/)
[![Semantic Versioning](https://img.shields.io/badge/Semantic%20Versioning-2.0.0-blue)](https://semver.org/spec/v2.0.0.html)

All notable changes to the XPhrase Generation project are documented in this file. This project adheres to the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) standard, which ensures a structured and human-readable format for tracking changes. By following this approach, we provide clear visibility into the project's evolution, making it easier for users and contributors to understand what has been added, changed, or fixed in each release. Additionally, the project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html) (SemVer), which uses a versioning scheme of MAJOR.MINOR.PATCH. This practice enhances predictability and compatibility by clearly indicating the impact of updates: major versions for breaking changes, minor versions for new features, and patch versions for bug fixes. Together, these standards improve the project's maintainability, transparency, and usability for developers and security enthusiasts.

---

## [1.0.0] - 2025-11-16

### Created
- Create XPHRASECALCULATION.md

### Added
- New interactive mode with structured menu options
- Word count validation (3-21 words per phrase)
- Phrase count validation (5-10 phrases for multiple generation)
- Specific count-based generation with `--count` argument (5-10 words)

### Revised
- Complete overhaul of CLI interface section in README.md
- Updated command behavior and usage examples
- Restructured interactive mode workflow

### Updated
- Default command behavior to generate exactly 8 words
- `--count` argument to accept specific word counts (5-10)
- Interactive mode to include two-step phrase generation
- Documentation to reflect new generation rules

### Fixed
- Clear separation between single and multiple phrase generation
- Consistent word count ranges across all interfaces

### Reordered
- CLI argument examples by functionality
- Interactive mode options for better user flow

### Deleted
- Legacy interactive mode structure
- Obsolete command examples from previous versions


## [1.0.0] - 2025-11-10
### Created
- Create CHANGELOG.md


## [1.0.0] - 2025-11-09

### Added
- Add bug report template for XPHRASE GENERATION

### Created
- Create config.yml
- Create issue_template.md
- Create SECURITY.md for security policy and practices

### Updated
- Update CONTRIBUTING.md for clarity and copyright
- Update index.html


## [1.0.0] - 2025-11-08

### Added
- Add installation instructions for Linux
- Add unit tests for XPhrase generation
- Add initial test package for XPhrase Generation

### Revised
- Revise README with installation and usage details

### Updated
- Update word_manager.py
- Update CNAME file

### Fixed
- Fix order of languages in module docstring

### Reordered
- Reorder language imports and dictionary entries

### Deleted
- Delete docs/CNAME


## [1.0.0] - 2025-11-07

### Added
- Add index.html for XPhrase Generation project
- Add .nojekyll file to prevent Jekyll processing
- Add Jekyll configuration for documentation site
- Add CNAME file for custom domain
- Add CNAME for custom domain
- Add WordManager class for language word management
- Add XPhraseGenerator for expressive phrase generation
- Add setup.py for xphrase package configuration
- Add requirements.txt for future dependencies
- Add GitHub Actions workflow for PyPI publishing
- Add CI workflow for XPhrase Generator

### Created
- Create CNAME
- Create portuguese_words.py
- Create english_words.py
- Create german_words.py

### Updated
- Update GERMAN_WORDS

### Removed
- Remove Black and Flake8 configuration from pyproject
- Remove flake8 linting from Python CI workflow

### Fixed
- Fix formatting in pyproject.toml

### Initialized
- Initialize data module for XPhrase Generation

---

#### Copyright © 2025 Gerivan Costa dos Santos
