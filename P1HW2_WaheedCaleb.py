#Caleb Waheed
#2/25/2024
#P1HW2
#Adding and subtracting a budget

bug1 = int(input("Enter Budget: "))

Loc1 = input("Enter your travel destination: ")

Gas1 = int(input("How much do you think you will spend on gas? "))

Hotel1 = int(input("Approximately, how much will you need for accmodation/hotel? "))

food1 = int(input("Last, how much do you need for food? "))

print("------------Travel Expenses------------")

print("Location:", Loc1)

print("Initial Buget:", bug1)

print("Fuel:", Gas1)

print("Accomodation:", Hotel1)

print("Food:", food1)

print("Remaining Balance:", bug1, "-", Gas1, "-", Hotel1, "-", food1, "=", bug1 - Gas1 - Hotel1 - food1) 
