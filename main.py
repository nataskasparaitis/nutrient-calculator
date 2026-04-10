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
    


def split_line(line):
    items = {"name": "-", "mass": "-", "calories": "-", "protein": "-", "carbs": "-", "fat": "-"}
    item_types = {"mass": "g", "calories": "cal", "protein": "p", "carbs": "car", "fat": "f"}   #if this line is used a lot maybe move to main and add as an argument to the function
    for it in line.split(" "):
        if it.isnumeric():
            print(f"Input Error: '{it}'; must have a valid nutrient abbreviation: {it}g/cal/p/car/f")
            items = {}
            return items
        elif is_digit_alpha(it):
            if not it.endswith(tuple(item_types.values())):
                print(f"Input Error: '{it}'; must have a valid nutrient abbreviation: {it.replace(strip_digits(it), "")}g/cal/p/car/f")
                items = {}
                return items
            else:   #add an if that checks if with the suffix removed the item is_digit_alpha (so this 1a0a0cal would print an error)
                for key, value in item_types.items():
                    if is_float(it.replace(value, "")) and items[key] == "-":
                        items.update({key: float(it.replace(value, ""))})
                    elif is_float(it.replace(value, "")) and is_float(items[key]):
                        items[key] += float(it.replace(value, ""))
        elif it.isalpha():
            if items["name"] == "-":
                items.update({"name": it})
            else:
                items["name"] += " " + it
    return items


def text_calorie_calculator(items):
    print("------- Minimal calorie calculator -------")
    print("Enter the 'name {number}g/cal/p/car/f' of a specific food (e.g: chicken 200cal 44p): ")
    while True:
        line = input("> ").lower()
        if line == "":
            break

        line = line.replace(",", ".")
        sline = split_line(line)
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


def main():
    items = []
    total = {"mass": "-", "calories": "-", "protein": "-", "carbs": "-", "fat": "-"}
    item_types = {"mass": "g", "calories": "cal", "protein": "p", "carbs": "car", "fat": "f"}

    items = text_calorie_calculator(items)
    total = calc_total_nutrients(items, total)

    print("Today you ate:")
    for i in items:
        for key, value in i.items():
            if key != "name":
                print(f"{value}{item_types[key]} ", end="")
            else:
                print(f"{value} ", end="")
        print()

    total_string = "\n"
    for key, value in total.items():
        if value == "-":
            total_string += f"Total {key + ":":<10} {value}\n"
        else:
            total_string += f"Total {key + ":":<10} {value}{item_types[key]}\n"

    print(total_string)
    print(f"{total["calories"]}cal {total["protein"]}p".replace(".", ","))

if __name__ == "__main__":
    main()

#modify so the input can be name g cal p car f; not all must be provided ✅
#switching from (name = [], calories = [], protein = []) to [{"name": }, {"calories": }, {"protein": }, ...] ✅
#make it so if 100c in input that would provide an error message ✅
#print total of all nutrients provided ✅
#add a option what to choose (nutrient text calculator, ...)
#add entries by date (choose: today, or enter date yourself)
#add print of a specific date (type in date, most cal, most p, best cal to p ratio, choose your own ratio)
#'add entry' 'modify entry' options that lets you add/modify the nutrients per 100g of a food in a data file
#'add recipe' 'modify recipe' that lets you add/modify a recipe thats made up of ingredients