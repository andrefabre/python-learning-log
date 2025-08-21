#! python3
# mclip.py - A multi-clipboard program
import sys, pyperclip

TEXT = {"agree": """Yes, I agree that sounds fine to me.""",
        "busy": """Sorry, can we do this later this week or next week""",
        "upsell": """Would you consider making a monthly donation"""}

if len(sys.argv) < 2:
    print("Syntax: python mclip.py [keyphrase] - copy phrase text")
    sys.exit()
    
keyphrase = sys.argv[1] # first command line argument is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"TEXT for {keyphrase} copied to clipboard")
else:
    print("There is no text for {keyphrase}")
    

    
    