# Day 9 - Build a Flashcard Quiz Game

# Use dictionaries, random, and file reading
# Build a quiz app that tests you with flashcards
# Practice input, shuffling, and scoring

# Imports
import json
import random
import time


# Global variables
flashcards_dict = {
    "variable": "a named container for a value",
    "function": "a reusable block of code",
    "loop": "a way to repeat code",
    "method": "a block of code which only runs when it is called",
    "int": "a fundamental built-in data type used to represent whole numbers. ",
    "pandas": "a Python library used for working with data sets"
}
file_path = "flashcards.json"


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
        print(e)
        return flashcards_dict


def save_file(content, path):
    try:
        json_string = json.dumps(content)
        with open(path, "w") as file:
            file.write(json_string)
    except Exception as e:
        print(e)
        return


def choose_a_number(prompt, start, end):
    while True:
        try:
            num = int(input(prompt + f"({start} ~ {end}) > "))
            if start <= num <= end:
                return num
            print(f"You selected a number out of range. Please select {start} ~ {end}.")
        except Exception as e:
            print(f"Invalid input. Please enter a number.")


# Basic methods
def write_flashcards_file(flashcards):
    return save_file(flashcards, file_path)


def load_flashcards_from_json(path):
    return read_file(path)


def choose_reverse_mode():
    return get_yes_no_input("Do you want to try Reverse Mode? ")


def pick_number_of_question(total_cards):
    return choose_a_number("How many question do you want to try? ", 1, total_cards)


def give_a_quiz(flashcards, reverse, num):
    score = 0
    selected_card = random.sample(list(flashcards.items()), num)
    for key, value in selected_card:
        if not reverse:
            answer = input(f"What term matches this definition? \n{value} > ")
            if answer == key:
                print(f"✅ Correct!")
                score = score + 1
            else:
                print(f"❌ Wrong. The answer is: {key}.")
        else:
            answer = input(f"What definition matches this term? \n{key}\n > ")
            if answer == value:
                print(f"✅ Correct!")
                score = score + 1
            else:
                print(f"❌ Wrong. The answer is: {value}.")
    return score


# Main methods
def main():
    # write_flashcards_file(flashcards_dict)
    flashcards = load_flashcards_from_json(file_path)
    total_cards = len(flashcards)
    while True:
        reverse = choose_reverse_mode()
        num = pick_number_of_question(total_cards)
        score = give_a_quiz(flashcards, reverse, num)
        time.sleep(1)
        print(f"Score: {score}/{num}")
        if get_yes_no_input("Play again? "):
            continue
        else:
            print("Thanks for playing!")
            break


# Operation
main()