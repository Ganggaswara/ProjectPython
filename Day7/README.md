# 🔐 Caesar Cipher — Python Encryption & Decryption Tool

Welcome to the **Caesar Cipher Program** — a classic encryption technique brought to life with Python!  
Easily encode or decode your secret messages using letter shifting logic based on Julius Caesar's original method of cryptography. 🏛️

---

## 🧠 What is Caesar Cipher?

The **Caesar Cipher** is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

For example, with a shift of **3**:

```
Plain Text:  hello
Cipher Text: khoor
```

---

## ✨ Features

- 🔐 Encode & decode messages using a shift-based cipher
- 🔄 Repeat runs without restarting the program
- 🧮 Custom shift number input
- 🔤 Keeps symbols and spaces as-is
- 🖼️ ASCII art title via the `art` library

---

## 🚀 Getting Started

### 1. Clone the repository or copy the script.
### 2. Install required package:

```bash
pip install art
```

### 3. Run the script:

```bash
python caesar_cipher.py
```

---

## 🖥️ Sample Usage

```text
~~~ Welcome To Caisar Cipher Program ~~~

Type 'encode' to encrypt text, type 'decode' to decrypt text : 
> encode

Type your message :
> meet me at the bridge

Type the shift number:
> 5

Your encrypted result is : rjjy rj fy ymj gwnijl
```

---

## 🛠️ How It Works

- Alphabet is indexed 0–25
- Input characters are converted to a list
- Characters not in the alphabet are preserved
- Uses modulo arithmetic to wrap around (e.g., `z` → `c`)
- Built-in loop for program re-run via user input

---

## 📚 Python Concepts Demonstrated

- Functions and parameters
- List and string manipulation
- Control flow with `if`, `elif`, `else`
- ASCII art integration using third-party module
- Modular arithmetic

---

## 🧪 To-Do Ideas

- [ ] Add support for uppercase detection and retention
- [ ] Implement auto-detect language or auto-decrypt
- [ ] Build GUI with `tkinter` or web version using Flask
- [ ] Save encrypted messages to a file

---

## 👤 Author

Made with 💡 and 🧠 by **GanggaSwara**  
For educational and entertainment purposes only.

---

Enjoy encrypting like it’s Ancient Rome! 🏛️
