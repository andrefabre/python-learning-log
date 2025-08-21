"""
Implement a Rock, Paper, Scissors game, where a user plays against a computer

"""
import random
import sys

def main():
    # The game should prompt the user to enter their name and write a greeting message
    print("\nWelcome to Gamespace\n")
    player_name = get_name().title()
    greeting(player_name)
    # Play Game
    play_game(player_name)
    # Play again
    while True:
        play_again = input("Would you like to play again (Y/N)?: ").strip().lower()
   
        if play_again == "y" or play_again == "yes":
            play_game(player_name)
        elif play_again == "n" or play_again == "no":
            sys.exit()
#-------------------------------------------------------------------------------

def get_name():
    player_name = input("Please enter your name: ")
    if player_name == "":
        player_name = "Guest"
    return player_name

def greeting(player_name):
    
    message = print(f"""
Hi {player_name},
    
Today's game is Rock, Paper, Scissors

Game Rules:

1. It is a best of 5 series 
2. Each round you will choose Rock, Paper or Scissors
3. The computer will then make a choice
4. The winner will be determined by the following rules
    Rock beats Scissors
    Scissors beats Paper
    Paper beats Rock

You can quit the game at any time by entering "quit"
""")

    return message

def get_player_choice():
    """ Get input from user, returns string"""
    player_choice = input("Choose Rock, Paper, or Scissors: ")
    return player_choice

def validate_input(player_choice):
    """ returns True is input is valid"""
    # validate input: strip input of whitespace, format to lowercase
    player_choice = player_choice.strip().lower()
    return player_choice.isalpha() # returns true if string consists of letters and is not blank

def display_choice(player_choice):
    """ returns str = rock, paper, scissors or quit"""
    if player_choice == "quit":
        return "Thanks for playing!"
    elif player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
        return f"You chose: {player_choice.title()}"
    else:
        return "invalid choice"

def get_computer_choice():
    """ returns computer choice; rock, paper, or scissors"""
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_choice = "rock"
    elif computer_choice == 2:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"
    return computer_choice

def decide_winner(player_choice, computer_choice):
    """Decides winner from Rock, Paper, Scissors single game
    tie game = 0, player win = 1, computer win = 2"""
    
    if player_choice == 'rock' and computer_choice == "paper":
        return 2
    elif player_choice == 'rock' and computer_choice == "scissors":
        return 1
    elif player_choice == "paper" and computer_choice == "rock":
        return 1
    elif player_choice == "paper" and computer_choice == "scissors":
        return 2
    elif player_choice == "scissors" and computer_choice == "rock":
        return 2
    else:
        return 0
    
def game_score_player(player_name, wins, losses, ties):
    """Display current game total (wins, losses, ties)"""
    return f"{player_name}'s Score: Wins: {wins}, Losses: {losses}, Ties: {ties}"

def game_score_computer(wins, losses, ties):
    """Display current game total (wins, losses, ties)"""
    return f"Computer's Score: Wins: {wins}, Losses: {losses}, Ties: {ties}"

def play_game(player_name):
    
    round_count = 1
    total_rounds = 5
    round_break = total_rounds // 2 + 1 # short circuit round if win, loss or tie decide
    player_wins, player_losses, computer_wins, computer_losses, ties = 0, 0, 0, 0, 0 # counter: wins, losses and ties
    
    while round_count <= total_rounds:
    
        # print game round
        print(f"\nROUND {round_count}\n")
        # Get player_choice
        player_choice = get_player_choice().lower()
        # Validate input
        valid_input = validate_input(player_choice)  
        if valid_input:
            choice = display_choice(player_choice) 
            if  choice == "Thanks for playing!":
                print(f"\n{choice}")
                break
            elif choice == "invalid choice":
                continue
            else:
                print(f"\n{choice}")
        else:
            continue
        # Get and display computer choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice.title()}")
        # Decide winner
        game_result = decide_winner(player_choice, computer_choice)
        if game_result == 0:
            ties += 1
            print("It's a tie! \U0001F9D1 \U0001F4BB")
        elif game_result == 1:
            player_wins += 1
            computer_losses += 1
            print("You win! \U0001F9D1 \U0001F389")
        else:
            player_losses += 1
            computer_wins += 1
            print("Computer Wins! \U0001F4BB \U0001F389")
        # display Results
        
        player_score = game_score_player(player_name, player_wins, player_losses, ties)
        computer_score = game_score_computer(computer_wins, computer_losses, ties)
        
        # Check if player has 3 wins, losses or ties
        if ties == round_break or player_wins == round_break or player_losses == round_break:
            break
        else:
            print(f"\n{player_score}")
            print(computer_score)
        # Increment round_count
        round_count += 1
        
    if player_wins == round_break:
        game_winner = "{player_name} WON!"
    elif player_losses == round_break:
        game_winner = "Computer WON!"
    else:
        game_winner = "Its a tie!"
    
    print("\nFinal Scores:\n")
    print(f"{player_name}'s Final Score - Wins: {player_wins}, Losses: {player_losses}, Ties: {ties}")
    print(f"Computer's Final Score - Wins: {player_losses}, Losses: {player_wins}, Ties: {ties}")
    print(f"\n{game_winner}")    
   
    
    
main()

