import os
import datetime
import re
import csv

from Errors import InputError


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



class Log:
    def __init__(self):
        self.log()

    def log(self):
        clear_screen()
        date = datetime.date.today()
        task = input('Task Title \n>>').lower()
        notes = input('Optional: Task Notes (Press enter to skip)\n>>').lower()
        while True:
            try:
                minutes = int(input('Task Length (in minutes)? \n>>'))
            except ValueError:
                print("Re-enter task length as integer")
            else:
                with open('log.csv', 'a') as log_file:
                    fieldnames = ['date', 'minutes', 'task', 'notes']
                    log_entry = csv.DictWriter(log_file, fieldnames = fieldnames)
                    log_entry.writerow({
                        'date':date,
                        'minutes': minutes,
                        'task': task,
                        'notes': notes
                    })
                break
