import art

print(art.logo)
print ("~~ Welcome To Secret Auction Program ~~")

offers = {}
def auction() :
    name_bidder = input("What's your name? : ")
    bid = int(input("What's ur bid? : $"))
    others_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    offers[name_bidder] = bid
    while others_bidder == 'yes' :
        print("\n" * 100)
        name_bidder = input("What's your name? : ")
        bid = int(input("What's ur bid? : $"))
        others_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        offers[name_bidder] = bid

auction()
name_winner = max(offers, key=offers.get)
bid_winner = offers[name_winner]
print("\n" * 100)
print(f"Congrats! for {name_winner.upper()} you win the bid, amount of bid is ${bid_winner}.")
