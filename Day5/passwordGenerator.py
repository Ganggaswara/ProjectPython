import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

all_char = letters + symbols + numbers

nr_letters = int(input("Welcome to the PyPassword Generator!\nHow many letters would u like in ur password?\n"))
# nr_symbols = int(input("How many symbols would u like?\n"))
# nr_numbers = int(input("How many number would u like?\n"))

password = ""

for _ in range(nr_letters) :
    password += random.choice(all_char)
# for _ in range(nr_symbols) :
#     password += random.choice(symbols)
# for _ in range(nr_numbers) :
#     password += random.choice(numbers)

password_final = "".join(random.sample(password, len(password)))
print(f"Your Generate Password is : \n{password_final}")







