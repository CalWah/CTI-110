#Caleb Waheed
#3/26/2024
#P4LAB2
#Using the range function

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

#While loop- as long as num1 is smaller than num2, increase by 5 each time

while num1 > num2:  #Bad
    print("First number must be smaller")
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
#Code will happen ONLY when the loop breaks
print("You did it right!")
