# Contributing to XPHRASE GENERATION

Thank you for your interest in contributing to the **XPHRASE GENERATION**! This project provides an expressive phrase generator that creates strong, modern, and minimalist phrases in multiple languages, and we welcome contributions to enhance its functionality, documentation, and accessibility. Whether you're fixing bugs, adding features, improving documentation, or contributing in other ways, your efforts are greatly appreciated.

---

## 🤝 Ways to Contribute

You can contribute to the XPHRASE GENERATION in several ways:
- **Code**: Fix bugs, add new features, or optimize existing functionality in `xphrase.py` and `word_manager.py`.
- **Documentation**: Improve `README.md`, `SECURITY.md`, or add inline comments and docstrings.
- **Word Banks**: Contribute to or expand the multilingual word banks in the `data/` directory.
- **Issues**: Report bugs, suggest features, or propose documentation enhancements via GitHub Issues.
- **Translations**: Translate documentation or add support for additional languages.
- **Testing**: Validate functionality across different Python versions or platforms.

---

## 🚀 Getting Started

### ⚙️ 1. Setting Up Your Environment
To contribute, set up a local development environment:
1. **Install Python**: Ensure you have Python 3.8 or higher installed.
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
4. **Install development tools** (optional, but recommended):
   ```bash
   pip install flake8 black isort
   ```
   These tools help ensure code quality:
   - `flake8`: Linting to enforce PEP 8.
   - `black`: Automatic code formatting.
   - `isort`: Sorting imports.

### 📢 2. Reporting Issues
If you find a bug, have a feature request, or notice documentation that needs improvement:
- **Search existing issues**: Check the [GitHub Issues page](https://github.com/gerivanc/xphrase/issues) to avoid duplicates.
- **Provide details**: Include a clear title, description, steps to reproduce (if applicable), expected behavior, and screenshots or logs.
- **Security issues**: For vulnerabilities, follow the process in [SECURITY.md](https://github.com/gerivanc/xphrase/blob/main/SECURITY.md) instead of opening a public issue.

### 🔄 3. Submitting Pull Requests
To contribute code, documentation, or other changes, submit a pull request (PR):
1. **Fork the repository**:
   - Click the "Fork" button on the [repository page](https://github.com/gerivanc/xphrase).
   - Clone your fork:
     ```bash
     git clone https://github.com/gerivanc/xphrase.git
     cd xphrase
     ```
2. **Create a branch**:
   - Use a descriptive name (e.g., `feature/add-new-language`, `fix/word-selection-bug`):
     ```bash
     git checkout -b feature/your-feature-name
     ```
3. **Make changes**:
   - Follow the coding standards below.
   - Test changes locally (see "Testing" section).
   - Update documentation (e.g., `README.md`, docstrings) if necessary.
   - Run linting and formatting tools:
     ```bash
     flake8 .
     black .
     isort .
     ```
4. **Commit changes**:
   - Use clear, concise commit messages following the [Conventional Commits](https://www.conventionalcommits.org/) format (e.g., `feat: add German word support`, `fix: correct phrase length calculation`):
     ```bash
     git commit -m "feat: describe your change"
     ```
5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a pull request**:
   - Go to the [repository](https://github.com/gerivanc/xphrase) and click "New pull request".
   - Select your branch and provide a detailed description of your changes.
   - Reference related issues (e.g., "Fixes #123").
   - Ensure your PR passes the GitHub Actions CI checks (if configured).

### 📜 4. Coding Standards
To maintain consistency and security, adhere to these guidelines:
- **Python Version**: Use Python 3.8 or higher.
- **Style**: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for code style. Use `flake8` for linting and `black` for formatting.
- **Docstrings**: Write clear, English docstrings for all functions and modules.
- **Security**: Use the `secrets` module for cryptographic randomness. Avoid insecure libraries like `random`.
- **File Structure**: Keep changes within the existing structure (e.g., core logic in `xphrase.py`, word management in `word_manager.py`).
- **Licensing**: By contributing, you agree that your contributions are licensed under the [MIT License](https://github.com/gerivanc/xphrase/blob/main/LICENSE.md).

### 🧪 5. Testing
Ensure your changes do not break existing functionality:
- **Manual Testing**:
  - Run the CLI with different arguments:
    ```bash
    python xphrase.py
    python xphrase.py --count 5
    python xphrase.py --min 5 --max 10
    ```
  - Verify that generated phrases follow the specified rules (special characters, digits, final uppercase letter).
- **Cross-Version Testing**:
  - Test with Python 3.8, 3.10, and 3.12 to ensure compatibility.
- **Word Bank Testing**:
  - Validate that word banks in `data/` directory are properly loaded and words are correctly selected.

### ✅ 6. Pull Request Review Process
After submitting a PR:
- **Review Time**: The maintainer will review your PR within 7 business days. Complex changes may take longer.
- **Criteria**: PRs are evaluated based on code quality, adherence to standards, security, and alignment with project goals.
- **Feedback**: You may be asked to make revisions. Address feedback promptly to expedite merging.
- **Approval**: PRs require approval from the maintainer (Gerivan Costa dos Santos) before merging.
- **CI Checks**: Ensure all GitHub Actions checks (if configured) pass. Fix any failures reported in the workflow.

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
