# Contributing to XPHRASE GENERATION

Thank you for your interest in contributing to the **XPHRASE GENERATION**! This project provides an expressive phrase generator that creates strong, modern, and minimalist phrases in multiple languages (English, German, Portuguese), and we welcome contributions to enhance its functionality, documentation, and accessibility. Whether you're fixing bugs, adding features, improving documentation, or contributing in other ways, your efforts are greatly appreciated.

---

## 🤝 Ways to Contribute

You can contribute to the XPHRASE GENERATION in several ways:
- **Code**: Fix bugs, add new features, or optimize existing functionality in `src/xphrase/main.py` and `src/xphrase/word_manager.py`.
- **Documentation**: Improve `README.md`, `SECURITY.md`, or add inline comments and docstrings.
- **Word Banks**: Contribute to or expand the multilingual word banks in the `src/xphrase/data/` directory.
- **Issues**: Report bugs, suggest features, or propose documentation enhancements via GitHub Issues.
- **Translations**: Translate documentation or add support for additional languages.
- **Testing**: Validate functionality across different Python versions or platforms.

---

## 🚀 Getting Started

### ⚙️ 1. Setting Up Your Environment
To contribute, set up a local development environment:
1. **Install Python**: Ensure you have Python 3.8 or higher installed (tested on 3.10–3.12).
2. **Clone the repository**:
   ```bash
   git clone https://github.com/gerivanc/xphrase.git
   cd xphrase
   ```
3. **Create a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   **On Windows**:
   ```bash
   python -m venv xphrase_venv
   .\xphrase_venv\Scripts\Activate.ps1
   ```
4. **Install the package in editable mode** (required for development):
   ```bash
   pip install -e .
   ```
   This enables running the CLI as `python -m xphrase.main` or using the `run.py` script.
5. **Install development tools** (optional, but recommended):
   ```bash
   pip install flake8 black isort pytest
   ```
   These tools help ensure code quality:
   - `flake8`: Linting to enforce PEP 8.
   - `black`: Automatic code formatting.
   - `isort`: Sorting imports.
   - `pytest`: Enhanced testing.

### 📢 2. Reporting Issues
If you find a bug, have a feature request, or notice documentation that needs improvement:
- **Search existing issues**: Check the [GitHub Issues page](https://github.com/gerivanc/xphrase/issues) to avoid duplicates.
- **Provide details**: Include a clear title, description, steps to reproduce (if applicable), expected behavior, and screenshots or logs.
- **Security issues**: For vulnerabilities, follow the process in [SECURITY.md](https://github.com/gerivanc/xphrase/blob/main/SECURITY.md) instead of opening a public issue.

### 🔄 3. Submitting Pull Requests
To contribute code, documentation, or other changes:
1. **Fork the repository** and create a new branch for your feature (e.g., `git checkout -b feature/add-spanish-support`).
2. **Make your changes**: Follow the coding standards below.
3. **Test locally**: Ensure your changes pass all checks (see "Testing" section).
4. **Commit and push**:
   ```bash
   git add .
   git commit -m "feat: add Spanish word bank support"
   git push origin feature/add-spanish-support
   ```
5. **Open a Pull Request**: Link to the issue (if applicable) and describe your changes clearly.

### 📝 4. Coding Standards
- **Style Guide**: Use PEP 8. Run `black src/` and `isort src/` before committing.
- **Comments and Docstrings**: All code comments and docstrings must be in English. Use clear, concise language.
- **Imports**: Use absolute imports (e.g., `from xphrase.word_manager import WordManager`) to avoid relative import issues.
- **Phrase Generation Rules**: Any new features must adhere to the core formula:
  - Mix words from English, German, and Portuguese (or new languages).
  - Separate words with random special character + digit (e.g., `@3`, `#7`).
  - End the last word with an uppercase letter.
  - CLI modes: Default (8 words), `--count N` (5–10 words exact), `--min M --max X` (random M–X, 3–21), `--interactive` (menu for single/multiple).
- **Word Management**: Updates to word banks in `src/xphrase/data/` should maintain alphabetical order and avoid duplicates.
- **Licensing**: By contributing, you agree that your contributions are licensed under the [MIT License](https://github.com/gerivanc/xphrase/blob/main/LICENSE).

### 🧪 5. Testing
Ensure your changes do not break existing functionality:
- **Manual Testing** (use `./run.py` or `python -m xphrase.main`):
  - Default: `./run.py` (generates 1 phrase with exactly 8 words).
  - Exact count: `./run.py --count 5` (generates 1 phrase with exactly 5 words; valid 5–10).
  - Random range: `./run.py --min 5 --max 10` (generates 1 phrase with 5–10 words randomly).
  - Interactive: `./run.py --interactive` (menu: option 1 for single phrase with 3–21 words; option 2 for 5–10 phrases, each 3–21 words).
  - Version: `./run.py --version` (shows "XPhrase Generation v1.0.3").
  - Verify generated phrases: Check for mixed languages, separators (special + digit between words), and final uppercase letter (no separator at end).
- **Automated Testing**:
  - Run unit tests: `python -m unittest discover tests/ -v` (or `pytest` if installed).
  - Ensure all tests pass (coverage: word selection, separators, CLI args, phrase structure).
- **Cross-Version Testing**:
  - Test with Python 3.8, 3.10, 3.11, and 3.12 to ensure compatibility.
- **Word Bank Testing**:
  - Validate that word banks in `src/xphrase/data/` are properly loaded and words are correctly selected (no empty pools).

### ✅ 6. Pull Request Review Process
After submitting a PR:
- **Review Time**: The maintainer will review your PR within 7 business days. Complex changes may take longer.
- **Criteria**: PRs are evaluated based on code quality, adherence to standards, security, and alignment with project goals.
- **Feedback**: You may be asked to make revisions. Address feedback promptly to expedite merging.
- **Approval**: PRs require approval from the maintainer (Gerivan Costa dos Santos) before merging.
- **CI Checks**: Ensure all GitHub Actions checks pass (linting, tests, build). Fix any failures reported in the workflow.

### 🤗 7. Code of Conduct
We are committed to fostering an inclusive and respectful community. Please:
- Be kind, respectful, and professional in all interactions.
- Avoid offensive language, harassment, or discriminatory behavior.
- Report inappropriate behavior to the maintainer at [ask@gerivan.me](mailto:ask@gerivan.me).
Violations may result in exclusion from the project.

### ❓ 8. Getting Help
For questions or assistance:
- Read the [README.md](https://github.com/gerivanc/xphrase/blob/main/README.md) for project details.
- Check the [SECURITY.md](https://github.com/gerivanc/xphrase/blob/main/SECURITY.md) for vulnerability reporting.
- Open an issue on the [GitHub Issues page](https://github.com/gerivanc/xphrase/issues).
- Contact the maintainer at [ask@gerivan.me](mailto:ask@gerivan.me).

### 🙌 9. Acknowledgments
Thank you for contributing to the **XPHRASE GENERATION**! Your efforts help make this tool more expressive, secure, and valuable for users worldwide. Significant contributors may be acknowledged in the project's documentation or release notes (with your consent).

---

#### Copyright © 2025 Gerivan Costa dos Santos
