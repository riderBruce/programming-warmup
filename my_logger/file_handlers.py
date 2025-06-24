from .utils import reusable_functions as reuse


def open_csv_file(path) -> list:
    """
    Open a CSV file and reads its content as a list of dictionaries.

    Args:
        path (str): Path to the CSV file.

    Returns:
        Tuple of (list of dict, list of str): The data and headers.
    """
    return reuse.read_csv_file(path)


def save_csv_file(path, new_data: dict) -> None:
    """
    Saves a new log entry to a CSV file.

    Args:
        path (str): Path to the CSV file.
        new_data (dict): The log entry to save.

    Returns:
        None
    """
    reuse.add_dict_to_csv(path, new_data)


def save_another_file(selected_data: [dict]) -> None:
    if len(selected_data) > 0:
        if reuse.select_yes_or_no("Save it to another file? "):
            new_file_name = str(input("Input a new file name : "))
            headers = [k for k in selected_data[0].keys()]
            reuse.overwrite_to_csv(new_file_name + '.csv', selected_data, headers)

