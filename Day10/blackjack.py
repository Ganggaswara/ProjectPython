import random
from art import logo


def deal_card():
    # Return a random cards from the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    # Take a list of cards and returns the score calculated from the cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "~~ DRAW ~~"
    elif c_score == 0:
        return "You Lose, Opponent has Blackjack !"
    elif u_score == 0:
        return "You Win, You have Blackjack !"
    elif u_score > 21:
        return "You Lose, Score more than 21 !"
    elif c_score > 21:
        return "You Win, Score Computer more than 21 !"
    elif u_score > c_score:
        return "You Win"
    elif c_score > u_score:
        return "You Lose"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards : {user_cards}, current score: {user_score}")
        print(f"Computer's first card is : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deals = input(
                "Type 'y' to get another card, type 'n' to pass : ").lower()
            if user_should_deals == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards is : {user_cards} and the final score is : {user_score}")
    print(
        f"Computer cards is : {computer_cards} and the final score is : {computer_score}")
    print(compare(user_score, computer_score))
    should_continue = input(
        "Do you want to play a game of Blackjack ? Type 'y' if yes and 'n' if no : ").lower()
    if should_continue == 'y':
        print("\n" * 20)
        play_game()


# Mulai permainan
play_game()
