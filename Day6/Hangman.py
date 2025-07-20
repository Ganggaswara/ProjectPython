import random

hangman = ['''
+---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
           ''']
hangman_title = ('''
 _   _    _    _   _  ____ __  __    _    _   _    ____    _    __  __ _____ 
| | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |  / ___|  / \  |  \/  | ____|
| |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| | | |  _  / _ \ | |\/| |  _|  
|  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  | | |_| |/ ___ \| |  | | |___ 
|_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_|  \____/_/   \_\_|  |_|_____|
                 ''')
print("\nMade by GanggaSwara")
print(hangman_title)

print("Welcome to Hangman Game, Have a good fight !")
print("The game starts with 6 lives which if wrong will be reduced by 1.\n")
print("Guess the name of the Animal !") 
 
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
choice = random.choice(word_list)


placeholder = ""
for p in range(len(choice)):
    placeholder += "_"
print(f"Word to guess : {placeholder}\n")

game_over = False
list_answer = []
lives = 6 

while not game_over :
    guess = input("guess a letter (with one letter): ").lower()

    if guess in list_answer:
        print(f"You already guesssed \"{guess}\", Try Again!")
    # elif guess not in choice :
    #     print(f"You guessed \"{guess}\" , that's not in a list of answers, you lost a life! ")

    display = ""
    for c in choice:
        if c == guess :
            display += c
            list_answer.append(guess)
        elif c in list_answer :
            display += c 
        else:
            display += "_"

    if guess in choice and lives == 6:
        print(hangman[0])

    if guess not in choice :
        print(f"You guessed \"{guess}\" , that's not in a list of answers, you lost a life! ")
        lives -= 1
        if lives == 5 :
            print(hangman[1])
        elif lives == 4 :
            print(hangman[2])
        elif lives == 3 :
            print(hangman[3])
        elif lives == 2 :
            print(hangman[4])
        elif lives == 1 :
            print(hangman[5])
        else :
            print(hangman[6])

    print(display)
    print(f"Your lives : {lives}")

    if "_" not in display :
        game_over = True
        print('''
__   __           __        ___         _ 
\ \ / /__  _   _  \ \      / (_)_ __   | |
 \ V / _ \| | | |  \ \ /\ / /| | '_ \  | |
  | | (_) | |_| |   \ V  V / | | | | | |_|
  |_|\___/ \__,_|    \_/\_/  |_|_| |_| (_)
              
              ''')
        print(f"Good!! The answer is : \"{choice}\"")
        break
    if lives == 0 :
        print('''         
__   __            _                     _ 
\ \ / /__  _   _  | |    ___  ___  ___  | |
 \ V / _ \| | | | | |   / _ \/ __|/ _ \ | |
  | | (_) | |_| | | |__| (_) \__ \  __/ |_|
  |_|\___/ \__,_| |_____\___/|___/\___| (_) 
              
              ''')
        print(f"The answer is : \"{choice}\"")
        break
