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
    nutrient_items = []
    item = {"name": "-", "mass": "-", "calories": "-", "protein": "-", "carbs": "-", "fat": "-"}
    item_types = {"mass": "g", "calories": "cal", "protein": "p", "carbs": "car", "fat": "f"}
    path_names = {"dir_year": "", "dir_month": "", "dir_day": "", "file_name": ""}
    total = {}
    total.update(item)
    total.pop("name")
    project_path = os.path.dirname(os.path.realpath(__file__))

    nutrient_items = read_from_txt(nutrient_items, item, "data/ingredients.txt", item_types)
    print(nutrient_items)
    #nutrient_calc_choise = get_choise("nutrient_calculation")
    #items = text_calorie_calculator(items, item, {"mass": "g"}, nutrient_calc_choise)
    #print(items)

    #cache_choise = get_choise("cache")
    print("----------------------------------")
    print("WELCOME TO THE NUTRIENT CALCULATOR")
    print("----------------------------------")

    #INPUT
    input_choise = get_choise("input")
    if input_choise == "1":
        items = text_calorie_calculator(items, item, item_types)
    elif input_choise == "2":
        input_file = input_valid_file(project_path)
        if input_file.endswith(".csv"):
            items = read_from_csv(input_file)
        elif input_file.endswith(".txt"):
            items = read_from_txt(items, item, input_file, item_types)

    total = calc_total_nutrients(items, total)
    text = get_item_string(items, item_types) + get_total_string(total, item_types) #print date instead of 'today you ate'

    #OUTPUT
    output_choise = get_choise("output")
    path_names.update(get_date(path_names, output_choise))
    csv_name = f"csv_data/{path_names["dir_year"]}/{path_names["dir_month"]}/{path_names["dir_day"]}/{path_names["file_name"]}.csv"
    csv_path = os.path.dirname(csv_name)
    create_dirs(csv_path)

    if output_choise == "1":
        print(text)
    elif output_choise == "2":
        txt_name = f"output/{path_names["dir_year"]}/{path_names["dir_month"]}/{path_names["dir_day"]}/{path_names["file_name"]}.txt"
        output_path = os.path.dirname(txt_name)
        create_dirs(output_path)
        print_to_txt(txt_name, text)
        print(text)

    print_to_csv(items, csv_name)



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
#add an 'available recepies' based on what ingredients you have