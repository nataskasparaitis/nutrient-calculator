#   USED FOR ACTIONS WITH USER INPUT AND DATES 


import os
import datetime
from string_utils import convert_if_int


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
    

def enter_valid_date():
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
        date["year"] = now.strftime("%Y")
        date["month"] = now.strftime("%B")
        date["day"] = now.strftime("%d")
    elif date_choise == "2":
        date["year"], date["month"], date["day"] = enter_valid_date()
    return date


def convert_month_to_digit(month):
    month = month.lower()
    match month:
        case "january":
            return "1"
        case "february":
            return "2"
        case "march":
            return "3"
        case "april":
            return "4"
        case "may":
            return "5"
        case "june":
            return "6"
        case "july":
            return "7"
        case "august":
            return "8"
        case "september":
            return "9"
        case "october":
            return "10"
        case "november":
            return "11"
        case "december":
            return "12"
        case _:
            return month
        

def convert_digit_to_month(month):
    match month:
        case "1":
            return "January"
        case "2":
            return "February"
        case "3":
            return "March"
        case "4":
            return "April"
        case "5":
            return "May"
        case "6":
            return "June"
        case "7":
            return "July"
        case "8":
            return "August"
        case "9":
            return "September"
        case "10":
            return "October"
        case "11":
            return "November"
        case "12":
            return "December"
        case _:
            return month