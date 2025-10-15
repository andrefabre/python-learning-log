"""
# Purpose: ICT100 Transition to IT Assignment 2 - Guess the Number Game
# Author/s: Andre Fabre
NOTE # Copyright: 10 October 2025

Program Description:

The goal is to develop a simple software application that asks users to guess a random number between 1 and 10 and gives them (3) chances to correctly guess the answer

Constraints:
- A text-based (aka console) application
- No graphical user interface (GUI)
- Not a desktop application
- Not a web application
- Not a mobile application

Requirements:

Functions:
    - menu(): Displays the menu and gets user menu choice
    - add_movie(): Prompts user to enter a movie name to add the movie_names
    - remove_movie(): Prompts user to enter a movie name to remove from the movie_names
    - view_all(): Displays all movies in the list and their watched/unwatched status
    - mark_as_watched(): Prompts user to enter a movie name to mark as watched
    - search_movie(): Searches for a movie by name

"""
# This is a guess the number game

secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20")

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())
    
    if guess < secretNumber:
        print("Your guess is to low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break
        # This condition if the correct guess

if guess == secretNumber:
    print(f"Good job!. You guessed my number in {guessesTaken} guesses")
else:
    print(f"Nope, the number I was thinking of was {secretNumber}")