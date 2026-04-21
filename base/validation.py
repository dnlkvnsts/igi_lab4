"""
The functions that can help validate the inputed data

Lab 4. Working with files, classes, serializers, regular expressions, and
standard libraries

Version: 1

Developer: Danilkova Anastasia Alexandrovna

Date: 13.04.2026
"""

import re
import matplotlib
import matplotlib.colors

def get_int_input(text):
    """
    Asks the user to input an integer number and validates it.

    Args:
        text (str): The message to show to the user.

    Returns:
        int: The valid integer number entered by the user.
    """
    while True:
        user_input = input(text)
        if re.fullmatch(r'[+-]?\d+', user_input):
            return int(user_input)
        print("Invalid input. Please enter an integer number.\n")

def get_int_positive_input(text):
    """
    Asks the user to input an integer number and validates it.

    Args:
        text (str): The message to show to the user.

    Returns:
        int: The valid integer number entered by the user.
    """
    while True:
        number = get_int_input(text)
        if number > 0:
            return number
        else:
            print("Invalid input. Please enter an integer positive number.\n")
        
           

def get_string(message):
    """
    Asks the user to input a text string and ensures it is not empty or just spaces.

    Args:
        message (str): The message to show to the user.

    Returns:
        str: The valid text string entered by the user.
    """
    while True:
        text=input(message)
    
        if re.search(r'\S', text):
            return text
    
        print("Invalid input. The string cannot be empty or consist only of spaces.\n")
        
        
def get_float_input(text):
    """
    Asks the user to input a float number and validates it.

    Args:
        text (str): The message to show to the user.

    Returns:
        float: The valid float number entered by the user.
    """
    while True:
        user_input = input(text)
        if re.fullmatch(r'[+-]?\d+(\.\d+)?', user_input):
            return float(user_input)
        print("Invalid input. Please enter a number.\n")
            
            

def get_float_positive_input(text):
    """
    Asks the user to input a float number strictly between 0 and 1.

    Args:
        text (str): The message to show to the user.

    Returns:
        float: The valid float number between 0 and 1.
    """
    while True:
        number=get_float_input(text)
        if 0 < number < 1:
            return number
        else:
            print("Invalid input. Please enter a positive float number from 0 to 1.\n")
           
#Task 4           
def get_side_of_rhomb(prompt):
    """
    Asks the user to input a side length and ensures it is greater than 0.

    Args:
        prompt (str): The message to show to the user.

    Returns:
        float: The valid positive float number representing the side.
    """
    while True:
        value = get_float_input(prompt)
        if value > 0:
            return value
        print("Invalid input. Please enter a positive number (greater than 0).\n")


def get_valid_angle(prompt, min_angle=0, max_angle=90):
    """
    Asks the user to input an angle within a specific range.

    Args:
        prompt (str): The message to show to the user.
        min_angle (float): The minimum allowed angle value.
        max_angle (float): The maximum allowed angle value.

    Returns:
        float: The valid float number between the specified range.
    """
    while True:
        value = get_float_input(prompt)
        if min_angle < value < max_angle:
            return value
        print(f"Invalid input. Please enter an angle between {min_angle} and {max_angle}.\n")


def get_color_input(prompt):
    """
    Asks the user to input a color and validates it using a regular expression.
    Supports names (letters only) or hex codes (e.g., #FFFFFF).

    Args:
        prompt (str): The message to show to the user.

    Returns:
        str: A valid color name or hex code.
    """
    color_pattern = r'^\s*([a-zA-Z]+|#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3}))\s*$'

    while True:
        raw_input = input(prompt)
        match = re.match(color_pattern, raw_input)
        
        if match:        
            color = match.group(1)
  
            if matplotlib.colors.is_color_like(color):
                return color
            else:
                print(f"Error: '{color}' is not a recognized color. Try 'red', 'green', etc.\n")
        else:
            print("Invalid format. Use letters (e.g., 'red') or hex (e.g., '#FF0000').\n")