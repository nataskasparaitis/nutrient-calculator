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