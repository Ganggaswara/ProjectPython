from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffemaker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

machine_on = True

while machine_on:
    options = menu.get_items()
    choice = input(
        "What would u like some coffee ? (espresso/latte/cappucino) : ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffemaker.report()
        money_machine.report()
    else :
        drink = menu.find_drink(choice)
        if coffemaker.is_resource_sufficient(drink) :
            if money_machine.make_payment(drink) :
                coffemaker.make_coffee(drink)

        
