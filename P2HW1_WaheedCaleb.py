#Caleb Waheed
#2/29/2024
#P2HW1
#Coding for calculating travel expenses

print("This program calculates and displays travel expenses")

bug1 = float(input("Enter Budget: "))

Loc1 = input("Enter your travel destination: ")

Gas1 = float(input("How much do you think you will spend on gas? "))

Hotel1 = float(input("Approximately, how much will you need for accmodation/hotel? "))

food1 = float(input("Last, how much do you need for food? "))

print("------------Travel Expenses------------")

print("Location:", Loc1)

print(f"Initial Buget: ${bug1:.2f}")

print(f"Fuel: ${Gas1:.2f}")

print(f"Accomodation: ${Hotel1:.2f}")

print(f"Food: ${food1:.2f}")

print("--------------------------------------")

print(f"Remaining Balance: ${(bug1 - Gas1 - Hotel1 - food1):.2f}")
