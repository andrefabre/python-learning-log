def main():
    print(take_input())
    
def take_input():
    
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer of Single-player? ")
    return (difficulty, players)


if __name__ == "__main__":
    main()
