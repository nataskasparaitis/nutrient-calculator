#   USED FOR ACTIONS WITH STRINGS


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    

def is_digit_alpha(string):
    digit_count = 0
    alpha_count = 0
    for c in string:
        if c.isdigit():
            digit_count += 1
        elif c.isalpha():
            alpha_count += 1
    if digit_count > 0 and alpha_count > 0:
        return True
    else:
        return False
    

def strip_digits(string):
    new = ""
    for c in string:
        if not c.isdigit():
            new += c
    return new


def strip_alpha(string):
    new = ""
    for c in string:
        if not c.isalpha():
            new += c
    return new


def convert_if_float(string):
    try:
        return float(string)
    except ValueError:
        return string
    

def convert_if_int(string):
    try:
        return int(string)
    except ValueError:
        return string


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