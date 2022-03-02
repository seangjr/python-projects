import random

#exercise 1 and 2
def countOddEven(firstNumber, secondNumber):

    countOdd = 0
    countEven = 0

    for i in range(firstNumber, secondNumber+1, 7):
        if not i % 2:
            countEven += 1
        else:
            countOdd += 1
    
    print("The number of even numbers is ", countEven)
    print("The number of odd numbers is ", countOdd)

    print("The sum off odd and even numbers are ",countOdd+countEven)

countOddEven(1, 100) #call the function and add the range

#exercise 3 and 4
def moneyStack(x):

    cents = 30
    day = 1

    while day < x:
        cents *= 2 #multiply by 2 as each day passes
        day += 1
    
    print(cents,"c")

moneyStack(30) #call the function, x number of days

#exercise 5
userGuess = 0
guessCount = 0
botNumber = random.randint(1, 90)
print(botNumber)

while userGuess != botNumber:
    userGuess = int(input("="*40+"\nGuess a number between 1 to 90\nYour guess: "))
    guessCount += 1

    if userGuess == botNumber:
        print("Well guessed!\nTotal number of guesses: ",guessCount)
    elif userGuess < botNumber:
        print(userGuess,"is lower than the answer. Try again.\nGuess count: ",guessCount)
    elif userGuess > botNumber:
        print(userGuess,"is higher than the answer. Try again. \nGuess count: ",guessCount)
    elif userGuess < 1 or userGuess > 90:
        print("Please put a proper guess!")
    else:
        print("Put a correct input!")