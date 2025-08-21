#-------------------------------------------------------------------------------
#   Chapter 7: User Input and While Loops
#-------------------------------------------------------------------------------

# The input function pauses your program and waits for the user to enter some
# text

# Example: write a prompt that is longer than one line

prompt = "If you share your name we can personalise the messages you see"
prompt += "\nWhat is your first name? "

name = input(prompt).lower()
print(f"Hello {name}")