# Day 8 - Random, Time, and Simple Games

# Use the random and time modules
# Practice loops, logic, and user interaction
# Build something playful to relax your brain while still coding

# Mini-Project: Number Guessing Game
# The computer randomly selects a number between 1 and 100.
# The user has to guess it.
# After each guess, print:
# Too high or Too low or Correct
# Count how many guesses it took.
# Add a 1-second delay between responses (using time.sleep(1))
# Ask if the user wants to play again.

# Limit the number of tries (e.g., 7 guesses max)
# At the end, say "You lost! The number was 84."
# Record high scores in a file


# import
import time
import random
import json


# Global variables
file_path = "high_scores.txt"
max_tries = 7


# Reusable methods
def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt + " (Y/N): ").lower()
        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please response with 'y' or 'n'.")


def read_file(path):
    try:
        with open(path, "r") as file:
            json_string = file.read()
            return json.loads(json_string)
    except Exception as e:
        return


def save_file(content, path):
    json_string = json.dumps(content)
    with open(path, "w") as file:
        file.write(json_string)


# Basic methods
def select_a_number():
    target = random.randint(1, 100)
    return target


def guess_the_number():
    try:
        user_select = int(input("Take a guess: "))
        if 1 <= user_select <= 100:
            return True, user_select
        print(f"You selected a number out of range. Please select 1 ~ 100.")
        return False, -1
    except Exception as e:
        print(f"Invalid input. Please enter a number.")
        return False, -1


def check_the_number(target, selected):
    if target < selected:
        print("Too high")
        return False
    elif target > selected:
        print("Too low")
        return False
    elif target == selected:
        print("Correct!")
        return True
    else:
        print("There's some problem. Check it again.")
        return False


def ask_to_play_again():
    return get_yes_no_input("Play again? ")


def record_high_scores(tries):
    data = read_file(file_path)
    high_scores = int(data) if data is not None else max_tries
    if high_scores > tries:
        save_file(tries, file_path)


# Main methods
def main():
    while True:
        target = select_a_number()
        tries = 0
        while True:
            tries = tries + 1
            success, user_select = guess_the_number()
            time.sleep(1)
            if not success:
                continue   # still one try, but skip checking
            is_correct = check_the_number(target, user_select)
            if is_correct:
                print(f"Correct! 🏆 You guessed it in {tries} tries.")
                record_high_scores(tries)
                break
            if tries >= max_tries:
                print(f"You lost! The number was {target}.")
                break
        if ask_to_play_again():
            continue
        else:
            break

# Execution
main()
