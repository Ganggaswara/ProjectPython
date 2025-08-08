
# 🎮 Higher Lower Game

## 📜 Description
Welcome to the **Higher Lower Game**! This is a simple yet engaging game where you compare social media profiles to guess which one has more followers. The game continues until you make an incorrect guess, and your score increases with each correct guess. Can you get the highest score?

## 📊 How to Play
1. **Guess** which profile has more followers — either **A** or **B**.
2. If your guess is correct, you earn **1 point**.
3. If your guess is incorrect, the game ends and your **final score** is displayed.
4. The game keeps selecting new profiles randomly, making each round unique!

## 🔧 Requirements

Ensure you have Python installed and the necessary libraries to run the game:

- **`art`**: For generating ASCII art logos.
- **`random`**: To randomly select profiles.
- **`game_data`**: Contains data for the social media profiles (names, follower counts, descriptions).

### Install required libraries:

```bash
pip install art
```

## 🖥️ Project Files
- **`game_data.py`**: Contains the profile data with names, descriptions, countries, and follower counts. This data is used to generate the game.
- **`logo.py`**: Contains the ASCII art logo for the game.
- **`main.py`**: The main script where the game logic runs and the game is played.

## 📑 Code Breakdown

### 1. **Random Profile Selection**  
   Two profiles are randomly selected from the dataset using `random.choice()`. The game makes sure not to select the same profile twice in a round.

### 2. **Displaying the Game**  
   The profile details (name, description, and country) are displayed along with an ASCII logo. The user has to choose which of the two profiles has **more followers**.

### 3. **Game Flow**
   - If the user inputs **'A'**, the game checks if the first profile has more followers than the second. If correct, the score increases by 1.
   - If the user inputs **'B'**, the game checks if the second profile has more followers than the first. If correct, the score increases by 1.
   - If the guess is incorrect, the game ends, and the user's final score is shown.

### 4. **Score Tracking**  
   The player's score is updated after each correct guess and is shown after every round. The game ends if the player guesses incorrectly.

## 💻 How to Start

1. Clone or download this repository.
2. Install the required dependencies by running:

```bash
pip install art
```

3. Run the **`main.py`** script to start the game:

```bash
python main.py
```

4. Enjoy and try to get the highest score!

## 🎨 Example Gameplay

```text
Welcome to Higher Lower Game, Let's guess which one higher!
Your current score is 2
A : Cristiano Ronaldo, a footballer, from Portugal
VS
B : Selena Gomez, a singer, from USA

Who has more followers? 'A' or 'B' : a
YOU WIN!
Your Score now is : 3
```

---

Feel free to edit the game or add more profiles to the dataset. Have fun and challenge your friends to beat your score! 🎮
