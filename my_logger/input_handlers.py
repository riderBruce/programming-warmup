from datetime import datetime


def get_log_input() -> dict:
    title = str(input(f"Title : ")).lower()
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    mood = input(f"How are you today? (Mood) : ")
    task = input(f"Task : ")
    journal = input(f"Journal : ")

    return {
        "title": title,
         "date": date,
         "time": time,
         "mood": mood,
         "task": task,
         "journal": journal
    }


def get_key_input() -> str:
    return input(f"Please input a key for searching > ")


def get_date_input(is_valid_datetime_func) -> str:
    while True:
        datetime_str = input(f"Please input a date like 2025-06-19 > ")
        if is_valid_datetime_func(datetime_str, "%Y-%m-%d"):
            return datetime_str


