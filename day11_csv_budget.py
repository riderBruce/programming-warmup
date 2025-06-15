# Day 11 CSV Budget Tracker

# Reading CSV files using csv.reader()
# Handling rows and headers
# Calculating totals (e.g., expenses)
# Light string/number processing

# Show all records (nicely formatted)
# Sum all expenses
# Group by category and show totals
# Add filtering (e.g., "Show only Food expenses")
# Allow user to add a new expense and write back to the file

# import
import csv

# Global variables
file_path = "budget.csv"
result_path = "result.csv"


# Reusable methods
def read_from_csv(file_name):
    try:
        with open(file_name, newline='') as file:
            reader = csv.DictReader(file)
            data = []
            headers = list(reader.fieldnames)
            for row in reader:
                # print(f"{row}")
                data.append(row)
            return data, headers
    except FileNotFoundError:
        print(f"Error : The file {file_name} was not found.")
    except Exception as e:
        print(e)


def add_dict_to_csv(file_name, data: dict):
    try:
        with open(file_name, 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            input_data = data.values()
            csv_writer.writerow(input_data)
            print(f"Successfully wrote {data} to {file_name}.")
            return
    except FileNotFoundError:
        print(f"Error : The file {file_name} was not found.")
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


def choose_a_number(prompt, start, end):
    while True:
        try:
            num = int(input(prompt + f"({start} ~ {end}) > "))
            if start <= num <= end:
                return num
            print(f"You selected a number out of range. Please select {start} ~ {end}.")
        except Exception as e:
            print(f"Invalid input. Please enter a number.")


def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt + " (Y/N): ").lower()
        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please response with 'y' or 'n'.")


def print_dict_csv_data(data):
    if not data:
        print("No data to display.")
        return

    headers = list(data[0].keys())
    print("\n" + "\t".join(h.ljust(12) for h in headers))
    print("-" * 50)
    for row in data:
        print("\t".join(str(v).ljust(12) for v in row.values()))


# Basic methods
def select_a_name(prompt: str, data: list):
    print("-" * 30)
    for n, f in enumerate(data):
        print(f"{n + 1} : {f}")
    print("-" * 30)
    num = choose_a_number(prompt, 1, len(data))
    return data[num - 1]


def get_a_list_of_values_by_param(data: list, param):
    value_set = set()
    for row in data:
        value_set.add(row[param])
    value_list = list(value_set)

    # if field data are float
    try:
        value_list = [float(v) for v in value_list]
    except Exception as e:
        pass

    value_list.sort()
    return value_list


def group_by_field_name(data: list, field: str):
    value_list = get_a_list_of_values_by_param(data, field)
    selected = select_a_name("Which data do you want to check? ", value_list)
    selected_rows = []
    for row in data:
        if row[field] == selected:
            selected_rows.append(row)
    print_dict_csv_data(selected_rows)
    return selected_rows


def sort_by_param(data: list, param: str):
    value_list = get_a_list_of_values_by_param(data, param)
    new_data = []
    for v in value_list:
        for d in data:
            if param == 'Amount':
                if v == float(d[param]):
                    new_data.append(d)
            else:
                if v == d[param]:
                    new_data.append(d)
    return new_data


def sum_amount(data):
    total = 0.0
    for row in data:
        total += float(row['Amount'])
    print("-" * 30)
    print(f"Selected item's total : {total}")
    print("-" * 30)
    return total


def put_in_new_data(file_path, headers):
    data = {}
    for h in headers:
        value = input(f"{h} : ")
        data[h] = value.lower() if h != 'Amount' else value
    add_dict_to_csv(file_path, data)


# Main handler
def main():

    while True:
        data, headers = read_from_csv(file_path)
        if get_yes_no_input("Do you want to put it new data? > "):
            put_in_new_data(file_path, headers)
            continue

        if len(data) == 0:
            print(f"There's no data.")
            continue
        if get_yes_no_input("Do you want to sort all data and overwrite? > "):
            param = select_a_name("What do you want to sort by? > ", ['Date', 'Amount'])
            data = sort_by_param(data, param)
            overwrite_to_csv(file_path, data, headers)

        # data check
        field = select_a_name("Which field do you want to check? > ", headers)
        selected_rows = group_by_field_name(data, field)
        overwrite_to_csv(result_path, selected_rows, headers)
        sum_amount(selected_rows)

        if get_yes_no_input("Do you want to quit? > "):
            break


# Execution
main()

