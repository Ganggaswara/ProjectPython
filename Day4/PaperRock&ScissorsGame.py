import random

user_choice = input(
    "What do u choose? Type Rock, Paper, or Scissors\n").lower()
asciiart = [''' 
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
            ''',
            '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
            ''',
            '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
            ''']


if user_choice == "paper":
    print(asciiart[0])
    print("Computer choose :")
    computer = random.choice(asciiart)
    print(computer)
    if computer == asciiart[0]:
        print("We Draw")
    elif computer == asciiart[1]:
        print("You Win")
    elif computer == asciiart[2]:
        print("Computer Win")
    else:
        print("you noob")
elif user_choice == "rock":
    print(asciiart[1])
    print("Computer choose :")
    computer = random.choice(asciiart)
    print(computer)
    if computer == asciiart[0]:
        print("Computer Win")
    elif computer == asciiart[1]:
        print("We Draw")
    elif computer == asciiart[2]:
        print("You Win")
    else:
        print("Only choose Rock, Paper, and Scissors. dumbass!")
elif user_choice == "scissors":
    print(asciiart[2])
    print("Computer choose :")
    computer = random.choice(asciiart)
    print(computer)
    if computer == asciiart[0]:
        print("You Win")
    elif computer == asciiart[1]:
        print("Computer Win")
    elif computer == asciiart[2]:
        print("We Draw")
    else:
        print("Only choose Rock, Paper, and Scissors. dumbass!")
else:
    print("Only choose Rock, Paper, and Scissors. dumbass!")
