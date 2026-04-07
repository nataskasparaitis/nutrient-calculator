def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    


def main():
    name = []
    calories = []
    protein = []
    items = (name, calories, protein)
    lc = 0      #line count
    total_cal = 0
    total_p = 0

    print("Enter the minimal calorie tracker that you have (name *cal *p): ")
    while True:
        line = input("> ")
        if line == "":
            break

        line = line.replace(",", ".")
        items[0].append("")

        for t in line.split(" "):
            if is_float(t.replace("cal", "")):
                items[1].append(t)
                items[1][lc] = float(items[1][lc].replace("cal", ""))
                total_cal += items[1][lc]

            elif is_float(t.replace("p", "")):
                items[2].append(t)
                items[2][lc] = float(items[2][lc].replace("p", ""))
                total_p += items[2][lc]
                
            else:
                items[0][lc] += t + " "

        items[0][lc] = items[0][lc].strip()
        lc += 1

    print(f"Total: {total_cal:.1f}cal {total_p:.1f}p")

if __name__ == "__main__":
    main()