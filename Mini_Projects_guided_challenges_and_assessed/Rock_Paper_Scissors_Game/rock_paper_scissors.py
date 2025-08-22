"""
Implement a Rock, Paper, Scissors game, where a user plays against a computer

"""
import random

#-------------------------------------------------------------------------------

def get_name():
    """Takes input from user and returns string"""
    player_name = input("Please enter your name: ")
    if player_name == "":
        player_name = "Guest"
    return player_name

def greeting(player_name):
    """Takes string as input and returns personalised greeting with game name
    and description"""
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
    
    pc, cc = player_choice, computer_choice
    if  pc == 'rock' and cc == "scissors" or pc == "paper" and cc == "rock" or pc == "scissors" and cc == "paper":
        return 1
    elif cc == 'rock' and pc == "scissors" or cc == "paper" and pc == "rock" or cc == "scissors" and pc == "paper" :
        return 2
    else:
        return 0
    
def game_score_player(player_name, wins, losses, ties):
    """Display current game total (wins, losses, ties)"""
    return f"{player_name}'s Score: Wins: {wins}, Losses: {losses}, Ties: {ties}"

def game_score_computer(wins, losses, ties):
    """Display current game total (wins, losses, ties)"""
    return f"Computer's Score: Wins: {wins}, Losses: {losses}, Ties: {ties}"

def play_game(player_name, num_rounds):
    
    # Constants
    PERSON_EMOJI = "\U0001F9D1"
    COMPUTER_EMOJI = "\U0001F4BB"
    CELEBRATE_EMOJI = "\U0001F389"
    BLUE_TEXT_START = "\033[34m"
    END_TEXT_COLOR = "\033[0m"
    GREEN_TEXT_START = "\033[32m"
    
    # Variables
    round_count = 1 # counter for number of rounds
    total_rounds = num_rounds # number of rounds per game
    round_break = total_rounds // 2 + 1 # short circuit round if win, loss or tie decided
    player_wins, player_losses, computer_wins, computer_losses, ties = 0, 0, 0, 0, 0 # counter: wins, losses and ties
    
    while round_count <= total_rounds:
    
        # print game round
        print(f"\n{BLUE_TEXT_START}ROUND {round_count}{END_TEXT_COLOR}\n")
        # Get player_choice
        player_choice = get_player_choice().strip().lower()
        # Validate input
        valid_input = player_choice.isalpha() 
        if valid_input:
            choice = display_choice(player_choice) 
            if  choice == "Thanks for playing!":
                print(f"\n{choice}")
                break
            elif choice == "invalid choice":
                print(f"\n{GREEN_TEXT_START}Please enter rock, paper or scissors:{END_TEXT_COLOR} ")
                continue
            else:
                print(f"\n{choice}")
        else:
            print(f"\n{GREEN_TEXT_START}Please enter rock, paper or scissors:{END_TEXT_COLOR} ")
            continue
        # Get and display computer choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice.title()}")
        # Decide winner
        game_result = decide_winner(player_choice, computer_choice)
    
        if game_result == 0:
            ties += 1
            print(f"It's a tie! {PERSON_EMOJI} {COMPUTER_EMOJI}")
        elif game_result == 1:
            player_wins += 1
            computer_losses += 1
            print(f"You win! {PERSON_EMOJI} {CELEBRATE_EMOJI}")
        else:
            player_losses += 1
            computer_wins += 1
            print(f"Computer Wins! {COMPUTER_EMOJI} {CELEBRATE_EMOJI}")
        # display Results
        
        player_score = game_score_player(player_name, player_wins, player_losses, ties)
        computer_score = game_score_computer(computer_wins, computer_losses, ties)
        
        # Check if player has round_break wins, losses or ties
        if ties == round_break or player_wins == round_break or player_losses == round_break:
            break
        else:
            print(f"\n{player_score}")
            print(computer_score)
        # Increment round_count
        round_count += 1
        
    if player_wins == round_break or player_wins > player_losses:
        game_winner = f"{player_name} WON!"
    elif player_losses == round_break or player_losses > player_wins:
        game_winner = "Computer WON!"
    else:
        game_winner = "Its a tie!"
    
    print(f"\n{GREEN_TEXT_START}Final Scores:{END_TEXT_COLOR}\n")
    print(f"{player_name}'s Final Score - Wins: {player_wins}, Losses: {player_losses}, Ties: {ties}")
    print(f"Computer's Final Score - Wins: {player_losses}, Losses: {player_wins}, Ties: {ties}")
    print(f"\n{game_winner}")    
   
    

