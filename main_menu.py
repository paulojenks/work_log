import os
import sys

from log import Log
from search import Search


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class WorkLog:
    def __init__(self):
        print('Welcome to The Log')
        self.menu()

    def menu(self):
        prompt = 'What would you like to do?\n'
        prompt += '- (E)ntry\n'
        prompt += '- (S)earch\n'
        prompt += '- (Q)uit\n'
        while True:
            try:
                print(prompt)
                choice = input('>').lower()
            except ValueError:
                print("Invalid response!")
            else:
                if choice == 'e':
                    Log()
                elif choice == 's':
                    Search()
                elif choice == 'q':
                    break



WorkLog()
