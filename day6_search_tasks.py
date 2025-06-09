# Day 6 - File Reading & Search Feature


# What word would you like to search for?
# No matches found.
# case-insensitive
# Found 3 matches
# Would you like search again?

# import


# Global variable
file_path = "to_do_list.txt"


# Basic functions
def get_data_from_file(path):
    with open(path, "r") as file:
        data = file.readlines()
        _data = [d.strip() for d in data]
        return _data


def search_data(data, input_text):
    results = []
    for d in data:
        if input_text.lower() in d.lower():
            results.append(d)
    return results


def print_results(results, full_data):
    i = len(results)
    if i == 0:
        print("No matches found. 😭")
        return
    print(f"Found {i} match(es): ")
    for index, line in enumerate(full_data):
        if any(result == line for result in results):
            print(f"[{index + 1}]  {line}")


def ask_again():
    while True:
        text = str(input("Would you like to search again? (Y/N) 👌  ")).strip().lower()
        if text in ["y", "n"]:
            return text
        print("Please select Y or N.")


# Main Function
def main():
    data = get_data_from_file(file_path)
    while True:
        input_text = str(input("What word would you like to search for? 💁  "))
        if input_text.strip().lower() in ["q", "exit"]:
            print("Goodbye!")
            break
        results = search_data(data, input_text)
        print_results(results, data)
        answer = ask_again()
        if answer == "n":
            break


# Action
main()
