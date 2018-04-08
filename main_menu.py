import os
import sys

from log import Log
from search import Search
from Errors import InputError


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class WorkLog:
    """ Main Menu for Adding to or Searching Worklog """
    def __init__(self):
        print('Welcome to The Log')
        self.menu()

    def menu(self):
        """ Menu Options
        enter 'e' for (E)ntry for log entry
        enter 's' for (S)earch for searching entries
        enter 'q' for (Q)uit for exiting the program
        """
        prompt = 'What would you like to do?\n'
        prompt += '- (E)ntry\n'
        prompt += '- (S)earch\n'
        prompt += '- (Q)uit\n'
        choices = ['e', 's', 'q']
        while True:
            try:
                print(prompt)
                choice = input('>').lower()
                if choice not in choices:
                    raise InputError
            except InputError:
                print("Invalid response!")
            else:
                if choice == 'e':
                    Log()
                elif choice == 's':
                    Search()
                elif choice == 'q':
                    break



WorkLog()
