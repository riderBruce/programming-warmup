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
        bool: True if the user enters yes, False if the user enters no.
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
    """
    Print on screen neatly with headers and data.

    Args:
        data (list of dict): Data set to print

    Returns:
        None
    """
    if not data:
        print("No data to display.")
        return

    headers = list(data[0].keys())
    print("\n" + "\t".join(h.ljust(12) for h in headers))
    print("-" * 100)
    for row in data:
        print("\t".join(str(v).ljust(12) for v in row.values()))


def read_csv_file(file_name):
    """
    Open a CSV file and read its content as a list of dictionary.

    Args:
        file_name (str): Path to the CSV file.

    Returns:
        List of dict: the CSV data
    """
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
    """
    Check the CSV file. If the file is not, make the header. And add new log to CSV file.

    Args:
        file_name (str): Path to the CSV file.
        data (dict): The log entry to save.

    Returns:
        None
    """
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
    """
    Overwrite whole data at the CSV file as a list of dict.

    Args:
        file_name (str): Path to the CSV file.
        data (list): Whole data to write on.
        headers (list): The data headers sit on the top of the CSV file.

    Returns:
        None
    """
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
    """
    Check the string is valid on datetime format.

    Args:
        datetime_str (str): The string for checking.
        format_str (str): Datetime usual format.

    Returns:
        bool: True if the datetime string is valid, False otherwise.
    """
    try:
        datetime.strptime(datetime_str, format_str)
        return True
    except ValueError:
        return False

