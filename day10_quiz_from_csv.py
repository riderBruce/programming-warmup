import csv
import random
import datetime
import time
import os

quiz_file = "quiz.csv"
score_file = "quiz_scores.csv"


def load_quiz_data(path):
    with open(path, "r") as file:
        # read csv data as a list of dictionaries [{a: aa, b: bbb}, {a: dse, b: def}, {} ... ]
        # looks like each [ row {columns : value} {column: value} ... ],
        reader = csv.DictReader(file)
        return list(reader)


def run_quiz(quiz_data, num):
    picked_quiz = random.sample(quiz_data, num)
    score = 0
    for q in picked_quiz:
        user = input(f"{q['question']}\n> ").strip().lower()
        answer = q['answer'].strip().lower()
        if user == answer:
            print("\033[92m✅ Correct!\033[0m\n")
            score += 1
        else:
            print(f"\033[91m❌ Wrong.\033[0m The correct answer was: {q['answer']}\n")
    return score


def save_score(name, score, total, elapsed_time):
    header = ["Name", "Score", "Total", "TimeSpent", "date"]
    file_exists = os.path.isfile(score_file)

    with open(score_file, "a", newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(header)
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        data = [name, score, total, elapsed_time, date]
        writer.writerow(data)


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


def pick_number_of_question(total):
    return choose_a_number("How many questions do you want to try? ", 1, total)


def main():
    name = input("Enter your name: ").strip().title()
    quiz = load_quiz_data(quiz_file)
    total = len(quiz)
    # How many time do you want to play?
    while True:
        num = pick_number_of_question(total)
        start = time.time()
        score = run_quiz(quiz, num)
        recorded_score = round(score/num * 100)
        end = time.time()
        elapsed_time = end - start
        print(f"You spent {int(elapsed_time)} seconds in total.")
        print(f"🏁 Final Score for {name}: {score}/{num} ({recorded_score}%)")
        save_score(name, recorded_score, total, elapsed_time)
        time.sleep(1)
        if get_yes_no_input("Play again? "):
            continue
        else:
            print("Thanks for playing!")
            break


main()
