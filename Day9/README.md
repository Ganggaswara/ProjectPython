# 🧮 Python Interactive Calculator — Command Line Edition

Welcome to the **Python Calculator Program**, an interactive CLI-based calculator that performs basic arithmetic operations with an intuitive flow and clean logic. Powered by custom functions and user-friendly looping, it's perfect for learners and hobbyists alike!

---

## ✨ Features

- ➕ Addition  
- ➖ Subtraction  
- ✖️ Multiplication  
- ➗ Division  
- 🔁 Chain operations using the current result  
- 🔄 Option to reset or exit anytime  
- 🖼️ ASCII art title using the `art` module

---

## 🚀 How to Run

1. **Install the required module (if not installed):**
```bash
pip install art
```

2. **Run the program:**
```bash
python calculator.py
```

---

## 🧠 How It Works

- You enter the **first number**.
- Then choose an operation (`+`, `-`, `*`, `/`).
- Enter the **second number**, and the result is displayed.
- You can continue calculating using the **current result**, or **restart** the calculation.
- You can exit anytime by typing `"exit"` when prompted.

---

## 💻 Sample Interaction

```text
What's the first number? : 12
+  For Add
-  For Subtract
*  For Multiply
/  For Divide
Pick an operation: +
What's the next number? : 8
12.0 + 8.0 = 20.0

Type 'y' to continue calculating with 20.0, or type 'n' to start a new calculation: y
+  For Add
-  For Subtract
*  For Multiply
/  For Divide
Pick an operation: *
What's the next number? : 2
20.0 * 2.0 = 40.0

Type 'y' to continue calculating with 40.0, or type 'n' to start a new calculation: n
Type 'exit' to quit the calculator, or press Enter to start a new calculation:
```

---

## 🧪 Concepts Demonstrated

- Dictionary mapping of operators to functions
- Function-based operation definitions
- Input validation for operators
- Looping structure for continued usage
- ASCII art with the `art` module
- Screen-clearing simulation using `print("\n" * 100)`

---

## ✅ To-Do Suggestions

- Add support for **exponentiation** and **modulus**
- Support **float precision formatting** for cleaner output
- Implement **error handling** (e.g., division by zero)
- Use `os.system('cls')` or `'clear'` for real screen clearing
- Add **GUI version** with `tkinter` or `PyQt`

---

## 👤 Author

Made with 🧠 by **GanggaSwara**  
Use this project as a base to expand your CLI or GUI calculator experience.

---

Count on it. Calculate with confidence. 💡
