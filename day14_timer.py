# Day 14 - Timer & Reminder Tool (CLI App)


# import
import time
from datetime import datetime, timedelta
import resuable_functions as reuse
import os
import subprocess
import threading

# Global Variables
file_path = "Non, Je Ne Regrett Rien.mp3"
scheduler = []
# Store the process object
afplay_process = None


# Reusable Functions
def play_sound_async(file_path):
    global afplay_process
    if not os.path.exists(file_path):
        print(f"Sound file not found at {file_path}")
        return
    try:
        afplay_process = subprocess.Popen(["afplay", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Playing Sound : {file_path} (PID: {afplay_process.pid})")
    except FileNotFoundError:
        print("Error: 'afplay' command not found. Make sure you are on macOS and afplay is in your PATH.")
    except Exception as e:
        print(f"An error occurred while trying to play sound: {e}")


def play_song(path):
    if not os.path.exists(path):
        print(f"No Audio file. Just beep if no file given.")
    try:
        subprocess.run(["afplay", path], check=True)
        print("Sound played (macOS).")
    except FileNotFoundError:
        print("Error: 'afplay' command not found. (This is a macOS command)")
    except subprocess.CalledProcessError as e:
        print(f"Error playing sound: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def stop_sound():
    global afplay_process
    if afplay_process and afplay_process.poll() is None:
        print(f"Stopping Sound (PID:{afplay_process.pid})...")
        afplay_process.terminate()
        afplay_process.wait(timeout=5)
        if afplay_process.poll() is not None:
            print(f"Sound Stopped.")
        else:
            print(f"Warning : Sound Process did not terminate gracefully.")
            afplay_process.kill()
            afplay_process.wait()
            print(f"Sound forcefully stopped.")
    elif afplay_process:
        print(f"Sound was already stopped or finished.")
    else:
        print(f"No sound is currently playing via afplay to stop.")


def play_and_stop_song_by_input(path):
    play_sound_async(path)
    input("Stop with any input. > ")
    stop_sound()


def is_valid_datetime(datetime_str, format_str):
    try:
        datetime.strptime(datetime_str, format_str)
        return True
    except ValueError:
        return False


def is_future_date(timestamp: datetime, now: datetime):
    return True if timestamp > now else False


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


# Bridge Functions
def print_main_menus():
    print("\n")
    print(f"Welcome to Timer & Reminder")
    print(f"1. Start a countdown timer")
    print(f"2. Schedule a reminder")
    print(f"3. View current reminders")
    print(f"4. Exit")


def start_a_countdown_timer():
    minutes_count = reuse.select_a_number("Select minutes. > ", 0, 1000)
    seconds_count = reuse.select_a_number("Select seconds. > ", 0, 59)
    total_seconds = minutes_count * 60 + seconds_count
    for i in range(total_seconds, 1, -1):
        minutes_remain, seconds_remain = divmod(i, 60)
        print(f"Count Down > {'{:02}'.format(minutes_remain)}:{'{:02}'.format(seconds_remain)}")
        time.sleep(1)
    print(f"⏰ Time's up!")
    play_and_stop_song_by_input(file_path)


def remind_schedule():
    while True:
        input_time = str(input(f"Set future time stamp like 2025-06-18 15:00 > "))
        format_str = "%Y-%m-%d %H:%M"
        if not is_valid_datetime(input_time, format_str):
            print(f"{input_time} is not match this format {format_str}. ")
            continue
        timestamp = datetime.strptime(input_time, format_str)
        now = datetime.now()
        if not is_future_date(timestamp, now):
            print(f"{input_time} is not future. ")
            continue
        break
    message = str(input(f"Input a note > "))
    data = {"timestamp": timestamp, "message": message}
    scheduler.append(data)
    check_regularly(data)


def check_regularly(data):
    while True:
        time_left = data['timestamp'] - datetime.now()
        if time_left.days < 0:
            break
        days = time_left.days
        remain_seconds = time_left.seconds
        hours, remainder = divmod(remain_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time.sleep(3)
        print(f"{data['message']} : Timestamp remains {days} days, {hours}:{minutes}:{seconds} 🔜")
    print(f"{data['message']} is now")


def view_current_reminders():
    return print_csv_data(scheduler)


# Main Function
def main():
    while True:
        print_main_menus()
        order = reuse.select_a_number("Select a number. ", 1, 4)
        if order == 1:
            countdown_thread = threading.Thread(target=start_a_countdown_timer())
            countdown_thread.start()
            countdown_thread.join()
        elif order == 2:
            reminder_thread = threading.Thread(target=remind_schedule())
            reminder_thread.start()
            reminder_thread.join()
        elif order == 3:
            view_current_reminders()
        elif order == 4:
            break
        else:
            print("Error : The logic might be fault.")


# Execution
main()

