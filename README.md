# Car Price and Mileage Analyzer

#### Video Demo: https://www.youtube.com/watch?v=qtnpUiwR5cE

#### Description:

This Python project is called **Car Price and Mileage Analyzer**. It processes a CSV file of car data to suggest a color based on the car’s year and estimate the mileage based on its price.

The program reads a CSV with columns like `name`, `year`, and `price`, applies business rules, and generates a new CSV file with `name`, `colour`, and `expected_mileage`.

### Files in this Project:

- `project.py`: Contains `main()` and 3 functions:
  - `check_correct_args()`: Validates arguments.
  - `select_colour(year)`: Suggests a color based on year.
  - `select_mileage_from_price(price_str)`: Estimates mileage from price.

- `test_project.py`: Unit tests for the above functions using `pytest`.

- `requirements.txt`: Lists `pytest` as a dependency.

This project strengthened my skills in file I/O, error handling, and test-driven development. I chose this problem to simulate real-world data processing and provide actionable insights from raw CSV data.
