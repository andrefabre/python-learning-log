# This is a guess the number game
import random
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