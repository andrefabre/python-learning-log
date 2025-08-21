"""
Implement a Rock, Paper, Scissors game, where a user plays against a computer

Requirements:
    1.  The game should prompt the user to enter their name and write a greeting message
    2.  The game should the user to enter a choice. The input should be validated to ensure
        that the user only enters one of the valid options: rock, paper or scissors
    3.  The computer will randomly select one of these options
    4.  The winner will be determined according to the following rules:
            Rock beats Scissors
            Scissors beats Paper
            Paper beats Rock
    5.  If both the user and the computer select the same option, it is a tie
    6.  Implement a best of 5 series, where the first player to win 3 rounds wins 
        the overall game.
    7.  Display the choices of both the user and the computer after each round    
    8.  After each round, display the result of the game (win, lose, or tie).
    9.  Keep track of the score, displaying the number of wins, losses, and ties
        after each round for both player and computer.
    10. The user should be able to type "exit" at any time to quit the game.
    11. Display the winner of the best of 5 series after the game ends
"""
import random
import sys
# The game should prompt the user to enter their name and write a greeting message

playerName = input("""Welcome to Gamespace
                   
Please enter your name: """)

# Display Greeting

message = print(f"""
Hi {playerName},
    
Today's game is Rock, Paper, Scissors

Game Rules:

1. It is a best of 5 series 
2. Each round you will choose Rock, Paper or Scissors
3. The computer will then make a choice
4. The winner will be determined by the following rules
    Rock beats Scissors
    Scissors beats Paper
    Paper beats Rock

You can quit the game at any time by entering "quit" """)

print(message)

# Play Game
countRound = 1 # counter; counts number of rounds
totalRounds = 5 # total number of rounds in the game
wins, losses, ties = 0, 0, 0 # counter: wins, losses and ties
# TODO: wins and losses variables to be updated to playerWins, playerLosses.
# computerWin and computerLosses

while countRound <= totalRounds: # prevent infinite loop, loop will break when counter == 5
    
    # print current round number
    print(f"\nROUND {countRound}\n") 
    # get player choice
    playerChoice = input("Choose Rock, Paper, or Scissors: ")
    # validate input: strip input of whitespace, format to lowercase, save to playerChoice variable
    playerChoice = playerChoice.strip().lower()
    
    if playerChoice.isalpha(): # returns true if string consists of letters and is not blank
        if playerChoice == "quit": # if player enters 'quit' prints message and exits game
            print("Thanks for playing!")
            sys.exit()
        elif playerChoice == "rock" or playerChoice == "paper" or playerChoice == "scissors":
            print(f"You chose: {playerChoice.title()}") 
        else: #TODO - Line to be removed, using it for testing logic
            print("Input is invalid")
            continue
    else:
        print("Input is not a string") # TODO - print statement to be removed 
        continue
        
    # Create computer choice
    computerChoice = random.randint(1, 3) # calls randint method to create random number between 1 and 3
    ## if num is 1 = rock, if num is 2 == paper if num is 3 == scissors
    ## print computerChoice to screen. title() method capitalises string e.g. Rock
    if computerChoice == 1:
        computerChoice = "rock"
        print(f"Computer chose: {computerChoice.title()}")
    elif computerChoice == 2:
        computerChoice = "paper"
        print(f"Computer chose: {computerChoice.title()}")
    else:
        computerChoice = "scissors"
        print(f"Computer chose: {computerChoice.title()}")

    # Decide Winner
    # TODO: both player and computer need to have counter,
    # as player and computer win/loss/ tie need to be displayed
    # wins to be change to playerWins, losses to be changef to playerLosses.
    # computerWins, computerLosses counters need to be added to elif statments.
    # Ties stay unchanged
    if playerChoice == computerChoice:
        ties += 1 # add one to tie counter
        print("Its a tie!")
    elif playerChoice == 'rock' and computerChoice == "paper":
        losses += 1
        print("Computer wins!")
    elif playerChoice == 'rock' and computerChoice == "scissors":
        wins += 1
        print("You win!")
    elif playerChoice == "paper" and computerChoice == "rock":
        wins += 1
        print("You win!")
    elif playerChoice == "paper" and computerChoice == "scissors":
        losses += 1
        print("Computer wins!")
    elif playerChoice == "scissors" and computerChoice == "rock":
        losses += 1
        print("Computer wins!")
    else:
        wins += 1
        print("You win!")

    # Display Game Score
    # Requirement for the game is to break from game if there 3 wins, 3 losses or 3 ties
    # Check if player has 3 wins, losses or ties
    # TODO: needs to be updated to check computer wins and losses
    # TODO: requires two print statements for running scores. One for player and one for computer
    if wins == 3 or ties == 3 or losses == 3:
        break
    else:
        gameScore = f"\nGame Score: Wins: {wins}, Losses: {losses}, Ties: {ties}"
        print(gameScore)
    
    # Increment Round count
    countRound += 1
    
#TODO: requires final scores print statements to be updated to match the sample output
if wins == 3:
    result = "{playerName} Wins!"
elif losses == 3:
    result = "Computer Wins!"
else:
    result = "Its a tie"
print(f"\nFinal Result: {result}")