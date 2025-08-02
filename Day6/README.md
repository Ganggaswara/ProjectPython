# 🐍 Hangman Game: Animal Edition

Welcome to the **Hangman Game** — a classic word-guessing game with a Python twist!  
Test your vocabulary and survive by guessing the correct animal name before your 6 lives run out.  
Made with ❤️ by **GanggaSwara**.

---

## 🎯 Game Objective

Guess the **hidden animal name** by entering one letter at a time.  
But be careful! Every incorrect guess costs you a life... and the hangman gets closer to doom.

---

## 🕹️ How to Play

1. Run the script using Python 3.
2. You’ll be given a hidden animal name represented by underscores (`_`).
3. Type a **single letter** to guess.
4. You have **6 lives** in total. Each wrong guess brings the hangman closer to completion.
5. Win by guessing all the correct letters before your lives run out.

---

## 🧠 Features

- 🦁 **Over 60 animal names** randomly selected each game
- 💀 ASCII **Hangman stages** visualized for each wrong guess
- ⛔ Duplicate guess protection
- ✅ Instant win/lose detection
- 🎉 Victory and defeat banners

---

## 🖥️ Sample Gameplay

```bash
Welcome to Hangman Game, Have a good fight !
The game starts with 6 lives which if wrong will be reduced by 1.
Guess the name of the Animal !

Word to guess : _______

guess a letter (with one letter): o
_ o _ _ _ _ _
Your lives : 6

guess a letter (with one letter): z
You guessed "z", that's not in a list of answers, you lost a life!
+---+
|   |
O   |
    |
    |
    |
=========
Your lives : 5
