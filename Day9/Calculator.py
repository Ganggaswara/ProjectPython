import art

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# main loop
should_continue = True
while should_continue:
    # first input
    print (art.logo)
    first_num = float(input("What's the first number? : "))
    operation_user = input("+  For Add\n-  For Subtract\n*  For Multiply\n/  For Divide\nPick an operation: ")
    if operation_user not in operations :
        print("Only pick valid operation! ("+", "-", "*", "/"")
        continue
    second_num = float(input("What's the next number? : "))
    result = float(operations[operation_user](first_num, second_num))
    print(f"{first_num} {operation_user} {second_num} = {result}")
    restart = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    # next loop
    while restart == "y":
        operation_user = input("+  For Add\n-  For Subtract\n*  For Multiply\n/  For Divide\nPick an operation: ")
        second_num = float(input("What's the next number? : "))
        previous_result = result
        result = float(operations[operation_user](result, second_num))

        print(f"{previous_result} {operation_user} {second_num} = {result}")
        restart = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    if restart == "n":
        exit_choice = input(
            "Type 'exit' to quit the calculator, or press Enter to start a new calculation: ").lower()
        if exit_choice == "exit":
            should_continue = False
        else:
            print("\n" * 100)  # Clear screen
            continue
