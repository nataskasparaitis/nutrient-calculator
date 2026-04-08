def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    

def split_line(line):
    items = []
    items.append("")
    for it in line.split(" "):
        if is_float(it.replace("cal", "")):
            items.insert(1, float(it.replace("cal", "")))
        elif is_float(it.replace("p", "")):
            items.insert(2, float(it.replace("p", "")))    
        else:
            items[0] += it + " "
    items[0] = items[0].strip()
    return items


def split_line_new(line):
    items = []
    item_types = ["name", "g", "cal", "p", "car", "f"]
    first_name_iteration = True
    for it in line.split(" "):
        if it.isnumeric():
            items = []
            return items
        elif it.isalpha():
            if first_name_iteration:
                items.insert(item_types.index("name"), it)
                first_name_iteration = False
            else:
                items[item_types.index("name")] += " " + it
            
        for type in item_types:
            if type == "name":
                continue
            elif is_float(it.replace(type, "")):
                items.insert(item_types.index(type), float(it.replace(type, "")))
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
            print(f"Invalid input: '{sline}'; must have at least one or more of: name {{number}}g/cal/p/car/f")
            continue

        for i in range(len(sline)):
            items[i].append(sline[i])
    return items


def calc_min_nutrients(items, total_cal, total_p):
    for i in items[1]:
        total_cal += i
    for i in items[2]:
        total_p += i
    return (total_cal, total_p)


def main():
    name = []
    calories = []
    protein = []
    items = (name, calories, protein)
    total_g = 0
    total_cal = 0
    total_p = 0
    total_car = 0
    total_f = 0


    temp = split_line_new("100g vistiena 100cal 1,5f 0car 22p")
    print(temp)
    input("Enter")

    items = text_calorie_calculator(items)
    total_cal, total_p = calc_min_nutrients(items, total_cal, total_p)

    t = f"Total: {total_cal:.1f}cal {total_p:.1f}p"
    print(t)
    print(t.replace(".", ","))

if __name__ == "__main__":
    main()

#modify so the input can be name g cal p car f; not all must be provided ✅
#print total of all nutrients provided
#add a option what to choose (nutrient text calculator, ...)
#add entries by date (choose: today, or enter date yourself)
#add print of a specific date (type in date, most cal, most p, best cal to p ratio, choose your own ratio)
#'add entry' 'modify entry' options that lets you add/modify the nutrients per 100g of a food in a data file
#'add recipe' 'modify recipe' that lets you add/modify a recipe thats made up of ingredients