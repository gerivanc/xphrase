# 🚀 XPHRASE GENERATION

**Expressive phrase generator — strong, modern, and minimalist.**  
Built entirely in Python for CLI environments on Linux and Windows.

---

## 🚨🚧 Upcoming Project Alert 🚧🚨

We are currently undergoing construction, and as with any construction project, things are a bit disorganized at the beginning, but please be patient, the work will be completed soon.

--- 

## 🧠 PROJECT OVERVIEW

**XPhrase Generation** is a multilingual phrase generator designed for command-line interface (CLI) usage.  
It creates expressive, randomized phrases using words from **Portuguese**, **English**, and **German**, interlinked with special characters and digits.

This project is:
- 💯 Written 100% in Python
- 🖥️ CLI-compatible for Linux and Windows
- 🌐 Future-ready for HTML interface integration

---

## 📦 FEATURES

- Generates phrases with **3 to 21 words**
- Words are randomly selected from **Portuguese**, **English**, and **German** word banks
- Each word is **interlinked** with:
  - At least **one special character**: `!@#$%^&*()_+-=[]{}|;:,.<>?~\\`
  - At least **one digit**: `0123456789`
- The **last character of the final word** is always **uppercase**
- Output example:  
  `ice8café*intentos7vermeideN`

---

## 🛠️ REQUIREMENTS

- Python 3.8+
- No external dependencies
- Works on:
  - ✅ Linux (Debian, Ubuntu, Arch, etc.)
  - ✅ Windows (PowerShell, CMD)

---

## 📁 FILE STRUCTURE

```
xphrase/
├── .github/
│   └── workflows/
│       ├── pypi-publish.yml
│       └── python-app.yml
├── pyproject.toml 
├── README.md
├── requirements.txt
├── setup.py
├── xphrase.py
├── word_manager.py
├── data/
		├── __init__.py
		├── german_words.py
		├── portuguese_words.py
		└── english_words.py
```

---

## ⚙️ USAGE

### 🔧 Run from CLI

```bash
python src/xphrase.py
```

Or install as package:

```bash
pip install -e .
xphrase-generate
```

### 🧾 Output Example

```text
dream3vermeide!café9run#intentos2LiebeN
```

---

## 📚 WORD BANK SPECS

- It contains 4,000 specific and unique words, selected from the vocabulary of three different languages.
- This project was created by selecting words to generate sentences in three languages: English, Portuguese, and German.
- All words are stored in separate `.txt` files inside the `data/` folder.
- Words are randomly selected and mixed across languages.

| Language    | Word Count |
|-------------|------------|
| English     | 1,334      |
| Portuguese  | 1,333      |
| German      | 1,333      |

---

## 🔐 GENERATION RULES

- Phrase length: **3 to 21 words**
- Each word must include:
  - **1+ special character**
  - **1+ digit**
- Final word must end with a **capital letter**
- Language order is **randomized**

---

## 🧪 EXAMPLES

```text
run7Liebe!café2dream#vermeide9IntentoN
code3vermeide@ice8Liebe*intentos1caféZ
```

---

## 🧰 FUTURE ROADMAP

- 🌐 HTML interface (web version)
- 📦 Packaging for PyPI
- 🧪 Unit tests and coverage

---

## 🤝 CONTRIBUTING

Contributions are welcome! Please follow the guidelines in [CONTRIBUTING.md](https://github.com/gerivanc/xphrase/blob/main/CONTRIBUTING.md).

---

## 📜 License
This repository is licensed under the [MIT License](https://github.com/gerivanc/xphrase/blob/main/LICENSE.md).

---

## 💬 CONTACT

E-mail: ask@gerivan.me  
Location: Brazil  
Feel free to reach out for collaboration or feedback!

---

#### Copyright © 2025 Gerivan Costa dos Santos
#### XPhrase Generation — Expressive phrases. Strong logic. Minimalist design © 2025
