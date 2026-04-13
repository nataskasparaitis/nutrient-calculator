#   USED FOR ACTIONS WITH USER INPUT AND DATES 


import os
import datetime
from string_utils import convert_if_int, convert_month_to_digit, convert_digit_to_month


def get_choise(choise_type):
    choises = ("1", "2")
    #   COULD ADD A LIST OF DICTIONARIES THAT ALL HAVE THEIR PRINT AND ERROR MESSAGES
    prompts = {"cache": "\nWould you like to use cached parameters:    \n1) Yes    \n2) No    \n\n> ",
               "output": "\nWere would you like the calculated result to show:    \n1) only to the screen    \n2) to both screen and file    \n\n> ",
               "input": "\nHow would you like to provide the data:    \n1) Enter it yourself    \n2) Provide a path to a file    \n\n> ",
               "date": "\nWould you like to use the current date for the output?    \n1) Yes    \n2) No, I would like to enter my own date    \n\n> "
               }
    
    i = input(prompts[choise_type])
    while True:
        if i not in choises:
            print(f"\nInvalid input: {i}; must be {choises}")
            i = input("Try again   \n> ")
        else:
            break
    return i


def create_dirs(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def valid_date(year=1, month=1, day=1):
    try:
        datetime.date(year, month, day)
        return True
    except ValueError, TypeError:   #TypeError if str not int
        return False
    

def input_valid_date():
    while True:
        year = input("Input the year:   \n> ")
        month = input("Input the month:   \n> ")
        month = convert_month_to_digit(month)
        day = input("Input the day:   \n> ")
        if not valid_date(convert_if_int(year), convert_if_int(month), convert_if_int(day)):
            print(f"\nInput error: {year}/{month}/{day}; not a valid date, try again:")
            continue
        else:
            month = convert_digit_to_month(month)
            return (year, month, day)


def get_date(date_dict):
    date = {}
    date.update(date_dict)
    now = datetime.datetime.now()
    date_choise = get_choise("date")
    if date_choise == "1":
        date["dir_year"] = now.strftime("%Y")
        date["dir_month"] = now.strftime("%B")
        date["dir_day"] = now.strftime("%d")
        date["file_name"] = now.strftime("%H_%M_%S")
    elif date_choise == "2":
        date["dir_year"], date["dir_month"], date["dir_day"] = input_valid_date()
        date["file_name"] = now.strftime("%Y_%B_%d__%H_%M_%S")
    return date


def input_valid_file(proj_path):
    end = (".csv", ".txt")
    file = input(f"\nEnter a valid .csv or .txt file for input (with its path if its not in {proj_path}):   \n> ")
    while True:
        if not os.path.exists(file):
            print(f"\nInput Error: {file}; must be a valid file")
            file = input("Try again:    \n> ")
            continue
        elif not file.endswith(end):
            print(f"\nInput Error: {file}; must be a .csv or .txt file")
            file = input("Try again:    \n> ")
        else:
            return file
