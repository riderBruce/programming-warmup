# day 4 - Organizing Code with Function

# Import
import time


# Basic functions
def get_user_name():
    name = input("What's your name? ").strip().title()
    return name


def ask_feeling(name):
    feeling = input(f"How are you feeling today, {name}? ").strip().lower()
    responses = {
        "happy": "I'm happy to hear you. 💕 ",
        "sad": "That's too bad. 🥺 ",
        "tired": "We could use a beer. 🍻 ",
        "angry": "Look at me. Really? 😳 "
    }
    time.sleep(1)
    if feeling in responses:
        print(f"{responses[feeling]} {name}\n")
    else:
        print(f"Whoa, intense mood! Hang in there, {name} 🧨")
    return feeling


def check_energy(name):
    while True:
        try:
            energy_score = int(input(f"On a scale from 1 to 10, how was your energy today, {name}? "))
            time.sleep(1)
            if 8 <= energy_score <= 10:
                print("You were full of energy today.")
                break
            elif 4 <= energy_score <= 7:
                print("You had a moderate energy today.")
                break
            elif 1 <= energy_score <= 3:
                print("Maybe you need a rest.")
                break
            else:
                print(f"Please input from 1 to 10. {name}")
        except ValueError:
            time.sleep(1)
            print(f"That's too bad. Could you please input numbers? {name}")


# Main function
def main():
    name = get_user_name()
    time.sleep(1)
    ask_feeling(name)
    time.sleep(1)
    check_energy(name)


main()
