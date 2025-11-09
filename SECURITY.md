# Security Policy

## ✅ Supported Versions

The following versions of the XPHRASE GENERATION are currently supported with security updates. Unsupported versions will not receive patches for vulnerabilities. To check your installed version, run `python xphrase.py --version`.

| Version | Supported          | End-of-Life Date       |
|---------|--------------------|------------------------|
| 1.0.x   | :white_check_mark: | TBD (Est. August 2026) |
| < 1.0   | :x:                | -                      |

## 🧪 Test PyPI Usage

The Test PyPI release of XPHRASE GENERATION is intended for testing and development purposes only. It may contain experimental features or unpatched vulnerabilities and should not be used in production environments. For production use, install the stable version from the official [Python Package Index (PyPI)](https://pypi.org/project/xphrase-generation/).

## 🛡️ Security Best Practices

To ensure the secure use of XPHRASE GENERATION:
- Use Python 3.8 or higher, keeping it updated to the latest patch version.
- Install the tool in a virtual environment to isolate dependencies.
- Verify package integrity during installation by checking the package's hash or signature (available on the [PyPI project page](https://pypi.org/project/xphrase-generation/)).
- Store generated phrases securely using a trusted password manager, such as [Bitwarden](https://bitwarden.com/).

## 🚨 Reporting a Vulnerability

If you discover a security vulnerability in the XPHRASE GENERATION, please report it promptly to protect the community. We consider vulnerabilities such as insecure random number generation, code execution flaws, or phrase generation weaknesses within scope. Follow these steps:

1. **Where to Report**: Email [ask@gerivan.me](mailto:ask@gerivan.me) with a detailed description of the vulnerability, including steps to reproduce, impact, and affected versions.
2. **Expected Response Time**: You will receive an acknowledgment within 48 hours. A detailed update, including assessment and resolution plan, will be provided within 7 business days.
3. **Resolution Process**:
   - **Accepted Vulnerabilities**: We will prioritize a fix based on severity (e.g., critical issues patched within 30 days) and deploy it in the next supported release.
   - **Declined Vulnerabilities**: If the issue is not reproducible, out of scope, or not a vulnerability, you will be notified with an explanation.
4. **Responsible Disclosure Timeline**:
   - Acknowledgment: Within 48 hours.
   - Initial assessment: Within 7 business days.
   - Patch release: Within 30–60 days, depending on severity.
   - Public disclosure: Coordinated with the reporter, typically after the patch is released.
5. **Confidentiality**: Do not disclose the vulnerability publicly until we have resolved it and provided clearance. Responsible reporters may be acknowledged publicly (with consent) in release notes.
6. **Contact for Queries**: For questions about the process, email [ask@gerivan.me](mailto:ask@gerivan.me).

---

#### Copyright © 2025 Gerivan Costa dos Santos
