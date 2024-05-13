#Caleb Waheed
#3/29/2029
#P4HW1
#Making a code for users to put in their scores

G_L = []

num_g = int(input("How many scores do you want to enter?"))
for item in range(num_g):
    
    score_1 = int(input(f"Enter score #{item+1}: "))


    while score_1 < 0 or score_1 > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score_1 = int(input(f"Enter score #{item+1}: "))
  
    G_L.append(score_1)


print(G_L)
print("------------------Results---------------------")

low = min(G_L)
G_L.remove(low)
print(G_L)
high = max(G_L)
Summary = sum(G_L)
avg = Summary/len(G_L)

if avg >= 90:
 print("Your grade is: A")
elif avg >= 80:
 print("Your grade is: B")
elif avg >= 70:
 print("Your grade is: C")
elif avg >= 60:
 print("Your grade is: D")
else:
 print("Your grade is: F") 
