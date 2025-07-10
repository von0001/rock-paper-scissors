import random

def startMenu():
    print("ROCK PAPER SCISSORS // by von")
    print("[1] - Play Game")
    print("[2] - Rules")
    print("[3] - Exit")
    
#functions
def StartMenuInput():
    while True:
        menuInput = str(input("")).lower()
        
        if menuInput in ["play game", "1", "2", "rules", "exit", "3"]:
            if menuInput == "rules" or menuInput == "2":
                return "rules"
            elif menuInput == "play game" or menuInput == "1":
                return "play game"
            elif menuInput == "exit" or menuInput == "3":
                return "exit"
        else:
            print("Incorrect input. Please try again!")

def BestOutOfMenu():
    print("[1] - Single Round")
    print("[2] - Best of N")
    print("[3] - Back")

def BOOInput():
    while True:
        booChoice = str(input("")).lower()
        
        if booChoice in ["single round", "1", "2", "best of n", "back", "3"]:
            if booChoice == "single round" or booChoice == "1":
                return "single round"
            elif booChoice == "best of n" or booChoice == "2":
                return "best of n"
            elif booChoice == "back" or booChoice == "3":
                return "back"
        else:
            print("Incorrect input. Please try again!")

def Rules():
    print("The rules of rock paper scissors is pretty simple. The computer will one of the three options: Rock, Paper, or Scissors.")
    print("Your job is to be the computer by choosing a choice that beats the computer.")
    print("Paper beats rock. Rock beats scissors. Scissors beats paper.")
    print("[1] - Back")
    while True:
        exitRulesChoice = str(input("")).lower()
        if exitRulesChoice in ["back" , "1"]:
            return exitRulesChoice
        else:
            print("Wrong input. Please enter yes.") 

def Replay():
    while True:
        print("Would you like to play again? [Yes/No]")
        replayInput = str(input("")).lower()
        if replayInput in ["yes", "no"]:
            return replayInput
        else:
            print("That is an incorrect input. Only inputs are: [Yes/No]. Please try again.")

def bestofNLogic():
    print("Best out of how many rounds? (Odd Numbers Only)")
    
    while True:
        BOORoundsInput = int(input(""))

        if BOORoundsInput % 2 == 1:
            return BOORoundsInput
        else:
            print("Your number is not an odd number. Please try again.")

def playRound():
    userwon = False
    tie = False
    computerList = ["paper", "scissors", "rock"]
    computerGuess = random.choice(computerList)
    
    while True:
        print("What would be your guess: Rock, Paper, or Scissors?")
        userGuess = input("").lower()
        if userGuess in ["rock", "paper", "scissors"]:
            break
        else:
            print("Wrong input, try again. Inputs are: Rock, Paper, or Scissors.")

    if userGuess == computerGuess:
        print("You both have guessed the same option.")
        tie = True
        userWon = None
    elif userGuess == "paper" and computerGuess == "scissors":
        print("The computer has picked scissors. You chose paper. Computer wins!")
        userWon = False
    elif userGuess == "scissors" and computerGuess == "paper":
        print("The computer has picked paper. You chose scissors. You've won!")
        userWon = True
    elif userGuess == "rock" and computerGuess == "paper":
        print("The computer has picked paper. You chose rock. You've lost.")
        userWon = False
    elif userGuess == "paper" and computerGuess == "rock":
        print("The computer has picked rock. You chose paper. You've won!")
        userWon = True
    elif userGuess == "rock" and computerGuess == "scissors":
        print("The computer has chosen scissors. You chose rock. You've won!")
        userWon = True
    elif userGuess == "scissors" and computerGuess == "rock":
        print("The computer has chosen rock. You chose scissors. You've lost")
        userWon = False
    else:
        userWon = None
        
    return userWon, tie

#variables
userScore = 0
computerScore = 0
tieScore = 0
userWon = False
tie = False


#code
while True:
        
        startMenu()

        menuInput = StartMenuInput()
            
        if menuInput == "play game":
            BestOutOfMenu()
            booChoice = BOOInput()
            if booChoice == "single round":
                 userWon, tie = playRound()
                 if userWon == True:
                     userScore += 1
                     print("You won this round!")
                 elif userWon == False:
                     computerScore += 1
                     print("The computer has won this round.")
            if booChoice == "best of n":
                userScore = 0
                computerScore = 0
                ties = 0
                userWon = False
                BOORoundsInput = bestofNLogic()
                roundsToWin = (BOORoundsInput // 2) + 1
                while userScore < roundsToWin and computerScore < roundsToWin:
                    userWon, tie = playRound()
                    if userWon == True:
                        userScore += 1
                    elif userWon == False:
                        computerScore += 1
                    elif tie == True:
                        tieScore += 1
                        
                    print(f"Score: You - {userScore} | Computer - {computerScore} | Tie - {tieScore}")
                else:
                    if userScore == roundsToWin:
                        print(f"You have won the best out of {BOORoundsInput}!")
                    elif computerScore == roundsToWin:
                        print(f"The computer has won the best out of {BOORoundsInput}.")
        
        replayInput = Replay()