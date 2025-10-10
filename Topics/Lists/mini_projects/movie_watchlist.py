"""
# Purpose: Workhop 9 - Mini Project - Movie Watchlist
# Group Name: External Group - 14
# Author/s: Andre Fabre
# Copyright: 10 October 2025

Program Description:

Create a Python-based Movie Watchlist Manager that allows users to add movie titles,
remove them, view the complete list, mark movies as watched, and search for movies
by name.

Requirements: You must build a console-based menu-driven program offering the
following features. Create fuctions for each feature and menu

Functions:
    - menu(): Displays the menu and gets user menu choice
    - add_movie(): Prompts user to enter a movie name to add the movie_names
    - remove_movie(): Prompts user to enter a movie name to remove from the movie_names
    - view_all(): Displays all movies in the list and their watched/unwatched status
    - mark_as_watched(): Prompts user to enter a movie name to mark as watched
    - search_movie(): Searches for a movie by name

"""

def main():
    '''Main function to run the Movie Watchlist Manager'''
    
    movie_names = []  # List to store movie names
    watched_status = []  # List to store watched/unwatched status

    movie_choice = menu()  # Get initial user menu choice
    while movie_choice != 6:
        
        match movie_choice:
            case 1:
                # Call add_movie function to add movie to movie_names
                add_movie(movie_names, watched_status)
                
            case 2:
                # Call remove_movie function to remove movie from movie_names
                remove_movie(movie_names, watched_status)
                
            case 3:
                # Call view_all function to display all movies in movie_names and watched status
                view_all(movie_names, watched_status)

            case 4:
                # Call mark_as_watched function to mark a movie as watched
                mark_as_watched(movie_names, watched_status)
                
            case 5:
                # Call search_movie function
                search_movie(movie_names, watched_status)

        # Print menu to console and get user menu choice
        movie_choice = menu()

    # Display exit message when menu_choice == 6
    print("\nGoodbye!")
    
def menu():
    '''Displays the menu options and gets user choice
    Valid choices are int(1-6).
    On invalid choice, it will keep prompting user until a valid choice is entered.
    
    Returns:
        movie_choice (int): User's menu choice
    '''
    print("""
    --- Movie Watchlist ---
    1. Add Movie
    2. Remove Movie
    3. View Watchlist
    4. Mark as Watched
    5. Search Movie
    6. Exit
    ------------------------""")
    
    while True:
        try:
            movie_choice = int(input("Choose an option (1-6): "))
            if movie_choice in [1, 2, 3, 4, 5, 6]:
                return movie_choice
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

def add_movie(movie_names, watched_status):
    ''' Prompts user to enter a movie name to add to the movie_names.
        Checks for empty input and adds movie to movie_names with "Not Watched" status.
        Checks for duplicates and does not add if movie already exists.

    Args:
        movie_names (list): List to store movies
        watched_status (list): List to store watched status
        
    Returns:
        None '''
    
    # Get user input: movie name to add
    movie_name = input("Enter movie name: ").strip().lower()
    
    # Validate input: movie name should not be empty
    while len(movie_name) == 0:
        print("Movie name cannot be blank. Please try again.")
        movie_name = input("Enter movie name: ").strip().lower()
    
    # Check movie name is not in the movie_names
    if movie_name in movie_names:
        print("Movie already exists in the watchlist.")
        return
    
    # Add movie to movie_names and set its status to "Not Watched"
    movie_names.append(movie_name)
    watched_status.append("✗ Not Watched")
    
    # Print confirmation message to console
    print(f"{movie_name.title()} added to movie_names.")

def remove_movie(movie_names, watched_status):
    '''Prompts user to enter a movie name to remove from the movie_names
    
    Args:
        movie_names (list): List to store movies
        watched_status (list): List to store watched status
    Returns:
        None '''
        
    # Get user input: movie name to remove    
    movie_name = input("Enter the movie name to remove: ").strip().lower()
    
    # Check if movie exists in the movie_names; Remove if it does
    if movie_name in movie_names:
        movie_index = movie_names.index(movie_name)   # Find the index of the movie
        movie_names.pop(movie_index)                  # Remove movie from movie_names
        watched_status.pop(movie_index)             # Remove watched status    
    else:
        print(f"'{movie_name.title()}' not found.")
        return
    
    # Print confirmation message to console
    print(f"'{movie_name.title()}' removed from watchlist.")

def view_all(movie_names, watched_status):
    '''Displays all movies in the list along with their watched/unwatched status

    Args:
        movie_names (list): List to store movies
        watched_status (list): List to store watched status
    Returns:
        None 
    '''
  
    # Print header
    print(f"Displaying all movies in the watchlist.\n")
    
    # Check if movie_names is empty
    if not movie_names:
        print("Watchlist is empty.")
        return
    else:
        # Print name of each movie with its watched status to console
        count = 1
        for movie, status in zip(movie_names, watched_status):
            print(f"{count}. {movie.title()} - {status}")
            count += 1

def mark_as_watched(movie_names, watched_status):
    '''Prompts user to enter a movie name to mark as watched

    Args:
        movie_names (list): List to store movies
        watched_status (list): List to store watched status
    Returns:
        None '''
        
    # Get user input: movie name to mark as watched
    while True:
        movie_name = input("Enter the movie name to mark as watched: ").strip().lower()
        if len(movie_name) != 0:
            break
        else:
            print("Movie name cannot be empty. Please try again.")
    
    # Check if movie exists in the movie_names
    if movie_name not in movie_names:
        print(f"'{movie_name.title()}' not found in the watchlist.")
        return
    
    # Find the index of the movie and update its status in watched_status list
    movie_index = movie_names.index(movie_name)
    watched_status[movie_index] = "✓ Watched"

    # Print confirmation message to console
    print(f"'{movie_name.title()}' marked as watched.")

def search_movie(movie_names, watched_status):
    '''Searches movie_names by keyword; displays movie title and watched status for movies which contain the keyword.
    
    Args:
        movie_names (list): List to store movies
        watched_status (list): List to store watched status
    Returns:
        None '''
        
    # Get user input: keyword to search
    search_item = input("Enter the movie name to search: ").strip().lower()
    
    # If search term is empty, display full movie_names
    if len(search_item) == 0:
        print("No search term entered. Displaying full watchlist.")
        view_all(movie_names, watched_status)
    else:
        print(f"Searching for movies containing '{search_item}'...")
    # Search for the keyword in the movie_names; display movie title and watched status to consoleif found
        for item in range(len(movie_names)):
            if search_item in movie_names[item]:
                print(f"Found: {movie_names[item].title()} - {watched_status[item]}")
    return
    
    
main()