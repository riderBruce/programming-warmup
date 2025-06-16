# Day 12 Mini Tools: Unit Converter

# Choose conversion type : temperature, length, weight, currency, time
# Submenu : Choose unit pairs °C ⇄ °F, kg ⇄ lb, cm ⇄ in, etc.
# Input: User enters a value
# Output: Show converted result


# Import
import time
import datetime

# Global Variables


# Reusable Methods
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


# Basic Methods
def celsius_to_fahrenheit(c):
    return int(c * 9 / 5 + 32)


def fahrenheit_to_celsius(f):
    return int((f - 32) * 5 / 9)


def kilo_gram_to_pound(k):
    return int(k * 2.20462)


def pound_to_kilo_gram(p):
    return int(p / 2.20462)


def centimeter_to_inch(c):
    return int(c / 2.54)


def inch_to_centimeter(i):
    return int(i * 2.54)


def krw_to_cad(k):
    return int(k / 1000)


def cad_to_krw(c):
    return int(c * 1000)


def seoul_time_to_vancouver_time(h):
    return (h + 8) % 24


def vancouver_time_to_seoul_time(h):
    return (h + 16) % 24


def select_unit(a, b):
    print(f"Please select the order")
    print(f"1. {a} ➡️ {b}")
    print(f"2. {b} ➡️ {a}")
    print(f"0. Go to Main Menu.")
    return choose_a_number("> ", 0, 2)


# Bridge Methods
def temperature_converter():
    a = "°C"
    b = "°F"

    order = select_unit(a, b)
    if order == 1:
        x = choose_a_number("Put it a value. > ", -1000, 1000)
        y = celsius_to_fahrenheit(x)
        print("*" * 30)
        print(f"{x} {a} ➡️ {y} {b}")
    elif order == 2:
        x = choose_a_number("Put it a value. > ", -1000, 1000)
        y = fahrenheit_to_celsius(x)
        print("*" * 30)
        print(f"{x} {b} ➡️ {y} {a}")
    elif order == 0:
        print("Return to Main Menu.")
    time.sleep(1)
    return


def length_converter():
    a = "cm"
    b = "in"

    order = select_unit(a, b)
    if order == 1:
        x = choose_a_number("Put it a value. > ", -1000, 1000)
        y = centimeter_to_inch(x)
        print("*" * 30)
        print(f"{x} {a} ➡️ {y} {b}")
    elif order == 2:
        x = choose_a_number("Put it a value. > ", -1000, 1000)
        y = inch_to_centimeter(x)
        print("*" * 30)
        print(f"{x} {b} ➡️ {y} {a}")
    elif order == 0:
        print("Return to Main Menu.")
    time.sleep(1)
    return


def weight_converter():
    a = "kg"
    b = "lb"

    order = select_unit(a, b)
    if order == 1:
        x = choose_a_number("Put it a value. > ", -1000, 1000)
        y = kilo_gram_to_pound(x)
        print("*" * 30)
        print(f"{x} {a} ➡️ {y} {b}")
    elif order == 2:
        x = choose_a_number("Put it a value. > ", -1000, 1000)
        y = pound_to_kilo_gram(x)
        print("*" * 30)
        print(f"{x} {b} ➡️ {y} {a}")
    elif order == 0:
        print("Return to Main Menu.")
    time.sleep(1)
    return


def currency_converter():
    a = "KRW"
    b = "CAD"

    order = select_unit(a, b)
    if order == 1:
        x = choose_a_number("Put it a value. > ", -1000, 1000)
        y = krw_to_cad(x)
        print("*" * 30)
        print(f"{x} {a} ➡️ {y} {b}")
    elif order == 2:
        x = choose_a_number("Put it a value. > ", -1000, 1000)
        y = cad_to_krw(x)
        print("*" * 30)
        print(f"{x} {b} ➡️ {y} {a}")
    elif order == 0:
        print("Return to Main Menu.")
    time.sleep(1)
    return


def time_converter():
    a = "SEL"
    b = "VAN"

    order = select_unit(a, b)
    if order == 1:
        h = choose_a_number("Put it hour. (24hour) > ", 0, 23)
        m = choose_a_number("Put it minute. > ", 0, 60)
        _h = seoul_time_to_vancouver_time(h)
        x = datetime.time(h, m)
        y = datetime.time(_h, m)
        print("*" * 30)
        print(f"{x} {a} ➡️ {y} {b}")
    elif order == 2:
        h = choose_a_number("Put it hour. > ", 0, 23)
        m = choose_a_number("Put it minute. > ", 0, 60)
        _h = vancouver_time_to_seoul_time(h)
        x = datetime.time(h, m)
        y = datetime.time(_h, m)
        print("*" * 30)
        print(f"{x} {b} ➡️ {y} {a}")
    elif order == 0:
        print("Return to Main Menu.")
    time.sleep(1)
    return


def print_main_menu():
    print("-" * 30)
    print("Welcome to the Unit Converter!")
    print("1. Temperature ")
    print("2. Length")
    print("3. Weight")
    print("4. Currency(KRW-CAD)")
    print("5. Time (SEL-VAN)")
    print("0. Quit the program")
    print("-" * 30)


# Main Methods
def main():
    while True:
        print_main_menu()
        order = choose_a_number(">  ", 0, 5)
        if order == 1:
            temperature_converter()
        elif order == 2:
            length_converter()
        elif order == 3:
            weight_converter()
        elif order == 4:
            currency_converter()
        elif order == 5:
            time_converter()
        elif order == 0:
            if get_yes_no_input("Confirm to quit. "):
                break


# Execution
main()
