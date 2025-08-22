import sys
import rock_paper_scissors as rps


def main():
    # The game should prompt the user to enter their name and write a greeting message
    print("\nWelcome to Gamespace\n")
    
    # Get player name and display greeting
    player_name = rps.get_name().title()
    rps.greeting(player_name)
    
    # Play Game and set number of rounds
    num_rounds = int(input("How many rounds would you like to play?: "))
    rps.play_game(player_name, num_rounds)
    
    # Play again
    while True:
        play_again = input("\nWould you like to play again (Y/N)?: ").strip().lower()
   
        if play_again == "y" or play_again == "yes":
            rps.play_game(player_name, num_rounds)
        elif play_again == "n" or play_again == "no":
            sys.exit()
            
main()