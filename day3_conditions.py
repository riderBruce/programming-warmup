name = input("What's your name? ").strip().title()

responses = {
    "happy": "I'm happy to hear you. 💕 ",
    "sad": "That's too bad. 🥺 ",
    "tired": "We could use a beer. 🍻 ",
    "angry": "Look at me. Really? 😳 "
}

answer = input(f"How are you feeling today, {name}? ").strip().lower()


if answer in responses:
    print(f"{responses[answer]} {name}")
else:
    print(f"Whoa, intense mood! Hang in there, {name} 🧨 ")


while True:
    try:
        energy_score = int(input(f"On a scale from 1 to 10, how was your energy today, {name}? "))
        if 8 <= energy_score <= 10:
            print("You were full of energy today.")
            break
        elif 4 <= energy_score <= 7:
            print("You had a moderate energy today.")
            break
        elif 1<= energy_score <= 3:
            print("Maybe you need a rest.")
            break
        else:
            print("Please input from 1 to 10.")
    except ValueError:
        print("That's not what I want. Please input numbers.")

