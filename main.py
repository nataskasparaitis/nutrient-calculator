import csv
import os
import datetime
import time

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
    

def split_line(line, item_line, item_types):
    item = {}
    item.update(item_line)
    for it in line.split(" "):
        if it.isnumeric():
            print(f"Input Error: '{it}'; must have a valid nutrient abbreviation: {it}g/cal/p/car/f")
            item = {}
            return item
        elif is_digit_alpha(it):
            if not it.endswith(tuple(item_types.values())):
                print(f"Input Error: '{it}'; must have a valid nutrient abbreviation: {it.replace(strip_digits(it), "")}g/cal/p/car/f")
                item = {}
                return item
            else:   #add an if that checks if with the suffix removed the item is_digit_alpha (so this 1a0a0cal would print an error)
                for key, value in item_types.items():
                    if is_float(it.replace(value, "")) and item[key] == "-":
                        item.update({key: float(it.replace(value, ""))})
                    elif is_float(it.replace(value, "")) and is_float(item[key]):
                        item[key] += float(it.replace(value, ""))
        elif it.isalpha():
            if item["name"] == "-":
                item.update({"name": it})
            else:
                item["name"] += " " + it
    return item


def text_calorie_calculator(items, item, item_types):       #add input_choise; if 1 then the usual if 2 call read from txt which i have to make
    print("------- Minimal calorie calculator -------")
    print("Enter the 'name {number}g/cal/p/car/f' of a specific food (e.g: chicken 200cal 44p): ")
    while True:
        line = input("> ").lower()
        if line == "":
            break

        line = line.replace(",", ".")
        sline = {}
        sline.update(split_line(line, item, item_types))
        if len(sline) == 0:
            print(f"Try again")
            continue

        items.append(sline)
    return items


def calc_total_nutrients(items, total):
    for item in items:
        for key, value in item.items():
            if key == "name" or value == "-":
                continue
            elif total[key] == "-":
                total[key] = 0
            total[key] += value
    return total


def print_to_csv(items, path_to_file, mode):    #add try except
    with open(path_to_file, mode, newline='') as file:
        fieldnames = items[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(items)


def read_from_csv(path_to_file):
    with open(path_to_file, "r") as file:
        reader = csv.DictReader(file)
        items = []
        for row in reader:
            converted_row = {}
            for key, value in row.items():
                converted_row[key] = convert_if_float(value)
            items.append(converted_row)
    return items


def print_to_txt(items, total, path_to_file, item_types, mode):    #add try except
    text = ""
    with open(path_to_file, mode) as file:
        text += get_item_string(items, item_types)
        text += get_total_string(total, item_types)
        file.write(text)


def get_item_string(items, item_types):
    text = "Today you ate:\n"
    for i in items:
        for key, value in i.items():
            if key != "name":
                text += f"{value}{item_types[key]} "
            else:
                text += f"{value} "
        text += "\n"
    return text
    

def get_total_string(total, item_types):
    total_string = "\n"
    for key, value in total.items():
        if value == "-":
            total_string += f"Total {key + ":":<10} {value:}\n"
        else:
            total_string += f"Total {key + ":":<10} {value:.1f}{item_types[key]}\n"

    total_string += f"\n{total["calories"]}cal {total["protein"]:.1f}p".replace(".", ",")
    
    return total_string


def create_date_directories():
    pass


def get_date():
    year = 0
    month = input("Input the month: ")
    day = input("Input the day: ")
    while True:
        if year.isdigit() and year > 0:
            year = input("Input a valid year: ")
        #finish this

def convert_month(month):
    pass


def get_choise(choise_type):
    choises = ("1", "2")
    prompts = {"cache": "\nWould you like to use cached parameters:   \n1) yes   \n2) no   \n(type '1' or '2')   \n> ",
               "output": "\nWere would you like the calculated result to show:   \n1) to only the screen   \n2) to both screen and file   \n(type '1' or '2')  \n> ",
               "input": "\nHow would you like to provide the data:   \n1) Enter it yourself   \n2) provide a path to a file   \n(type '1' or '2')\n> "}
    
    i = input(prompts[choise_type])
    while True:
        if i not in choises:
            print(f"\nInvalid input: '{i}'; must be '1' or '2'")
            i = input("Try again   \n> ")
        else:
            break
    return i


def main():
    items = []
    item = {"name": "-", "mass": "-", "calories": "-", "protein": "-", "carbs": "-", "fat": "-"}
    item_types = {"mass": "g", "calories": "cal", "protein": "p", "carbs": "car", "fat": "f"}
    total = {}
    total.update(item)
    total.pop("name")
    csv_path = "csv_data/test.csv"
    txt_path = "output/test.txt"

    now = datetime.datetime.now()
    todays_date = {"year": now.strftime("%Y"), "month": now.strftime("%B"), "day": now.strftime("%d")}
    
    
    #cache_choise = get_choise("cache")
    #output_choise = get_choise("output")
    #input_choise = get_choise("input")

    #if output_choise == "1":
    #    items = text_calorie_calculator(items, item, item_types)

    


    #print(todays_date, type(todays_date))
    #input("Enter")

    #read from csv and print everything to txt and concole
    """items = read_from_csv(csv_path)
    total = calc_total_nutrients(items, total)
    print_to_txt(items, total, txt_path, item_types, "w")
    print(get_item_string(items, item_types))
    print(get_total_string(total, item_types))"""
    #input from console write to csv
    """items = text_calorie_calculator(items, item, item_types)
    print_to_csv(items, csv_path, "w")"""
    #input from console and print to concole and txt
    items = text_calorie_calculator(items, item, item_types)
    total = calc_total_nutrients(items, total)
    print_to_txt(items, total, txt_path, item_types, "w")
    print(get_item_string(items, item_types))
    print(get_total_string(total, item_types))


if __name__ == "__main__":
    main()

#modify so the input can be name g cal p car f; not all must be provided ✅
#switching from (name = [], calories = [], protein = []) to [{"name": , "calories": , "protein": }, ...] ✅
#make it so if 100c in input that would provide an error message ✅
#print total of all nutrients provided ✅
#create directories based on the current date: output/2026/april/11.txt
#add a option what to choose (nutrient text calculator, ...)
#add entries by date (choose: today, or enter date yourself)
#add print of a specific date (type in date, most cal, most p, best cal to p ratio, choose your own ratio)
#'add entry' 'modify entry' options that lets you add/modify the nutrients per 100g of a food in a data file
#'add recipe' 'modify recipe' that lets you add/modify a recipe thats made up of ingredients