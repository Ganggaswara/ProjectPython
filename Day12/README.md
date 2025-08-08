# Number Guessing Game 🎯

A simple Python terminal game where the player tries to guess a number between 1 and 100. The game offers two difficulty levels — `easy` and `hard` — each providing a limited number of guesses.

## 🧠 How It Works

- The computer randomly selects a number between 1 and 100.
- You choose a difficulty level:
  - **Easy**: 10 attempts
  - **Hard**: 5 attempts
- After each guess, the program tells you whether your guess was too high or too low.
- If you guess the number correctly within the allowed attempts, you win!
- If not, the game ends and reveals the correct number.

## 🚀 How to Run

1. Make sure you have Python installed (version 3.x).
2. Place your `main.py` (containing the code) and `art.py` (containing `logo1`, `logo2`) in the same folder.
3. Run the script:

```bash
python main.py
```

## 📁 File Structure

```
.
├── main.py        # Game logic
├── art.py         # ASCII art for logos
└── README.md      # Project documentation
```

## 🛠 Features

- Replay option after each game
- Clean console at game restart (`print("\n" * 20)`)
- Separated logic for different difficulty levels

## 🖼 Sample ASCII Art

Defined in `art.py`:
```python
logo1 = "..."  # Welcome logo
logo2 = "..."  # Goodbye logo
```

Feel free to customize the art to make the game more fun!

## 📌 License

MIT License — free to use and modify.