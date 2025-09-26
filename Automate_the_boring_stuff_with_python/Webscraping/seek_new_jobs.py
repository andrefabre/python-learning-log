"""
Load latest jobs on seek
"""
import webbrowser, sys

def main():
    
    while True:
        if len(sys.argv) <= 1:
            print("Syntax: options 'seek'")
            sys.exit()
        else: break
    
    if sys.argv[1].lower() == "seek":
        seek(sys.argv[1])


def seek(arg1):
    arg1 = webbrowser.open("https://seek.com.au/jobs/in-Perth-WA-6000?daterange=1&salaryrange=0-300000&salarytype=annual")

main()