print("Welcome to the tip Calculator!")

# variabel
bill = float(input("What was the total bill? $ "))
tip = float(input("What tip do you like want to give? 10, 12, 20? "))
people = float(input("how many people to split bill? "))
result = round(bill * (tip / 100 + 1) / people, 2)
# output
print(f"Total semua orang akan bayar sebnanyak ${result}")
