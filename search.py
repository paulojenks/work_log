import os
import sys
import re
import csv

from Errors import InputError

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Search:
    def __init__(self):
        self.line = (re.compile(r'''
            ^(?P<date>(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})),  #date
            (?P<minutes>\d+),  #minutes
            (?P<task>[\w\s]*),  #task
            (?P<notes>[\w\s]+)?$ #notes
        ''', re.X|re.M))
        clear_screen()
        self.search_menu()


    def search_menu(self):
        """ Search Menu Options
        enter 'd' for search by date
        enter 'm' for search by minutes
        enter 'k' for search by keyword
        enter 'p' for search by pattern
        enter 'e' to exit the search menu
        """
        choice_prompt = "How would you like to search:\n"
        choice_prompt += "(D)ate\n"
        choice_prompt += "(M)inutes\n"
        choice_prompt += "(K)eyword\n"
        choice_prompt += "(P)attern\n"
        choice_prompt += "(E)xit to main menu\n"
        choices = ['d', 'm', 'k', 'p', 'e']
        while True:
            try:
                print(choice_prompt)
                choice = input(">>").lower()
                if choice not in choices:
                    raise InputError
            except InputError:
                if choice not in choices:
                    clear_screen()
                    print("Sorry, I didn't get that.")
            else:
                if choice == 'd':
                    self.date_search()
                elif choice == 'm':
                    self.minute_search()
                elif choice == 'k':
                    self.keyword_search()
                elif choice == 'p':
                    self.pattern_search()
                elif choice == 'e':
                    break


    def date_search(self):
        """ Searches log for DATE search terms given """
        search_pattern = input("Enter a date to search (YYYY-MM-DD)\n>>")
        line = self.line
        results = []

        with open("log.csv", newline='') as log_file:
            data = log_file.read()
            for match in line.finditer(data):
                if search_pattern in match.group('date'):
                    results.append('Date: {date} | '
                                    'Task: {task} | Minutes: {minutes} | '
                                    'Notes: {notes}'.format(**match.groupdict()))

        self.search_results(results)

    def minute_search(self):
        """ Searches log for MINUTE search terms given """
        search_pattern = input("Enter duration in minutes to search\n>>")
        line = self.line
        results = []

        with open("log.csv", newline='') as log_file:
            data = log_file.read()
            for match in line.finditer(data):
                if search_pattern in match.group('minutes'):
                    results.append('Date: {date} | '
                                    'Task: {task} | Minutes: {minutes} | '
                                    'Notes: {notes}'.format(**match.groupdict()))

        self.search_results(results)


    def keyword_search(self):
        """ Searches log for KEYWORD search terms given """
        search_pattern = re.compile("[" + input("Enter a keyword to search\n>>") + "]")
        line = self.line
        results = []
        with open("log.csv", newline='') as log_file:
            data = log_file.read()
            for match in line.finditer(data):
                if search_pattern.findall(match.group()):
                    results.append('Date: {date} | '
                                    'Task: {task} | Minutes: {minutes} | '
                                    'Notes: {notes}'.format(**match.groupdict()))

        self.search_results(results)


    def pattern_search(self):
        """ Search for REGEX pattern given """
        search_pattern = input("Enter a regex pattern to search\n>>")
        line = self.line
        search_pattern = re.compile(search_pattern)
        results = []
        with open("log.csv") as log_file:
            data = log_file.read()
            for match in line.finditer(data):
                if search_pattern.findall(match.group()):
                    results.append('Date: {date} | '
                                    'Task: {task} | Minutes: {minutes} | '
                                    'Notes: {notes}'.format(**match.groupdict()))

        self.search_results(results)


    def search_results(self, results):
        count = 1
        item = ''
        result_count = len(results)
        print('{} search results'.format(result_count))

        if result_count > 0:
            if len(results) == 1:
                for result in results:
                    print(str(count) + ') ' + result)
                    count += 1
            elif len(results) > 1:
                for result in results:
                    print(str(count) + ')' + result)
                    count += 1
                try:
                    result_choice = input("Enter the item number would you like to choose")
                    item += results[int(result_choice)-1]
                except IndexError:
                    print("Invalid Response")
                else:
                    item = item.replace(" | ", "\n").upper()
                    print(item)
        else:
            return 0
