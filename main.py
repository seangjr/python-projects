import random

def rockPaperScissors():

    print("="*60)
    userInput = str(input("Rock, Paper or Scissors? (Case sensitive)\nInput: "))

    botNumber = random.randrange(1, 3+1)
    
    if botNumber == 1:
        botNumber = "Rock"
    elif botNumber == 2:
        botNumber = "Paper"
    else:
        botNumber = "Scissors"

    if userInput != "Paper" and userInput != "Rock" and userInput != "Scissors":
        print("Please put correct input!")
    elif (userInput == botNumber):
        print("It's a tie!")
    elif (userInput == "Rock" and botNumber == "Paper") or (userInput == "Paper" and botNumber == "Scissors") or (userInput == "Scissors" or botNumber == "Rock"):
        print("You lost! Bot played "+botNumber)
    else:
        print("You win! Bot played "+botNumber)

rockPaperScissors()