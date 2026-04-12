#   USED FOR READING AND WRITING


import csv
from string_utils import convert_if_float


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


def print_to_txt(items, total, file_name, item_types, mode):    #add try except
    text = ""
    with open(file_name, mode) as file:
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