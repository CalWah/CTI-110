#Caleb Waheed
#3/7/2024
#P2HW2
#Write program Pseudocode

nums = []
#print(nums)

num1 = float(input("Enter grade dor Module 1: "))

num2 = float(input("Enter grade dor Module 2: "))

num3 = float(input("Enter grade dor Module 3: "))

num4 = float(input("Enter grade dor Module 4: "))

num5 = float(input("Enter grade dor Module 5: "))

num6 = float(input("Enter grade dor Module 6: "))

nums.append(num1)
nums.append(num2)
nums.append(num3)
nums.append(num4)
nums.append(num5)
nums.append(num6)

print("------------Results-------------")

list_min = min(nums)
print(f"Lowest Grade: {list_min}")

list_max = max(nums)
print(f"Largest Grade: {list_max}")

list_sum = sum(nums)
print(f"Sum of Grades: {list_sum}")

list_avg = sum(nums)/len(nums)
print(f"Average: {list_avg:.2f}")
print("-------------------------------------------------")
