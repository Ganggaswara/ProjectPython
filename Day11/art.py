import random

num = list(range(1, 101))

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 - 100.")
level_game = input("Choose a dificulty. Type 'easy' or 'hard' : ").lower()
choosen_num = random.choice(num)
attempts = [10, 5]

while level_game == 'hard' :
    attempts = attempts[1]
    guess = int(input("Make a guess number between 1 - 100 : "))
    if guess < choosen_num :
        print("Too Low, guess again !")
        guess
    if guess > choosen_num :
        print("Too High, guess again!")
        guess
    if guess == choosen_num :
        print("You are correct, Congrats!")
        break

