#Caleb Waheed
#2/27/2024
#P2LAB1
#Coding to find out the cost of gas

#Get vaules from user
mpg = float(input("Enter the car's mpg: "))
cost_gas = float(input("How much is a gallon of gas: "))

#Calculate cost of driving 20 miles
miles_20 = (20/mpg) * cost_gas

#Calculate cost of driving 75 miles
miles_75 = (75/mpg) * cost_gas

#Calculate cost of driving 500 miles
miles_500 = (500/mpg) * cost_gas

#Output info to user
print(f"Cost to drive 20 miles is ${miles_20:.2f}")
print(f"Cost to drive 75 miles is ${miles_75:.2f}")
print(f"Cost to drive 500 miles is ${miles_500:.2f}")
