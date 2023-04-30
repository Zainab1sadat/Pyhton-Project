# Name: Zainab Sadat
# Description: Write a program that allows the user to
# play a game using a virtual 20-sided die.
# The naming convention of dice is a D followed by the number of sides.
# The most common dice are 6-sided: D6.
# In this program, you will be rolling a virtual 20-sided die, called a D20!
import random
score = 0

for number in range(5):
    userInput = int(input("Enter a number (1-5)"))
    while userInput < 1 or userInput > 5:
        userInput = int(input("Enter a number (1-5)"))

    print("you select case:", userInput)
    print("rol these numbers")

    if userInput == 1:
        for num in range(2, 21, 2):
            print(num, end=" ")
        print("\n")
    if userInput == 2:
        for num in range(1, 21, 2):
            print(num, end=" ")
        print("\n")
    if userInput == 3:
        for num in range(5, 11):
            print(num, end=" ")
        print("\n")
    if userInput == 4:
        for num in range(10, 21, 2):
            print(num, end=" ")
        print("\n")
    if userInput == 5:
        for num in range(3, 21, 3):
            print(num, end=" ")
        print("\n")
    userRoll = random.randrange(1, 21)
    print("you roll:", userRoll)

    win = False
    if userInput == 1:
        if userRoll % 2 == 0:
            win = True
    if userInput == 2:
        if userRoll % 2 != 0:
            win = True
    if userInput == 3:
        if userRoll > 5 and userInput < 10:
            win = True
    if userInput == 4:
        if userRoll > 10 and userInput < 20 and userInput % 2 == 0:
            win = True
    if userInput == 5:
        if userRoll % 3 == 0:
            win = True
    if win:
        score += 50
        print("you win 50 points")
    else:
        print("you didn't win")
print("your  total score is:", score)
