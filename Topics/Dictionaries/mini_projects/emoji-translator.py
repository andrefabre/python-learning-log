"""
# Purpose: Workhop 10 - Mini Project - Emoji Translator
# Group Name: External Group - 14
# Author/s: Andre Fabre
# Copyright: 18 October 2025

Program Description:

Create a Python-based Emoji Translator application that allows users to translate plain english words or phrases into emojis, and vice versa.
Users can also add their own customer emoji mappings during runtime

Requirements: You must build a console-based menu-driven program offering the
following features.

Functions:
    - menu(): Displays the menu and gets user menu choice
    - text_to_emoji(): Prompts user to enter a sentence to translate to emojis
    - emoji_to_text(): Prompts user to enter a sentence to translate to text
    - add_custom_emoji(): Prompts user to enter a word and its corresponding emoji to add to the emoji dictionary
    - view_all_emojis(): Displays all emojis in the dictionary

"""

def main():
    '''Main function to run the Emoji Translator'''

    # Initialize emoji dictionary
    emoji_dict = {
        "love": "❤️",
        "pizza": "🍕",
        "cat": "🐱",
        "dog": "🐶",
        "happy": "😊",
        "sad": "😢",
        "sun": "☀️",
        "moon": "🌙",
        "car": "🚗",
        "bike": "🚲",
        # "apple": "🍎",
        # "banana": "🍌",
    }

    # Display menu in console and get user choice
    menu_choice = menu()

    while menu_choice != 5:

        match menu_choice:
            case 1:
                # Translate text to emojis
                text_to_emoji(emoji_dict)
            case 2:
                # Translate emojis to text
                emoji_to_text(emoji_dict)
            case 3:
                # Add a custom emoji to the dictionary
                add_custom_emoji(emoji_dict)
            case 4:
                # View all emojis in the dictionary
                view_all_emojis(emoji_dict)

        menu_choice = menu()
        
    # Display exit message to console when menu_choice == 5
    print("\nThanks for using Emoji Translator. Goodbye! 😊")
    
def menu():
    """ Displays the menu and gets user menu choice.
    Valid choices are int between 1 and 5.
    If input == invalid choice, prompt user to try again.
    
    Returns:
        menu_choice (int): user menu choice
    """
    print("""
--- Emoji Translator Menu ---
1. Text to Emoji
2. Emoji to Text
3. Add a Custom Emoji
4. View All Emojis
5. Exit
-----------------------------""")

    while True:
        try:
            menu_choice = int(input("\nChoose an option: "))
            if menu_choice in [1, 2, 3, 4, 5]:
                return menu_choice
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 5.")

def text_to_emoji(emoji_dict):
    """ Translates text to emojis using the emoji_dict.
    Prompts user to enter a sentence to translate to emojis.
    
    Returns:
        None
    """
    
    # Prompt user to enter a sentence to translate to emojis, validate input is not empty
    
    while True:
        
        text = input("Enter a sentence: ").strip()
        if text:
            break
        else:
            print("Input cannot be empty. Please try again.")
    
    # Translate text to emojis
    emojis = [emoji_dict.get(word, word) for word in text.split()]
    
    # Display the translated emojis to console
    print("\nTranslated:", " ".join(emojis))
    

def emoji_to_text(emoji_dict):
    """ Translates emojis to text using the emoji_dict.
    Prompts user to enter a sentence to translate to text.
    
    Returns:
        None
    """
    
    # Create a reversed dictionary for emoji to text translation
    emoji_dict_reversed = {v: k for k, v in emoji_dict.items()}
    
    # Prompt user to enter a sentence to translate to text
    text = input("Enter emojis: ")
    
    # Validate input is not empty
    while not text:
        
        print("Input cannot be empty. Please try again.")
        text = input("Enter emojis: ")
    
    # Translate emojis to text
    words = text.split()
    translated = [emoji_dict_reversed.get(word, word) for word in words]

    # Display the translated text to console
    print("\nText:", " ".join(translated))

def add_custom_emoji(emoji_dict):
    """ Adds a custom emoji to the emoji_dict.
    Prompts user to enter a word and its corresponding emoji
        to add to the emoji dictionary.
    Returns:
        None
    """
    
    # Prompt user to enter a word; validate input is not empty and not a duplicate
    while True:
        
        word = input("Enter a new word: ").strip().lower()
        if word:
            if word in emoji_dict:
                print("Word already exists in the emoji dictionary. Please try again.")
                continue
            else:
                while True:
                    emoji = input("Enter the corresponding emoji: ").strip()
                    if emoji:
                        
                        # Add the custom emoji to the dictionary
                        emoji_dict[word] = emoji
    
                        # Print confirmation message to console
                        print(f"\nAdded: '{word}' -> {emoji}")
                        break
                    else:
                        print("Emoji cannot be empty. Please try again.")
            break
        else:
            print("Word cannot be empty. Please try again.")


def view_all_emojis(emoji_dict):
    """ Displays all emojis in the emoji_dict
    Returns:
        None
    """
    
    # Validate emoji_dict IS NOT empty; print emoji-dict to console
    if not emoji_dict:
        print("No emojis found.")
    else:
        print("\nCurrent Emoji Mappings:")
        for word, emoji in emoji_dict.items():
            print(f"{word}: {emoji}")
    

main()