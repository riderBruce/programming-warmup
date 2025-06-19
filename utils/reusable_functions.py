# Reusable Function

def select_a_number(prompt: str, start: int, end: int):
    """
    Ask the user to enter a number between `start` and `end`.

    Parameters:
        prompt (str): The text shown to the user.
        start (int): The minimum acceptable value.
        end (int): The maximum acceptable value.
    Returns:
        int: A valid number entered by the user between start and end.
    """
    while True:
        try:
            num = int(input(prompt + f"({start} ~ {end}) > "))
            if start <= num <= end:
                return num
            print(f"You selected a number out of range. Please select {start} ~ {end}.")
        except Exception as e:
            print(f"Invalid input. Please enter a number.")


def select_yes_or_no(prompt: str):
    """
    Ask the user to enter yes or no and validate the response.

    Parameters:
        prompt (str): The text shown to the user.

    Returns:
        bool: True if the user enters yes, False if the user enter no.
    """
    while True:
        user_input = input(prompt + " (Y/N): ").lower()
        if user_input in ['y', 'yes']:
            return True
        elif user_input in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please response with 'y' or 'n'.")

