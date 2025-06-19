import csv
import os
from datetime import datetime


# Reusable Functions

def select_a_number(prompt: str, start: int, end: int):
    """
    Ask the user to enter a number between `start` and `end`.

    Parameters:
        prompt (str): The text shown to the user.
        start (int): The minimum acceptable value.
        end (int): The maximum acceptable value.
    Returns:
        int: A valid number entered by the user between start and end.
    """
    while True:
        try:
            num = int(input(prompt + f"({start} ~ {end}) > "))
            if start <= num <= end:
                return num
            print(f"You selected a number out of range. Please select {start} ~ {end}.")
        except Exception as e:
            print(f"Invalid input. Please enter a number.")


def select_yes_or_no(prompt: str):
    """
    Ask the user to enter yes or no and validate the response.

    Parameters:
        prompt (str): The text shown to the user.

    Returns:
        bool: True if the user enters yes, False if the user enter no.
    """
    while True:
        user_input = input(prompt + " (Y/N): ").lower()
        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please response with 'y' or 'n'.")


def print_csv_data(data: [dict]):
    if not data:
        print("No data to display.")
        return

    headers = list(data[0].keys())
    print("\n" + "\t".join(h.ljust(12) for h in headers))
    print("-" * 100)
    for row in data:
        print("\t".join(str(v).ljust(12) for v in row.values()))


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
        if os.path.exists(file_name):
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


def overwrite_to_csv(file_name, data: list, headers: list):
    try:
        with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            # dict to list
            input_data = []
            for d in data:
                each_rows = []
                for h in headers:
                    each_rows.append(d[h])
                input_data.append(each_rows)
            # write on
            csv_writer.writerow(headers)
            csv_writer.writerows(input_data)
            print(f"Successfully overwrote to {file_name}.")
            return
    except FileNotFoundError:
        print(f"Error : The file {file_name} was not found.")
    except Exception as e:
        print(e)


def is_valid_datetime(datetime_str, format_str):
    try:
        datetime.strptime(datetime_str, format_str)
        return True
    except ValueError:
        return False

