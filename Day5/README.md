# 🔐 PyPassword Generator

Welcome to **PyPassword Generator**, a simple yet powerful Python tool to generate secure and randomized passwords — perfect for your apps, accounts, or top-secret vaults! 🧠💣

---

## 🎯 About the Project

This script allows users to generate **randomized passwords** consisting of:
- ✅ Letters (uppercase & lowercase)
- ✅ Numbers (0–9)
- ✅ Symbols (`@`, `#`, `$`, etc.)

⚙️ Users can customize **how many characters** they want — and get a **shuffled result** that’s hard to crack.

---

## 📦 Features

- Prompt-based interface
- Randomly selects from **letters, numbers, and symbols**
- Uses `random.choice()` and `random.sample()` for extra randomness
- Lightweight: no external libraries required

---

## 💻 How It Works

1. User is asked how many characters they want in their password.
2. Script randomly pulls from:
   - `letters` (A–Z, a–z)
   - `numbers` (0–9)
   - `symbols` (!, @, #, etc.)
3. The selected characters are shuffled for better randomness.
4. Final password is printed.

---

## 🚀 Sample Output

```bash
Welcome to the PyPassword Generator!
How many letters would u like in ur password?
> 12

Your Generate Password is :
7X(fMi%Yb1&J
