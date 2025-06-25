from .utils import reusable_functions as reuse
from .input_handlers import get_log_input, get_key_input, get_date_input
from .file_handlers import save_csv_file, save_another_file


def add_data_in_memory(data: [dict], new_data: dict):
    """
    Add a new dictionary entry to an existing list of log entries (in-memory).

    Args:
        data (list of dict): The current list of log entries.
        new_data (dict): The new log entry to append.

    Returns:
        None
    """
    data.append(new_data)


def write_log(data: list, path) -> None:
    new_data = get_log_input()
    add_data_in_memory(data, new_data)
    save_csv_file(path, new_data)


def view_recent_logs(data) -> None:
    recent_num = reuse.select_a_number(f"How much logs do you want to see? ", 1, len(data))
    recent_data = data[recent_num * -1:]
    reuse.print_csv_data(recent_data)
    save_another_file(recent_data)


def search_logs_by_keyword(data) -> None:
    key = get_key_input()
    sorted_data = search_key(data, key)
    reuse.print_csv_data(sorted_data)
    save_another_file(sorted_data)


def search_tasks_by_date(data) -> None:
    key_date = get_date_input(reuse.is_valid_datetime)
    sorted_data = search_date(data, key_date)
    reuse.print_csv_data(sorted_data)
    save_another_file(sorted_data)


def search_key(data: [dict], key) -> [dict]:
    results = []
    try:
        for row in data:
            if any(key in v for v in row.values()):
                results.append(row)
    except Exception as e:
        print(e)
    return results


def search_date(data: [dict], key_date: str) -> [dict]:
    results = []
    try:
        for row in data:
            if row.get('date', 0) == key_date:
                results.append(row)
    except Exception as e:
        print(e)
    return results
