import csv
import os
import datetime
import time
from string_utils import is_float, is_digit_alpha, strip_digits, convert_if_float, convert_if_int
from nutrient_utils import text_calorie_calculator, calc_total_nutrients
from file_io import print_to_csv, read_from_csv, print_to_txt, get_item_string, get_total_string, read_from_txt
from ui import get_choise, create_dirs, valid_date, input_valid_date, get_date, input_valid_file


def main():
    items = []
    item = {"name": "-", "mass": "-", "calories": "-", "protein": "-", "carbs": "-", "fat": "-"}
    item_types = {"mass": "g", "calories": "cal", "protein": "p", "carbs": "car", "fat": "f"}
    path_names = {"dir_year": "", "dir_month": "", "dir_day": "", "file_name": ""}
    total = {}
    total.update(item)
    total.pop("name")
    project_path = os.path.dirname(os.path.realpath(__file__))
    


    
    #cache_choise = get_choise("cache")
    """print("----------------------------------")
    print("WELCOME TO THE NUTRIENT CALCULATOR")
    print("----------------------------------")
    input_choise = get_choise("input")
    output_choise = get_choise("output")"""





    """#if provide input file
    input_file = input_valid_file(project_path)
    items = read_from_txt(items, item, input_file, item_types)
    print(items)"""

    """
    #if dont print to txt file get current date for csv
    path_names.update(get_date(path_names))

    #if print to txt
    output_path = f"output/{path_names["dir_year"]}/{path_names["dir_month"]}/{path_names["dir_day"]}"
    txt_name = output_path + "/" + path_names["file_name"] + ".txt"
    create_dirs(output_path)

    #always
    csv_path = f"csv_data/{path_names["dir_year"]}/{path_names["dir_month"]}/{path_names["dir_day"]}"
    csv_name = csv_path + "/" + path_names["file_name"] + ".csv"
    create_dirs(csv_path)
    
    #if input from console
    items = text_calorie_calculator(items, item, item_types)

    #always
    total = calc_total_nutrients(items, total)

    #if print to txt file
    text = get_item_string(items, item_types) + get_total_string(total, item_types)
    print_to_txt(txt_name, text)

    #always for printing logs to csv
    print_to_csv(items, csv_name)

    #always for printing to screen
    print(get_item_string(items, item_types))
    print(get_total_string(total, item_types))"""


    #read from csv and print everything to txt and concole
    """items = read_from_csv(csv_path)
    total = calc_total_nutrients(items, total)
    text = get_item_string(items, item_types) + get_total_string(total, item_types)
    print_to_txt(txt_name, text)
    print(get_item_string(items, item_types))
    print(get_total_string(total, item_types))"""
    #input from console write to csv
    """items = text_calorie_calculator(items, item, item_types)
    print_to_csv(items, csv_path)"""
    #input from console and print to concole and txt
    """items = text_calorie_calculator(items, item, item_types)
    total = calc_total_nutrients(items, total)
    text = get_item_string(items, item_types) + get_total_string(total, item_types)
    print_to_txt(txt_name, text)
    print(get_item_string(items, item_types))
    print(get_total_string(total, item_types))"""


if __name__ == "__main__":
    main()

#modify so the input can be name g cal p car f; not all must be provided ✅
#switching from (name = [], calories = [], protein = []) to [{"name": , "calories": , "protein": }, ...] ✅
#make it so if 100c in input that would provide an error message ✅
#print total of all nutrients provided ✅
#create directories based on the current date: output/2026/april/11.txt ✅
#add entries by date (choose: today, or enter date yourself) ✅
#make it so if the user types in a date it would save in: output/2000/january/1/2026_may_12__21_33_50.txt if use current date: 2026/may/12/21_33_50.txt ✅

#in print_to_txt change "Today you ate: " to "In year/month/day you ate: "

#make it so if the user wants info appended, it should be appended in .csv file, then converted from csv to txt
#add a option what to choose (nutrient text calculator, ...)
#add print of a specific date (type in date, most cal, most p, best cal to p ratio, choose your own ratio)
#'add entry' 'modify entry' options that lets you add/modify the nutrients per 100g of a food in a data file
#'add recipe' 'modify recipe' that lets you add/modify a recipe thats made up of ingredients