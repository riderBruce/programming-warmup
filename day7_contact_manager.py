# Day 7 - Dictionary Practice: Contact Manager


# Use dictionaries to store structured data(e.g., name, phone, email)
# Practicing adding, updating, deleting, and viewing contact information
# Use functions to keep the code clean and modular

# What would you like to do?
# 1. View all contacts
# 2. Add a contact
# 3. Update a contact
# 4. Delete a contact
# 5. Exit




# import
import re
import json

# Global variables
MAIN_MENU_TEXT = """
What would you like to do?
1. View all contacts
2. Add a contact
3. Update a contact
4. Delete a contact
5. Exit
"""
contacts = {}
# contacts = {
#     "young": {"phone": "010-1111-2222", "email": "young@example.com"},
#     "hyeryeon": {"phone": "010-3333-4444", "email": "hyeryeon@example.com"}
# }
file_path = "contact_list.txt"


# Basic functions
def view_contacts():
    print("Contacts: ")
    for key, val in contacts.items():
        print(f"- {key}: {val['phone']}, {val['email']}")


def add_contact():
    name = str(input("Enter name: ")).lower()
    if name in contacts:
        answer_for_update = str(input("There's already that contact. Do you want to update? (Y/N) > ")).lower()
        if answer_for_update == "y":
            update_contact()
            return
        print("Return to menu.")
        return
    while True:
        phone = str(input("Enter phone: "))
        if validate_phone_number(phone):
            break
        print("It's invalid number. Please try it again.")
    while True:
        email = str(input("Enter email: "))
        if validate_email(email):
            break
        print("It's invalid email format. Please try it again. ")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added")
    view_contacts()


def update_contact():
    # showing all names
    names = [name for name in contacts.keys()]
    print(f"There are these contacts : {', '.join(names)}")
    # selecting name
    name = str(input("Which contact do you want to update? ✅ Select name: ")).lower()
    # return if there's no name
    if name not in names:
        print(f"There's no one who is {name}.")
        return
    # showing existed data
    print("Here's existed data. ")
    value = contacts[name]
    print(f"- {name}: {value['phone']}, {value['email']}")
    # input
    print("Please input new data. ")
    while True:
        phone = str(input("Enter phone: "))
        if validate_phone_number(phone):
            break
        print("It's invalid number. Please try it again. ")
    while True:
        email = str(input("Enter email: "))
        if validate_email(email):
            break
        print("It's invalid email format. Please try it again. ")
    # update
    contacts[name] = {"phone": phone, "email": email}
    # show
    value = contacts[name]
    print(f"- {name}: {value['phone']}, {value['email']}")
    print("Contact updated.")
    return


def delete_contact():
    # showing all names
    names = [name for name in contacts.keys()]
    print(f"There are these contacts : {', '.join(names)}")
    # selecting name
    name = str(input("Which contact do you want to delete? ✅ Select name: ")).lower()
    # return if there's no name
    if name not in names:
        print(f"There's no one who is {name}.")
        return
    # showing existed data
    print("Here's existed data. ")
    value = contacts[name]
    print(f"- {name}: {value['phone']}, {value['email']}")
    # confirm
    print("Do you really want to delete this contact? You can't undo this. 🧨 ")
    answer = str(input("Please input Y. It'll be deleted. : ")).lower()
    # delete
    if answer == 'y':
        contacts.pop(name)
        print("Contact deleted.")
        view_contacts()
        return
    print("Data is not deleted. ")
    return


def exit_program():
    print("Goodbye!")
    return "exit"


def get_an_order():
    try:
        order = int(input("> "))
        if order == 1:
            view_contacts()
            return
        if order == 2:
            add_contact()
            return
        if order == 3:
            update_contact()
            return
        if order == 4:
            delete_contact()
            return
        if order == 5:
            return exit_program()

        raise Exception
    except Exception as e:
        print("Please put the number from 1 to 5. 🥺")


def print_main_menu():
    print(MAIN_MENU_TEXT)


def validate_phone_number(number):
    pattern = re.compile(r"^\d{3}[\s.-]?\d{4}[\s.-]?\d{4}$")
    return re.match(pattern, number) is not None


def validate_email(email):
    pattern = (r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return re.match(pattern, email) is not None


def read_contact_file(path):
    try:
        with open(path, "r") as file:
            json_string = file.read()
            global contacts
            contacts = json.loads(json_string)
    except Exception as e:
        return


def save_contact_file(path):
    json_string = json.dumps(contacts)
    with open(path, "w") as file:
        file.write(json_string)

# Main function
def main():
    read_contact_file(file_path)
    print_main_menu()
    while True:
        result = get_an_order()
        save_contact_file(file_path)
        if result == "exit":
            break


# Execution
main()
