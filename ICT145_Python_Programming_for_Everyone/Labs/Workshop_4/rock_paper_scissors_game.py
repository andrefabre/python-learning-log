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

def greeting(playerName):
    
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

    return message


# Display Greeting
greeting(playerName)

# Play Game
countRound = 1
totalRounds = 5
wins, losses, ties = 0, 0, 0 # counter: wins, losses and ties
winner = True # true if player wins

while countRound <= totalRounds:
    
    print(f"\nROUND {countRound}\n")
    # get player choice
    playerChoice = input("Choose Rock, Paper, or Scissors: ")
    # validate input: strip input of whitespace, format to lowercase
    playerChoice = playerChoice.strip().lower()
    if playerChoice.isalpha(): # returns true if string consists of letters and is not blank
        if playerChoice == "quit":
            print("Thanks for playing!")
            sys.exit()
        elif playerChoice == "rock" or playerChoice == "paper" or playerChoice == "scissors":
            print(f"You chose: {playerChoice.title()}")
        else:
            print("Input is invalid")
            continue
    else:
        print("Input is not a string")
        continue
        
    # Create computer choice
    computerChoice = random.randint(1, 3)
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
    # Check if player has 3 wins, losses or ties
    if wins == 3 or ties == 3 or losses == 3:
        break
    else:
        gameScore = f"\nGame Score: Wins: {wins}, Losses: {losses}, Ties: {ties}"
        print(gameScore)
    
    # Increment Round count
    countRound += 1
    

if wins == 3:
    result = "{playerName} Wins!"
elif losses == 3:
    result = "Computer Wins!"
else:
    result = "Its a tie"
print(f"\nFinal Result: {result}")