


import base.validation as val



def input_team_data():
    
    name = val.get_string("Enter team name: ")
    points = val.get_int_input("Enter points: ")
    return name, points

def input_filename(extension=".csv"):
    name = val.get_string(f"Enter filename (default will add {extension}): ")
    if not name.endswith(extension):
        name += extension
    return name


















    
def repeat_task():
    """
    Asks the user if they want to repeat the task.

    Returns:
        bool: True if the user wants to repeat, False otherwise.
    """
    while True:
            choice = input("Repeat this task ?(y/n) ").lower()
            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print("Invalid input!!! Input y or n\n")