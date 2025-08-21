import random

name = input("enter your name: ") # input function is string by default so removed the cast

print(f'\nHi {name}, welcome to RPS, enter "exit" or "quit" to leave at any time\n')


round = 1 # NOTE Round is a keyword round() function in the python library, probably best not to use it a variable name
playing = True
isRepeat = False
randWins = 0
playerWins = 0
ties = 0

while(playing):
    
    print(f'\t\tROUND {round}') # NOTE Moved the counter to the end of the while loop. That way you won't need the if/else block.
    
    if playerWins > 2: pass #print
    if randWins > 2: pass #print

    res = input("will you choose rock, paper or scissors: ").lower()

    if res in ["exit","quit"]: # NOTE: if they quit, break statement will kick them from the loop
        print("exiting")
        break

    if res in "rock": # NOTE: the in statement will search within the string, so this if will return true if the user enters r, or ro, or roc or ock etc
        playerChoice = 1
    elif res in "paper":
        playerChoice = 2
    elif res in "scissors":
        playerChoice = 3
    else:
        print("invalid choice, try again") # NOTE: removed the repeat flag
        continue

    randChoice = random.randint(1,3)
    
     

    if randChoice == playerChoice: 
        ties += 1
        print("tie") #tie
    if playerChoice > randChoice or (playerChoice == 1 and randChoice == 3):
        playerWins += 1
        print("player won") #player win
    else:
        randWins += 1
        print("computer won") #rand win
    
    round += 1
    if round == 6:
        break
    else: continue