import random
from art import logo, vs
from game_data import data

score = 0
game_over = False

while not game_over:
    data1 = random.choice(data)
    data2 = random.choice(data)
    while data2 == data1 :
        data2 = random.choice(data)
    name_1 = data1["name"]
    desc_1 = data1["description"]
    country_1 = data1["country"]

    name_2 = data2["name"]
    desc_2 = data2["description"]
    country_2 = data2["country"]

    value_data1 = data1["follower_count"]
    value_data2 = data2['follower_count']

    print("\n" * 20)
    print(logo)
    print("Welcome to Higher Lower Game, Let's guess which one higher ! ")
    print(f"Your current score is {score}")
    print(f"A : {name_1}, a {desc_1}, from {country_1}")
    print(vs)
    print(f"B : {name_2}, a {desc_2}, from {country_2}")

    ask = input("Who has more followers ? 'A' or 'B' : ").lower()
    if ask == 'a':
        if value_data1 > value_data2:
            score += 1
            print("YOU WIN!")
            print(f"Your Score now is : {score}")
        else:
            print("\n" *20)
            print(logo)
            print(f"YOU LOSE, Final Score is : {score}")
            game_over = True
            break
    if ask == 'b':
        if value_data2 > value_data1:
            score += 1
            print("YOU WIN!")
            print(f"Your Score now is : {score}")
        else:
            print("\n" *20)
            print(logo)
            print(f"YOU LOSE, Final Score is : {score}")
            game_over = True
            break
    else : 
        print("Only choose 'A' or 'B' guys!")
