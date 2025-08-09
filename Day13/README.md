
# Coffee Machine Project

This is a Python-based Coffee Machine simulation program where users can order one of three types of coffee (Espresso, Latte, and Cappuccino). The program interacts with the user, processes the order, checks if sufficient resources are available, and accepts payment. It also allows the user to view the available resources and the amount of money in the machine.

## Features
- Users can order one of the following types of coffee:
  - Espresso
  - Latte
  - Cappuccino
- Payment is accepted in coins (pennies, nickels, dimes, and quarters).
- The program checks if there are sufficient resources (water, coffee, and milk) for each order.
- It calculates the price based on the selected coffee and processes payments.
- Users can view the available resources and total money in the machine by typing "report".
- The program can be turned off by typing "off".

## Requirements
- Python 3.x
- `art` module for logos and messages (can be installed via `pip install art`)

## How It Works
1. **User Input:** The user is prompted to select a type of coffee (Espresso, Latte, Cappuccino) or request a report of available resources and money.
2. **Resource Check:** The program verifies if enough water, coffee, and milk are available for the selected coffee.
3. **Payment:** The user is asked to input the number of coins they wish to use. The total is then calculated and compared with the price of the selected coffee.
4. **Order Processing:** If the payment is sufficient, the coffee is dispensed and the resources are updated. If not, the user is informed that their payment is insufficient.
5. **Reports:** Users can type `report` to check the remaining resources and the total money in the machine.
6. **Shutdown:** Typing `off` will turn off the machine and display a thank you message.

## Code Overview
- The code defines resources (water, milk, coffee) and the prices of three coffee types.
- The `get_payment()` function handles user input for coin payments and calculates the total amount.
- A `while` loop runs continuously until the machine is turned off, allowing the user to make multiple coffee orders.

## How to Run
1. Install the required module:
    ```bash
    pip install art
    ```
2. Run the Python script:
    ```bash
    python coffee_machine.py
    ```

3. Follow the prompts to select a coffee type, make a payment, and view resources.

## Sample Output
```
Welcome to the Coffee Machine!

What would you like? (espresso/latte/cappuccino): espresso
How much penny? : 5
How much nickel? : 2
How much dime? : 1
How much quarter? : 3
The price espresso is $1.50 and your money is $1.71. Your change is $0.21.
Here is your espresso, Enjoy!

What would you like? (espresso/latte/cappuccino): report
Water : 250
Milk : 200
Coffee : 82
Money : $1.50

What would you like? (espresso/latte/cappuccino): off
Thank you for using the Coffee Machine!
```

## Authors
- This project was created as a simulation for a simple coffee machine.

## License
This project is open source and available under the MIT License.
