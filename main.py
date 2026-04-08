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


def text_calorie_calculator(items):
    print("------- Minimal calorie calculator -------")
    print("Enter the 'name {number}cal {number}p' of a specific food: ")
    while True:
        line = input("> ").lower()
        if line == "":
            break

        line = line.replace(",", ".")
        sline = split_line(line)
        if len(sline) < 3 or sline[0] == "":
            print(f"Invalid line: '{line}'; must have: 'name {{number}}cal {{number}}p'")
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
    total_cal = 0
    total_p = 0

    items = text_calorie_calculator(items)
    total_cal, total_p = calc_min_nutrients(items, total_cal, total_p)

    t = f"Total: {total_cal:.1f}cal {total_p:.1f}p"
    print(t)
    print(t.replace(".", ","))

if __name__ == "__main__":
    main()