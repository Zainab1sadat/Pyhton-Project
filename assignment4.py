# Assignment 3
# Name: Zainab Sadat
# Description:Write a Python program that uses lists, string processing, and loops.
import random

# Lists of word
wordList = ["phyton", "apple" , "key", "notebook"]
# Lists of Jumbled word
jumbledList = ["pothny", "pepla", "eyk", "okontboe"]
# Lists of Hints
hint = ["snake", "fruit", "you can open Lock", " you can write in it"]
# number of words in list
print("the number of words is ", len(wordList))
index = random.randrange(0,4)
# randomly pick a jumbled word using index
randomJum = jumbledList[index]
# randomly pick a Hint using index
randomHint = hint[index]
# randomly pick a  word using index
wordLists = wordList[index]
# printing random Jumbled word
print("the jumbled word is:", randomJum)
# printing number of letters
print("the number of letter is:", len(randomJum))
# create a Var for our guesses assign to 1
guess = 1
# take from user a guess
userGuess = input("Enter your guess!    ")
# make Bold
print("your guess is " + '\033[1m' + userGuess + '\033[0m')
# using while loop until the guess doesn't equal to word to get hint
while userGuess != wordLists:
    print("your guess is incorrect :( ")
    # get hint bold
    hint = input("Do you want a hint? (y , n) : \u001b[1m ")
    print('\u001b[0m', end='')
    print('Your input is:', hint)

    print("the jumbled word is:", randomJum)
    # using branching if user enter yes or No for hint
    if hint.lower().strip() == "y" or hint.lower().strip() == "Y":
        print("hint is:", "\'"+randomHint+"\'", sep="")

    userGuess = input("Enter your guess!   \u001b[0m").lower().strip()
    print('\u001b[0m', end='')

else:
    print("your guess is incorrect :( ")
    print("the jumbled word is:", randomJum)
    # increasing our guess by 1 and assign it again to our Var that is guess
    guess += 1
    # print if the guess id correct
print("your guess", userGuess, "is correct")
# print the number of total guesses
print("the numbers of your guesses is:", guess)


