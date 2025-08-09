from art import logo
from data_coffee import espresso, latte, cappucino
from art import thanks


water = 300
milk = 200
coffee = 100

penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

price_espresso = 1.50
price_latte = 2.50
price_cappucino = 3.00

machine_money = 0


def get_payment():
    """Get payment from user and return total amount"""
    payment_penny = int(input("How much penny ? : "))
    payment_nickel = int(input("How much nickel ? : "))
    payment_dime = int(input("How much dime ? : "))
    payment_quarter = int(input("How much quarter ? : "))

    total = (payment_penny * penny +
             payment_nickel * nickel +
             payment_dime * dime +
             payment_quarter * quarter)
    return float(total)


print(logo)

machine_on = True
while machine_on:
    # User input some coffee
    choice = input(
        "What would u like? (espresso/latte/cappucino) :  ").lower()
    if choice == "espresso":
        # Check resources first
        if water < 50:
            print("Sorry there is not enough water")
        elif coffee < 18:
            print("Sorry there is not enough coffee")
        else:
            # Resources available, proceed with payment
            money = get_payment()
            pay = money - price_espresso

            if pay < 0:
                print(
                    f"The price espresso is ${price_espresso:.2f} and your money is ${money:.2f} not enough to pay, Money Refunded")
            elif pay == 0:
                print(
                    f"Thank you! Exact payment of ${price_espresso:.2f} received.")
                machine_money += price_espresso
                water -= 50
                coffee -= 18
                print("Here is your espresso, Enjoy!")
            else:  # pay > 0
                print(
                    f"The price espresso is ${price_espresso:.2f} and your money is ${money:.2f}. Your change is ${pay:.2f}.")
                machine_money += price_espresso
                water -= 50
                coffee -= 18
                print("Here is your espresso, Enjoy!")

    if choice == "latte":
        # Check resources first
        if water < 50:
            print("Sorry there is not enough water.")
        elif coffee < 18:
            print("Sorry there is not enough coffee.")
        elif milk < 150:
            print("Sorry there is not enough milk.")
        else:
            # Resources available, proceed with payment
            money = get_payment()
            pay = money - price_latte

            if pay < 0:
                print(
                    f"The price latte is ${price_latte:.2f} and your money is ${money:.2f} not enough to pay, Money Refunded")
            elif pay == 0:
                print(
                    f"Thank you! Exact payment of ${price_latte:.2f} received.")
                machine_money += price_latte
                water -= 50
                coffee -= 18
                milk -= 150
                print("Here is your latte, Enjoy!")
            else:  # pay > 0
                print(
                    f"The price latte is ${price_latte:.2f} and your money is ${money:.2f}. Your change is ${pay:.2f}.")
                machine_money += price_latte
                water -= 50
                coffee -= 18
                milk -= 150
                print("Here is your latte, Enjoy!")

    if choice == "cappucino":
        # Check resources first
        if water < 50:
            print("Sorry there is not enough water.")
        elif coffee < 18:
            print("Sorry there is not enough coffee.")
        elif milk < 100:
            print("Sorry there is not enough milk.")
        else:
            # Resources available, proceed with payment
            money = get_payment()
            pay = money - price_cappucino

            if pay < 0:
                print(
                    f"The price cappucino is ${price_cappucino:.2f} and your money is ${money:.2f} not enough to pay, Money Refunded")
            elif pay == 0:
                print(
                    f"Thank you! Exact payment of ${price_cappucino:.2f} received.")
                machine_money += price_cappucino
                water -= 50
                coffee -= 18
                milk -= 100
                print("Here is your cappucino, Enjoy!")
            else:  # pay > 0
                print(
                    f"The price cappucino is ${price_cappucino:.2f} and your money is ${money:.2f}. Your change is ${pay:.2f}.")
                machine_money += price_cappucino
                water -= 50
                coffee -= 18
                milk -= 100
                print("Here is your cappucino, Enjoy!")
    # Report choice
    elif choice == 'report':
        print(f'Water : {water}')
        print(f'Milk : {milk}')
        print(f'Coffee : {coffee}')
        print(f"Money : ${machine_money:.2f}")
    # Turn off the machine
    elif choice == "off":
        print(thanks)
        machine_on = False
    elif choice not in ["espresso", "latte", "cappucino", "report", "off"]:
        print("Invalid choice. Please select espresso/latte/cappucino")
