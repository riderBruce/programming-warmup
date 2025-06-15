## 📆 Day 11 – CSV Budget Tracker

A command-line tool that:

- Reads and parses CSV files using `csv.DictReader`
- Displays formatted tables of expenses
- Lets the user:
  - Filter data by fields (e.g., category or date)
  - Calculate total amounts from filtered data
  - Add new expense records interactively
  - Sort entries and overwrite the original CSV
- Saves results to `result.csv` for export

📁 Files:
- `budget.csv` – main data file
- `result.csv` – filtered export
- `day11_csv_budget.py` – main script

🛠️ Skills Practiced:
`csv`, file handling, data grouping, input validation, CLI menus, modular functions