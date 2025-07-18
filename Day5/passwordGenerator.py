# # fruits= ["apple", "peach","pear"]
# # for fruit in fruits :
# #     print(fruit)

# scores_std = [123, 234, 87, 65,98,56, 98, 1900]
# maks = scores_std [0]

# for score in scores_std :
#     if score > maks :
#         maks = score 

# print (maks)


# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0 :
#         print("FizzBuzz")
#     elif num % 3 == 0 :
#         print("Fizz")
#     elif num % 5 == 0 :
#         print("Buzz")
#     else :
#         print(num)

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






