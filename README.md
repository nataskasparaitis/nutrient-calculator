# Nutrient Calculator

A Python-based command-line tool to track and calculate nutritional intake (calories, protein, carbs, fat). It supports manual entry, file input, automatic nutrient lookup from a food database, and organized output with date-based folders.

## Features

* **Manual food entry**: Enter foods with name, mass, and any combination of nutrients (calories, protein, carbs, fat)
* **File input**: Read from `.txt` or `.csv` files
* **Automatic nutrient calculation**: If you only provide a name and mass (grams), the program looks up nutrients per 100g from a built-in database (`data/ingredients.txt`)
* **Smart parsing**: Handles abbreviations like `200cal`, `44p`, `30car`, `15f`, even multiple nutrients per line
* **Date-based organization**: Outputs are saved in the folder structure:

```text
output/YYYY/Month/Day/YYYY_Month_DD__HH_MM_SS.txt
```

Corresponding CSV logs are stored in:

```text
csv_data/YYYY/Month/Day/
```

* **Flexible output**: Print to screen only, or to both screen and file
* **CSV logging**: Every entry is automatically saved to a timestamped CSV file for later analysis
* **Error handling**: Clear error messages for invalid inputs, missing nutrients, or unrecognized foods

## Project Structure

```text
nutrient-calculator/
├── data/
│   └── ingredients.txt      # Food database (nutrients per 100g)
├── csv_data/                # Auto-generated CSV logs (date-based)
├── output/                  # Auto-generated TXT reports (date-based)
├── input/                   # Example input files (optional)
│   └── temp.txt
├── file_io.py               # CSV/TXT reading and writing
├── main.py                  # Main program entry point
├── nutrient_utils.py        # Nutrient calculation logic
├── string_utils.py          # String parsing helpers
├── ui.py                    # User input, date handling, directory creation
└── README.md
```

## Getting Started

### Prerequisites

* Python 3.6 or higher
* No external libraries required

Uses only Python's standard library:

* `csv`
* `os`
* `datetime`
* `time`

### Running the Program

```bash
python main.py
```

You will be guided through:

1. **Nutrient calculation mode**

   * Automatic nutrient lookup (name + mass only)
   * Manual nutrient entry

2. **Input method**

   * Manual entry
   * File input

3. **Output destination**

   * Screen only
   * Screen + file

4. **Report date**

   * Today's date
   * Custom date

## Usage Examples

### Manual Entry (Automatic Mode)

```text
> chicken 200g
> rice 150g
> (empty line to finish)
```

If `chicken` exists in `ingredients.txt`, the program automatically calculates nutrients based on the specified mass.

### Manual Entry (Full Manual Mode)

```text
> wrap 300cal 25p 40car 10f
> kefir 150cal 9p
> (empty line)
```

### File Input Example (`input/temp.txt`)

```text
330cal two caramel buns 8.25f
165cal lidl coffee 25abc
```

The parser extracts nutrient values from suffixes and correctly handles food names containing spaces.

## Output Example

### Console / TXT Report

```text
Today you ate:
coffee -g 85.0cal 0.0p -car -f
yogurt -g 150.0cal 3.3p -car -f
...

Total mass:      -
Total calories:  1912.0cal
Total protein:   148.6p
Total carbs:     -
Total fat:       -

1912,0cal 148,6p
```

### CSV Log

```csv
name,mass,calories,protein,carbs,fat
coffee,-,85.0,0.0,-,-
yogurt,-,150.0,3.3,-,-
...
```

## Completed Features

* Input can be name + any combination of `g`, `cal`, `p`, `car`, `f`
* Switched from parallel lists to a list of dictionaries

```python
[
    {"name": "...", "calories": "..."}
]
```

* Error message when invalid suffixes such as `100c` are entered
* Print totals of all provided nutrients
* Create directories based on date

```text
output/2026/april/11/
```

* Add entries using today's date or a custom date
* Save files with timestamped filenames

```text
2026_may_12__21_33_50.txt
```

* CSV logging for every entry

## Planned Features

* Change `"Today you ate:"` to `"In year/month/day you ate:"` when using custom dates
* Append to CSV instead of overwriting, then generate TXT reports from CSV
* Add support for multiple application modes (e.g. recipe builder)
* Generate statistics and reports:

  * Most calories
  * Most protein
  * Best calorie-to-protein ratio
  * Custom nutrient ratios
* Add or modify ingredients in `ingredients.txt`
* Create and manage recipes made from multiple ingredients
* Suggest recipes based on available ingredients

## How It Works

### Parsing

`string_utils.py` detects nutrient values such as:

```text
200cal
44p
30car
15f
```

and separates them from food names.

### Nutrient Lookup

When automatic mode is enabled, `calc_nutrients_by_weight()`:

1. Finds the food in `ingredients.txt`
2. Reads nutrient values per 100g
3. Calculates nutrients for the specified mass

### Totals

`calc_total_nutrients()` sums all numeric nutrient values across entries.

### File I/O

`file_io.py` handles:

* CSV reading/writing
* TXT report generation

CSV files use dictionaries for clean data organization.

### Date Handling

`ui.py` creates folder structures and filenames based on the selected date.

## Database Format (`data/ingredients.txt`)

Each line follows this format:

```text
name 100g {calories}cal {protein}p {carbs}car {fat}f
```

Example:

```text
chicken breast 100g 102cal 22p 0car 1,5f
butter 100g 743cal 0,6p 0,7car 82f
```

Commas are accepted as decimal separators and are automatically normalized.
