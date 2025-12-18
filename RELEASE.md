# XPhrase Generation v1.0.4

**Release Date:** December 01th, 2025

Released on 	2025/11/22 	

Last updated 	2025/12/01

Publisher 	[gerivanc](https://github.com/gerivanc/)

Changelog [Changelog](https://github.com/gerivanc/xphrase/blob/main/CHANGELOG.md)

Release Notes [RELEASE.md](https://github.com/gerivanc/xphrase/blob/main/RELEASE.md)

Reporting Issues	[Report a](https://github.com/gerivanc/xphrase/issues/new/choose)

---

# 🌍 Interactive Web Version

Experience the XPhrase Generation directly in your browser! The web version offers all the functionality of the Python script in an intuitive and responsive interface.

### 🚀 Access the Web Version

<div align="center">
  
[**🌐 Try It Now on XPhrase Generation**](https://xphrase.gerivan.me/xphrase.html)

</div>

### ⚡ Interactive Demo

<div align="center">

[**📚 Interactive Readme**](https://xphrase.gerivan.me/)

</div>

---

# 📋 Overview
The **XPhrase Generation** v1.0.4 is now available on [Test PyPI](https://test.pypi.org/project/xphrase/) and [PyPI](https://pypi.org/project/xphrase/)! This release builds on the improvements from v1.0.4, adding a GitHub Actions badge to the project documentation to reflect the status of CI/CD workflows and updating the version references to v1.0.4. 
The principle of randomness enables the generation of over 12.6 trillion unique combinations by interconnecting words from three languages, along with the inclusion of special characters and numerical digits.

# ✨ What's New
- Updated version references in `README.md` from `v1.0.3` to `v1.0.4`. Updates to all layout structures and section titles. 
- Adjusted layout styling and emoji use for better readability and visual identity.
- Corrected anchor links in the Table of Contents that were not functioning due to emoji or formatting conflicts. 

This project is:
- 💯 Written 100% in Python
- 🖥️ CLI-compatible for Linux and Windows
- 🌐 The CLI project has been fully converted to the web version of the HTML interface, maintaining the same phrase generation method, now accessible directly in your browser.

## 📋 Requirements

- Python 3.8+
- No external dependencies
- Works on:
  - ✅ Linux (Debian, Ubuntu, Arch, etc.)
  - ✅ Windows (PowerShell, CMD)

---

# 💾 Installation

Cloning the repository to install packages.

```
git clone https://github.com/gerivanc/xphrase.git
cd xphrase
```

---

# 📟 Command Line Interface - Virtual environment
## 📦 Stable Version Installation (PyPI)

To install the stable version from PyPI on Kali Linux, execute the following commands step-by-step:

```bash
python3 -m venv venv-stablepypi
source venv-stablepypi/bin/activate
python -m ensurepip --upgrade
pip install --upgrade pip
pip install xphrase
pip list
```

## 🛠️ After installation, navigate to the directory where the XPhrase Generation repository folder was installed, then choose one of the following options to generate the phrases:
### 🧪  Mode 'echo PYTHONPATH='

#### 5️⃣🔟 The parameter should be between 5 and 10 words long. 

```
echo 'PYTHONPATH=src python src/xphrase/main.py "$@"' > xphrase.sh
chmod +x xphrase.sh
./xphrase.sh --count 10
```

#### ➖➕ Defines the minimum and maximum number of words to be generated in the sentence. --min and --max must be between 3-21 and min <= max.
```
echo 'PYTHONPATH=src python src/xphrase/main.py "$@"' > xphrase.sh
chmod +x xphrase.sh
./xphrase.sh --min 5 --max 21
```

#### 📋🔘 Interactive menu - generates unique and multiple phrases.
```
echo 'PYTHONPATH=src python src/xphrase/main.py "$@"' > xphrase.sh
chmod +x xphrase.sh
./xphrase.sh --interactive
```

#### 📦✨ Show which version of XPhrase Generation it is.
```
echo 'PYTHONPATH=src python src/xphrase/main.py "$@"' > xphrase.sh
chmod +x xphrase.sh
./xphrase.sh --version
```

## 🧪 Development Version Installation (Test PyPI)

To install the development version from Test PyPI on Kali Linux, execute the following commands step-by-step:

```bash
python3 -m venv venv-testpypi
source venv-testpypi/bin/activate
python -m ensurepip --upgrade
pip install --upgrade pip
pip install -i https://test.pypi.org/simple/ --trusted-host test.pypi.org xphrase
pip list
```

## 🛠️ After installation, navigate to the directory where the XPhrase Generation repository folder was installed, then choose one of the following options to generate the phrases:
### 🧪 Mode './run.py'.  Apply the script below before activating the './run.py' mode to generate the phrases. Do this only on the first installation; after installation, navigate to the directory and generate the phrase using the function.:
```
cat > run.py << 'EOF'
#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from xphrase.main import main
if __name__ == '__main__':
    main()
EOF
chmod +x run.py
```

#### 📏✨ The parameter generates a single sentence with 8 words.
```
./run.py
```

#### 5️⃣🔟 The parameter should be between 5 and 10 words long.
```
./run.py --count 9
```

#### ➖➕ Defines the minimum and maximum number of words to be generated in the sentence. --min and --max must be between 3-21 and min <= max.
```
./run.py --min 5 --max 21
```

#### 📋🔘 Interactive menu - generates unique and multiple phrases.
```
./run.py --interactive
```

#### 📦✨ Show which version of XPhrase Generation it is.
```
./run.py --version
```

### 🎮 Description of the interactive mode
#### XPhrase Generation - Expressive phrase generator  
==================================================

**Options:**

1. **Generate single phrase**  
   - Asks: "generate between 3-21 words?"  
   - Generates one phrase with the specified word count (3-21 words)

2. **Generate multiple phrases**  
   - First asks: "generate between 3-21 words?" (words per phrase)  
   - Then asks: "generate between 5-10 phrases?" (number of phrases)  
   - Generates multiple phrases with consistent word count

3. **Exit**  
   - Closes the phrase generator

---

# 📬 Feedback
Help us improve by reporting issues using our [issue template](https://github.com/gerivanc/xphrase/blob/main/.github/ISSUE_TEMPLATE/issue_template.md).

Thank you for supporting **XPhrase Generation**! 🚀🔑
---

#### Copyright © 2025 Gerivan Costa dos Santos
