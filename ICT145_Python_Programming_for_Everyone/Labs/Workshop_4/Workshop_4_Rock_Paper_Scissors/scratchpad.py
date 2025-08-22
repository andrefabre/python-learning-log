def get_name(player_name="Guest"):
    """Takes input from user and returns string"""
    player_name = input("Please enter your name: ")
    # if player_name == "":
    #     player_name = "Guest"
    return player_name

print(get_name())