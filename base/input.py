

import re
import base.validation as val


#Task 1

def input_team_data():
    """
    Ask the user to enter a team name and its current points.

    Returns:
        tuple: A tuple containing the team name (str) and points (int).
    """
    name = val.get_string("Enter team name: ")
    while True:
        points = val.get_int_input("Enter points: ")
        if points >= 0:
            return name, points
        print("Points cannot be negative! Please try again.\n")

def input_filename(extension=".csv"):
    """
    Ask the user for a filename and automatically appends the extension if it's missing.
    Uses regular expressions to validate the file extension at the end of the string.

    Args:
        extension (str): The required file extension (e.g., '.csv' or '.pkl').

    Returns:
        str: The validated filename with the correct extension.
    """
    name = val.get_string(f"Enter filename (default will add {extension}): ")
    pattern = re.escape(extension) + r"$"
    
    if not re.search(pattern, name, re.IGNORECASE):
        name += extension
        
    return name


#Task 4

def input_rhomb_data():
    """
    Collects rhomb parameters from the user via console input.

    Returns:
        tuple: A tuple containing (side, angle, color, label).
               side (float): The length of the side.
               angle (float): The acute angle in degrees.
               color (str): The name of the color.
               label (str): The text label for the figure.
    """
    print("\n--- Rhomb Data Input ---")
    side = val.get_side_of_rhomb("Enter the side length of the rhomb (a): ")
    
    angle = val.get_valid_angle("Enter the angle in degrees (0 < angle < 90): ")
     
    color = val.get_color_input("Enter the shape color (name or #hex): ")
    label = val.get_string("Enter a label for the shape: ")
    
    return side, angle, color, label


#Task 5

def input_matrix_dims():
    """
    Prompts the user to input the dimensions (rows and columns) for a matrix.
    Uses a validation utility to ensure that the inputs are positive integers.

    Returns:
        tuple: A tuple containing (n, m), where:
               n (int): The number of rows.
               m (int): The number of columns.
    """
    n = val.get_int_positive_input("Enter the number of rows (n): ")
    m = val.get_int_positive_input("Enter the number of columns (m): ")
    return n, m


    
def repeat_task():
    """
    Asks the user whether to repeat the current task.
    
    
    Returns:
        bool: True if the user enters 'y' or 'Y' (yes), 
              False if the user enters 'n' or 'N' (no).
    """
    while True:
        choice = input("Repeat this task? (y/n): ")
        if re.fullmatch(r"^[yY]$", choice):
            return True
        if re.fullmatch(r"^[nN]$", choice):
            return False

        print("Invalid input!!! Please enter y or n (case insensitive).\n")
