#Caleb Waheed
#4/27/2024
#P5HW
#Code a Math Quiz

import random


def add_num():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f"{num1} + {num2}")
    ans = num1 + num2
    Guess = int(input("Enter answer"))
    Num_guess = 1
    while(ans != Guess):
        if (Guess > ans):
            print("Soory, guess is too high")
        if (Guess < ans):
            print("Soory, guess is too low")
        Guess = int(input("Try again"))
        Num_guess += 1
    print("Congratulations!!!! Your answer is correct.")
    print(f"Number of guess: {Num_guess}")

def sub_num():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f"{num1} - {num2}")
    ans = num1 - num2
    Guess = int(input("Enter answer"))
    Num_guess = 1
    while(ans != Guess):
        if (Guess > ans):
            print("Soory, guess is too high")
        if (Guess < ans):
            print("Soory, guess is too low")
        Guess = int(input("Try again"))
        Num_guess += 1
    print("Congratulations!!!! Your answer is correct.")
    print(f"Number of guess: {Num_guess}")
        
def ext():
    print("Thank you for playing...")
    print("Bye!!!")
    


def main(): 
    print("MAIN MENU")
    print("----------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

    option = input("Please choose one of the menu options:")
    while option != "3":
        
        if option == "1":
            add_num()
        if option == "2":
            sub_num()
        option = input("Please choose one of the menu options:")
    ext()


#Call the main function
main()
