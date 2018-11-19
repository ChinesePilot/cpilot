from app import app, variable
import sys
from termcolor import colored, cprint

if __name__ == "__main__":
    cprint('CPILOT RUNNING...', 'green', 'on_red')
    #print(colored('CPILOT RUNNING...', 'green'))
    app.run()