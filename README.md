# Car Price and Mileage Analyzer

#### Video Demo: https://www.youtube.com/watch?v=qtnpUiwR5cE

#### Description:

This Python project, **Car Price and Mileage Analyzer**, is designed to process raw CSV data about used cars and provide helpful insights such as estimated mileage and suggested color options based on the year of manufacture. It reads an input file containing a list of cars, performs logic-based enhancements, and then generates a new output file in CSV format.

The program simulates a basic data enrichment task that car dealerships or analysts might perform. Given the car’s name, year, and price, it suggests a color (based on the year) and estimates mileage based on the price. This can help customers or sales staff quickly gauge car quality and appearance without manual calculation or assumptions.

---

### How It Works

The program runs from the command line and expects two arguments:
1. The name of the input CSV file
2. The name of the output CSV file to generate

It uses `csv.DictReader` to parse rows from the input file, applies logic through two functions: `select_colour()` and `select_mileage_from_price()`, and writes the enhanced data to a new file using `csv.DictWriter`.

Each row in the output includes:
- `name`: the car’s name
- `colour`: a suggested paint color based on the year
- `expected_mileage`: a rough mileage estimate based on the price

The logic is simple:
- Cars from 2016–2017 → `"White"`
- Cars from 2018–2019 → `"Pearl_white"`
- Other years → `"None"`

If a car’s price is above 2 million (`"2.0M"` or more), it is assumed to have `"Below 50,000 km"` mileage. Otherwise, it returns `"Above 50,000 km"`.

---

### Files Included

- `project.py`: The main Python file. Contains the `main()` function, plus three custom functions:
  - `check_correct_args()` — validates command-line arguments
  - `select_colour()` — maps years to suggested colors
  - `select_mileage_from_price()` — estimates mileage from price

- `test_project.py`: Contains unit tests for all the custom functions using `pytest`. Tests include:
  - Missing arguments
  - Expected outputs for known inputs
  - Edge cases for years and prices

- `requirements.txt`: Lists the single required external dependency (`pytest`) to run the tests.

- `README.md`: This file.

---

### Design Decisions

This project intentionally focuses on clear, readable Python code with testability and error handling. The color and mileage logic is simplified but realistic for small data applications. I chose not to use classes to keep it procedural and beginner-friendly.

I also added input validation to ensure only proper CSV files are accepted, and the program fails gracefully when the file is not found or the price format is invalid.

This project helped me reinforce how to:
- Work with CSV data using Python
- Write modular, testable functions
- Use `pytest` for automated testing
- Apply logic and data processing in real-world scenarios

---

### Future Improvements

With more time, I would improve the mileage estimation logic by incorporating more variables, such as car make or fuel type. I could also develop a GUI using Tkinter or a web interface with Flask to make it more user-friendly for non-programmers.
