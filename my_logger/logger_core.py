# Day 15 - Logger

# Write short logs (like a journal or event tracker)
# Save them with a timestamp
# View or search past entries

# Create or open a log file : log.csv
# Allow the user to write a new log entry
# Each entry includes: date, time, and content
# View recent entries or search logs by keyword or date

# Add date-based filtering (like "logs from today")
# Add log categories (e.g., Mood, Task, Journal)

# imports
from .utils import reusable_functions as reuse
from datetime import datetime
import csv


# Global Variables
file_path = "log.csv"
csv_data_sample = [{"title": "noname",
                    "date": "YYYY-MM-DD",
                    "time": "HH:MM:SS",
                    "mood":"Good",
                    "task": "Go out",
                    "journal": "It's so good day to die."}]


# Basic functions
def print_main_menus():
    print("Select a menu.")
    print("1. Write log")
    print("2. View recent logs")
    print("3. Search logs by keyword")
    print("4. Search logs by date")
    print("5. Exit")


def get_log_input():
    title = str(input(f"Title : ")).lower()
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    mood = str(input(f"How are you today? (Mood) : "))
    task = str(input(f"Task : "))
    journal = str(input(f"Journal : "))
    each_data = {"title": title,
                 "date": date,
                 "time": time,
                 "mood": mood,
                 "task": task,
                 "journal": journal}
    return each_data


def add_data_in_memory(data: [dict], new_data: dict):
    data.append(new_data)


def save_csv_file(path, new_data: dict):
    reuse.add_dict_to_csv(path, new_data)


def save_another_file(selected_data: [dict]):
    if len(selected_data) > 0:
        if reuse.select_yes_or_no("Save it to another file? "):
            new_file_name = str(input("Input a new file name : "))
            headers = [k for k in selected_data[0].keys()]
            reuse.overwrite_to_csv(new_file_name + '.csv', selected_data, headers)


def get_key_input():
    return str(input(f"Please input a key for searching > "))


def search_key(data: [dict], key):
    results = []
    try:
        for row in data:
            for v in row.values():
                if key in v:
                    results.append(row)
    except Exception as e:
        print(e)
    return results


def get_date_input():
    while True:
        datetime_str = str(input(f"Please input a date like 2025-06-19 > "))
        format_str = "%Y-%m-%d"
        if reuse.is_valid_datetime(datetime_str, format_str):
            break
    return datetime_str


def search_date(data: [dict], key_date: str):
    results = []
    try:
        for row in data:
            if key_date == row['date']:
                results.append(row)
    except Exception as e:
        print(e)
    return results


# Bridge functions
def open_csv_file(path):
    return reuse.read_csv_file(path)


def write_log(data: list, path):
    new_data = get_log_input()
    add_data_in_memory(data, new_data)
    save_csv_file(path, new_data)


def view_recent_logs(data):
    recent_num = reuse.select_a_number(f"How much logs do you want to see? ", 1, len(data))
    recent_data = data[recent_num * -1:]
    reuse.print_csv_data(recent_data)
    save_another_file(recent_data)


def search_logs_by_keyword(data):
    key = get_key_input()
    sorted_data = search_key(data, key)
    reuse.print_csv_data(sorted_data)
    save_another_file(sorted_data)


def search_tasks_by_date(data):
    key_date = get_date_input()
    sorted_data = search_date(data, key_date)
    reuse.print_csv_data(sorted_data)
    save_another_file(sorted_data)


# Main function
def main():
    print("Welcome to My Logger CLI Tool!")
    while True:
        print_main_menus()
        data = open_csv_file(file_path)
        num = reuse.select_a_number(" > ", 1, 5)
        if num == 1:
            write_log(data, file_path)
        elif num == 2:
            view_recent_logs(data)
        elif num == 3:
            search_logs_by_keyword(data)
        elif num == 4:
            search_tasks_by_date(data)
        elif num == 5:
            break
        else:
            print("Logic problem occur.")


# Execution
main()
