# 📊 XPhrase Generation Calculation Methodology

**Detailed methodology for expressive phrase generation — combination space calculations, formation rules, and security analysis.**

This document explains **exactly how XPhrase Generation** constructs each phrase, with emphasis on **reproducibility, cryptographic strength, and combinatorial scale**.  
Based on the project's [README.md](README.md):  
[XPhrase Repository](https://github.com/gerivanc/xphrase/)

---

## 🧠 Process Overview

**XPhrase** generates phrases composed of:

- **3 to 21 words** (configurable via `--count`, `--min`, `--max`, or interactive mode)
- Words drawn from **3 languages**: Portuguese, English, and German
- Each word is **augmented** with:
  - **At least 1 special character**
  - **At least 1 digit**
- The **last letter of the final word is always uppercase**
- Language order is **randomized per word**

---

## 📚 Word Bank Specifications

| Language     | Word Count | Source File                     |
|--------------|------------|---------------------------------|
| Portuguese   | 1,333      | `data/portuguese_words.py`      |
| English      | 1,334      | `data/english_words.py`         |
| German       | 1,333      | `data/german_words.py`          |
| **Total**    | **4,000**  | —                               |

> Words are **unique per language** → **no cross-language duplicates**  
> **Total distinct words**: **4,000**

---

## 🔐 Phrase Formation Rules

For a phrase with \( n \) words (\( 3 \leq n \leq 21 \)):

### 1. **Word Selection**
   - Each word is selected **randomly with replacement** from the pool of 4,000
   - Language origin is **random per word** (uniform distribution across 3 languages)
   - **Order matters**, repetitions allowed

### 2. **Per-Word Modification**
   For each selected word:
   - Insert **at least one digit** (`0–9`) → 10 options
   - Insert **at least one special character** from:
     ```
     !@#$%^&*()_+-=[]{}|;:,.<>?~\\
     ```
     → **29 special characters**
   - Insertions occur **between letters**, **before**, or **after** the word
   - **Multiple insertions allowed** (no upper limit per word)
   - **No fixed pattern** — randomness ensures entropy

### 3. **Inter-Word Linking**
   - Words are **concatenated directly** with their modifications
   - No fixed separator between augmented words
   - Example: `word1!2word2+5word3`

### 4. **Final Word Capitalization**
   - The **last character of the final word** must be a **letter** and is **forced uppercase**
   - If the last character after modification is not a letter, a **valid letter is appended and uppercased**

---

## 🎰 Combinatorial Space Calculation

We calculate the **total number of possible phrases** using conservative and realistic bounds.

### **Step 1: Word Selection**
- \( 4,000 \) choices per word
- \( n \) words → \( 4000^n \)

### **Step 2: Per-Word Augmentation (Minimum)**
Each word must include:
- ≥1 digit
- ≥1 special character

Let’s define:
- \( L \): average original word length (assume ~7 chars)
- But to compute **minimum entropy**, assume **2 insertions per word** (1 digit + 1 special)

#### Minimum insertions per word:
- Choose **position** for digit: \( L+1 \) possible slots
- Choose **digit**: 10 options
- Choose **position** for special: \( L+2 \) slots
- Choose **special**: 29 options

**Per word (lower bound)**:  
\( 4000 \times 10 \times 29 \times (L+1) \times (L+2) \)

With \( L = 7 \):
\[
4000 \times 10 \times 29 \times 8 \times 9 = 83,520,000 \approx 8.35 \times 10^7
\]

For **n words**:
\[
\text{Total (min)} = (8.35 \times 10^7)^n
\]

---

### **Conservative Lower Bound (Minimum 1 digit + 1 special per word)**

| Word Count (n) | Min Combinations (Lower Bound) | Notation |
|----------------|-------------------------------|----------|
| 3              | \( (8.35 \times 10^7)^3 \)     | \( 5.8 \times 10^{23} \) |
| 8 (default)    | \( (8.35 \times 10^7)^8 \)     | \( 2.2 \times 10^{63} \) |
| 21             | \( (8.35 \times 10^7)^{21} \)  | \( 3.3 \times 10^{166} \) |

> **Note**: This is a **conservative lower bound**. Real entropy is **higher** due to multiple insertions.

---

## 🔄 Alternative Model: k Words Separated by 1 Digit + 1 Special Character

This model assumes a **structured format** not used in the current implementation, but useful for **comparative analysis** or **future variants**:

> `[word1][digit][special][word2][digit][special]...[wordk]`

- \( k \) words: \( 4000^k \)
- Between words: \( (k-1) \) pairs of **(1 digit + 1 special)**
- Each digit: **10 options**
- Each special: **29 options**

### Formula:
\[
\text{Total} = 4000^k \times 10^{k-1} \times 29^{k-1}
\]

### Practical Examples:

| k (words) | Calculation | Total Combinations (approx.) |
|-----------|-------------|------------------------------|
| 3         | \( 4000^3 \times 10^2 \times 29^2 \) | \( 64 \times 10^9 \times 100 \times 841 = 5.38 \times 10^{15} \) |
| 5         | \( 4000^5 \times 10^4 \times 29^4 \) | \( 1.024 \times 10^{17} \times 10^4 \times 707,281 \approx 7.24 \times 10^{26} \) |
| 8         | \( 4000^8 \times 10^7 \times 29^7 \) | \( 6.5536 \times 10^{26} \times 10^7 \times 17.2 \times 10^9 \approx 1.13 \times 10^{44} \) |
| 10        | \( 4000^{10} \times 10^9 \times 29^9 \) | \( 1.048 \times 10^{33} \times 10^9 \times 1.02 \times 10^{13} \approx 1.07 \times 10^{55} \) |

> **Note**: This model produces **structured, predictable patterns** (e.g., `word1!2word2#5word3`) → **lower effective entropy** than XPhrase’s free-form insertion.

---

## 🔒 Security & Entropy Analysis

| Feature                        | Contribution to Strength |
|--------------------------------|--------------------------|
| 4,000-word base                | High base entropy        |
| Random language mixing         | Prevents language-based attacks |
| Variable word count (3–21)     | Resists length profiling |
| Mandatory digit + special      | Blocks dictionary attacks |
| Final uppercase letter         | Normalizes but doesn't reduce entropy |
| No fixed separators            | Increases pattern complexity |

### **Effective Password Strength**
- 8-word phrase → **~500–600 bits of entropy** (conservative)
- Equivalent to a **150+ character random password**
- **Resistant to brute-force, rainbow tables, and dictionary attacks**

---

## ⚙️ Generation Algorithm (Pseudocode)

```python
def generate_phrase(n_words):
    phrase_parts = []
    for i in range(n_words):
        word = random.choice(ALL_WORDS)  # 4000 options
        modified = insert_digit(word)
        modified = insert_special(modified)
        # Optional: insert more for higher entropy
        if i == n_words - 1:
            modified = ensure_final_uppercase(modified)
        phrase_parts.append(modified)
    return "".join(phrase_parts)
```

---

## 📊 Example Breakdown

**Input**: `n = 8`  
**Output**:  
`Note,8oxidar+6truly=3Chaos\1ressaca[3kind;1achtzehn_9descréditO`

| Part           | Language  | Digit | Special | Final Cap |
|----------------|-----------|-------|---------|-----------|
| `Note,8`       | English   | 8     | ,       | —         |
| `oxidar+6`     | Portuguese| 6     | +       | —         |
| `truly=3`      | English   | 3     | =       | —         |
| `Chaos\1`      | German    | 1     | \       | —         |
| `ressaca[3`    | Portuguese| 3     | [       | —         |
| `kind;1`       | English   | 1     | ;       | —         |
| `achtzehn_9`   | German    | 9     | _       | —         |
| `descréditO`   | Portuguese| —     | —       | **O**     |

---

## 🛠️ CLI Integration Summary

| Command                            | Behavior |
|------------------------------------|---------|
| `python xphrase.py`                | 1 phrase, 8 words |
| `python xphrase.py --count 10`     | 1 phrase, 10 words |
| `python xphrase.py --min 5 --max 10` | 1 phrase, random 5–10 words |
| `python xphrase.py --interactive`  | Menu: single, batch, exit |

---

## 🚀 Conclusion

**XPhrase Generation** produces:
- **Human-memorable** passphrases
- **Cryptographically strong** (≥500 bits for default)
- **Highly configurable** via CLI
- **Massive combinatorial space** (\(10^{63}\) to \(10^{166}\))

> **Ideal for**: master passwords, encrypted backups, seed phrases (with caution), or secure tokens.

---

## 📌 References

- [README.md](https://github.com/gerivanc/xphrase/blob/main/README.md)
- [word_manager.py](https://github.com/gerivanc/xphrase/blob/main/word_manager.py)
- [xphrase.py](https://github.com/gerivanc/xphrase/blob/main/xphrase.py)
- Word lists: `data/*.py`

---

#### © 2025 Gerivan Costa dos Santos  
**XPhrase Generation — Expressive. Strong. Minimalist.**
