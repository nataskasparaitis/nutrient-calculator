#   USED FOR ACTIONS WITH NUTRIENTS


from string_utils import is_digit_alpha, is_float, strip_digits


def split_input_line(line, item_line, item_types):
    item = {}
    item.update(item_line)
    type_string = ""
    for value in item_types.values():
        last_value = list(item_types.values())[-1]
        if value != last_value:
            type_string += f"{value}/"
        else:
            type_string += f"{value}"

    for it in line.split(" "):
        if is_float(it):
            print(f"Input Error: '{it}'; must have a valid nutrient abbreviation: {it}{type_string}")
            item = {}
            return item
        elif is_digit_alpha(it):
            if not it.endswith(tuple(item_types.values())):
                print(f"Input Error: '{it}'; must have a valid nutrient abbreviation: {it.replace(strip_digits(it), "")}{type_string}")
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


def text_calorie_calculator(items, item, item_types, nutrient_calc_choise="2"):
    print("------- Minimal calorie calculator -------")
    print("Enter the 'name {number}g/cal/p/car/f' of a specific food (e.g: chicken 200cal 44p): ")
    while True:
        line = input("> ").lower()
        if line == "":
            break

        line = line.replace(",", ".")
        sline = {}
        sline.update(split_input_line(line, item, item_types))
        if len(sline) == 0:
            print(f"Try again")
            continue
        elif nutrient_calc_choise == "1":
            if sline["name"] == "-" or sline["mass"] == "-":
                print(f"Input Error: {line}; must have a name and a mass    \nTry again")
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


def calc_nutrients_by_weight(items, nutrient_items):
    temp = {}
    temp.update({1: 2})

    for item in items:
        for ni in nutrient_items:
            multiplier = 0.0
            if item["name"] == ni["name"]:
                for key, value in item.items():
                    if key == "name":
                        continue
                    elif key == "mass":
                        multiplier = value / ni[key]
                    else:
                        item.update({key: ni[key] * multiplier})
                break
        if multiplier == 0:
            print(f"Item {item["name"]} is not in the list of available foods")