# Day 13 - Mini-Project: Logger with Timestamps

# Add a new log entry with a timestamp
# View all entries
# Filter logs by date or keyword
# Save to a file (e.g., my_log.csv or log.txt)

# Use datetime.datetime.now() for timestamps
# Store each log entry as a dictionary or list
# Use CSV or plain text
# Keep your functions small and reusable

# import
import csv
import datetime
import os

# Global variables
file_path = "my_log.csv"


# Reusable Methods
def select_a_number(prompt, start, end):
    while True:
        try:
            num = int(input(prompt + f"({start} ~ {end}) > "))
            if start <= num <= end:
                return num
            print(f"You selected a number out of range. Please select {start} ~ {end}.")
        except Exception as e:
            print(f"Invalid input. Please enter a number.")


def select_yes_or_no(prompt):
    while True:
        user_input = input(prompt + " (Y/N): ").lower()
        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please response with 'y' or 'n'.")


def read_csv_file(file_name):
    try:
        with open(file_name, newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error : The file {file_name} was not found.")
        return []
    except Exception as e:
        print(e)


def add_dict_to_csv(file_name, data: dict):
    try:
        if os.path.exists(file_path):
            with open(file_name, 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                input_data = data.values()
                csv_writer.writerow(input_data)
        else:
            with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                headers = data.keys()
                csv_writer.writerow(headers)
                input_data = data.values()
                csv_writer.writerow(input_data)
        # print(f"Successfully wrote {data.values()} to {file_name}.")
    except Exception as e:
        print(e)


def print_csv_data(data: [dict]):
    if not data:
        print("No data to display.")
        return

    headers = list(data[0].keys())
    print("\n" + "\t".join(h.ljust(12) for h in headers))
    print("-" * 50)
    for row in data:
        print("\t".join(str(v).ljust(12) for v in row.values()))
    print("\n")


# Basic Methods
def print_main_menus():
    print("Welcome to My Daily Logger!")
    print("1. View all logs")
    print("2. Add a new log")
    print("3. Search logs by keyword")
    print("4. Exit")


# Bridge Methods
def view_all_logs():
    data = read_csv_file(file_path)
    return print_csv_data(data)


def add_a_new_log():
    note = str(input(f"Input a note > "))
    log = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    each_data = {"Note": note, "Log": log}
    add_dict_to_csv(file_path, each_data)


def search_logs_by_keyword():
    data = read_csv_file(file_path)
    if len(data) == 0:
        return print(f"No Data to display. ")
    key = str(input(f"Input the keyword for searching... ")).lower()
    new_data = []
    for d in data:
        if key in str(d.values()).lower():
            new_data.append(d)
    print_csv_data(new_data)


# Main method
def main():
    print_main_menus()
    while True:
        order = select_a_number("Select a number. > ", 1, 4)
        if order == 1:
            view_all_logs()
        elif order == 2:
            add_a_new_log()
        elif order == 3:
            search_logs_by_keyword()
        elif order == 4:
            break
        else:
            print("Error : The logic might be fault.")


# Execution
main()
