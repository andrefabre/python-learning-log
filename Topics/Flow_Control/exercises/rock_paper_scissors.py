import random, sys

print("ROCK, PAPER, SCISSORS")

# These variables keep track of the number of wins, losses, and ties.

wins = 0
losses = 0
ties = 0

while True: # the main game loop
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    while True: # the player input loop
        print("Enter your move r(rock), p(paper), s(scissors) or q (quit)")
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program
        elif playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop
        print("Type one of r, p, s, or q")
        
    # Display what the player chose:
    if playerMove == 'r':
        print("ROCK versus ...")
    elif playerMove == 'p':
        print("PAPER versus...")
    elif playerMove == 's': 
        print("SCISSORS versus...")
        
    # Display what the computer chose; 
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print("ROCK")
    elif randomNumber == 2:
        computerMove = 'p'
        print("PAPER")
    elif randomNumber == 3:
        computerMove = 's'
        print("SCISSORS")
        
    # Display and record the Win/Loss/Tie
    if playerMove == computerMove:
        print("Its a tie!")
        ties += 1
    if playerMove == 'r' and computerMove == 's':
        print("You Win!")
        wins += 1
    if playerMove == 'p' and computerMove == 'r':
        print("You Win!")
        wins += 1
    if playerMove == 's' and computerMove == 'p':
        print("You Win!")
        wins += 1
    if playerMove == 'r' and computerMove == 'p':
        print("You Lose!")
        losses += 1
    if playerMove == 'p' and computerMove == 's':
        print("You Lose!")
        losses += 1
    if playerMove == 's' and computerMove == 'r':
        print("You Lose!")
        losses += 1
        
            
        