import csv
import os
import datetime
import time
from string_utils import is_float, is_digit_alpha, strip_digits, convert_if_float, convert_if_int
from nutrient_utils import text_calorie_calculator, calc_total_nutrients
from file_io import print_to_csv, read_from_csv, print_to_txt, get_item_string, get_total_string
from ui import get_choise, create_dirs, valid_date, enter_valid_date, get_date


def main():
    items = []
    item = {"name": "-", "mass": "-", "calories": "-", "protein": "-", "carbs": "-", "fat": "-"}
    item_types = {"mass": "g", "calories": "cal", "protein": "p", "carbs": "car", "fat": "f"}
    date = {"year": "", "month": "", "day": ""}
    total = {}
    total.update(item)
    total.pop("name")
    output_path = "output"
    csv_path = "csv_data"
    project_path = os.path.dirname(os.path.realpath(__file__))
    
    date.update(get_date(date))

    output_path += f"/{date["year"]}/{date["month"]}"
    txt_name = output_path + "/" + date["day"] + ".txt"
    csv_path += f"/{date["year"]}/{date["month"]}"
    csv_name = csv_path + "/" + date["day"] + ".csv"
    create_dirs(output_path)
    create_dirs(csv_path)
    
    items = text_calorie_calculator(items, item, item_types)
    total = calc_total_nutrients(items, total)
    print_to_txt(items, total, txt_name, item_types, "w")
    print_to_csv(items, csv_name, "w")
    print(get_item_string(items, item_types))
    print(get_total_string(total, item_types))
    

    #create_dirs(f"{output_path}/{date["year"]}/{date["month"]}")
    #with open(date["day"] + ".txt", "w"):
    #    pass
    
    #cache_choise = get_choise("cache")
    #output_choise = get_choise("output")
    #input_choise = get_choise("input")

    #if output_choise == "1":
    #    items = text_calorie_calculator(items, item, item_types)


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
    """items = text_calorie_calculator(items, item, item_types)
    total = calc_total_nutrients(items, total)
    print_to_txt(items, total, txt_path, item_types, "w")
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
#make it so if the user types in a date it would save in: output/2000/january/1/2026_may_12__21_33_50.txt if use current date: 2026/may/12/21_33_50.txt
#add a option what to choose (nutrient text calculator, ...)
#add print of a specific date (type in date, most cal, most p, best cal to p ratio, choose your own ratio)
#'add entry' 'modify entry' options that lets you add/modify the nutrients per 100g of a food in a data file
#'add recipe' 'modify recipe' that lets you add/modify a recipe thats made up of ingredients