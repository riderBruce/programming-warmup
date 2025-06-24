# imports
from .utils import reusable_functions as reuse
from .input_handlers import get_log_input, get_date_input, get_key_input
from .file_handlers import open_csv_file, save_csv_file, save_another_file
from .log_actions import write_log, view_recent_logs, search_logs_by_keyword, search_tasks_by_date
from .menu import print_main_menus


# Global Variables
file_path = "log.csv"
csv_data_sample = [{"title": "noname",
                    "date": "YYYY-MM-DD",
                    "time": "HH:MM:SS",
                    "mood":"Good",
                    "task": "Go out",
                    "journal": "It's so good day to die."}]


# Main function
def main() -> None:
    """
    Control all menus and handle the process.
    """
    print("Welcome to My Logger CLI Tool!")
    while True:
        print_main_menus()
        data = open_csv_file(file_path)
        num = reuse.select_a_number(" > ", 1, 5)
        actions = {
            1: lambda: write_log(data, file_path),
            2: lambda: view_recent_logs(data),
            3: lambda: search_logs_by_keyword(data),
            4: lambda: search_tasks_by_date(data),
            5: lambda: exit()
        }
        actions.get(num, lambda: print("Logic problem occur."))()
