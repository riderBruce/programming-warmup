# 😁 Day 5 - Loops, Lists & Mini-Project

# Goals
# What do you like to do?
# 1. View to-do list
# 2. Add a task
# 3. Remove a task
# 4. Exit

# import
import datetime


# Global variable
to_do_list = []
file_path = "to_do_list.txt"


# Basic functions
def view_to_do_list():
    print("To-Do List: ")
    if to_do_list:
        for index, value in enumerate(to_do_list):
            print(f"{index + 1}. {value}")
    else:
        print("There's no data.")


def add_a_task():
    text = input("Enter a task: ")
    right_text = text_checker(text)
    to_do_list.append(text)
    print("Task added.")
    with open(file_path, "a") as file:
        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.writelines(text + ' ' + time_stamp + '\n')



# if there are similar text, this method give the exist item. or not give an input.
def text_checker(text):
    _text = text.strip().lower().replace(' ', '')
    for item in to_do_list:
        _item = item.strip().lower().replace(' ', '')
        if _text == _item:
            print("There's similar item.")
            return item
    return text


def remove_a_task():
    text = input("Enter a task: ")
    try:
        for i in range(len(to_do_list)):
            right_text = text_checker(text)
            to_do_list.remove(right_text)
            print(f"Task removed: {right_text}")
            with open(file_path, "a") as file:
                time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.writelines(right_text + ' ' + time_stamp + ' Done ✅ \n')
    except Exception as e:
        print(f"That task doesn't exist.")
        view_to_do_list()


def exit_from_to_do_list():
    print("Exit from To-Do List. Thank you.")


def get_an_order():
    try:
        order = int(input("> "))
        if not 1 <= order <= 4:
            raise Exception
        return order
    except Exception as e:
        print("Please select from 1 to 4.")
        return 1


def order_selector(order):
    if order == 1:
        view_to_do_list()
    elif order == 2:
        add_a_task()
    elif order == 3:
        remove_a_task()
    elif order == 4:
        exit_from_to_do_list()


# Main function
def main():
    print("What would you like to do?")
    print(" 1. View to-do list")
    print(" 2. Add a task")
    print(" 3. Remove a task")
    print(" 4. Exit")
    # print("> ")
    while True:
        order = get_an_order()
        order_selector(order)
        if order == 4: break


main()
