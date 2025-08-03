import random


def play_game():
    num = list(range(1, 101))

    print("Welcome to the Number Guessing Game! ")
    print("I'm thinking of a number between 1 - 100.")
    level_game = input("Choose a difficulty, Type 'easy' or 'hard : ").lower()
    choosen_num = random.choice(num)

    if level_game == "hard":
        attempts = 5
    elif level_game == "easy":
        attempts = 10
    else:
        print("Pick only 'easy' or 'hard'.")
        return

    game_over = False

    while attempts > 0 and not game_over:
        if level_game == 'hard':
            guess = int(input("Make a guess number between 1 - 100 : "))
            if guess > choosen_num:
                attempts -= 1
                if attempts > 0:
                    print("Too High")
                    print(f"You have {attempts} attempts again ")
                if attempts == 0:
                    print("Too High")
                    print("Game Over! You're out of attempts!")
                    print(f"The number was: {choosen_num}")
            elif guess < choosen_num:
                attempts -= 1
                if attempts > 0:
                    print("Too Low")
                    print(f"You have {attempts} attempts again ")
                if attempts == 0:
                    print("Too Low")
                    print("Game Over! You're out of attempts!")
                    print(f"The number was: {choosen_num}")
            elif guess == choosen_num:
                print("You're Right, Congrats!")
                game_over = True

        if level_game == 'easy':
            guess = int(input("Make a guess number between 1 - 100 : "))
            if guess > choosen_num:
                attempts -= 1
                if attempts > 0:
                    print("Too High")
                    print(f"You have {attempts} attempts again ")
                if attempts == 0:
                    print("Too High")
                    print("Game Over! You're out of attempts!")
                    print(f"The number was: {choosen_num}")
            elif guess < choosen_num:
                attempts -= 1
                if attempts > 0:
                    print("Too Low")
                    print(f"You have {attempts} attempts again ")
                if attempts == 0:
                    print("Too Low")
                    print("Game Over! You're out of attempts!")
                    print(f"The number was: {choosen_num}")
            elif guess == choosen_num:
                print("You're Right, Congrats!")
                game_over = True

# Loop for restart the game
while True:
    play_game()
    should_continue = input(
        "You want to play Number Guessing Game again ? 'y' or 'n' : ").lower()
    if should_continue != 'y':
        print("Thanks for playing! Goodbye!")
        break
