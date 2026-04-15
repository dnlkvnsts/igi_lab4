"""
The functions that can help validate the inputed data

Lab 4. Working with files, classes, serializers, regular expressions, and
standard libraries

Version: 1

Developer: Danilkova Anastasia Alexandrovna

Date: 13.04.2026
"""


def get_int_input(text):
    """
    Asks the user to input an integer number and validates it.

    Args:
        text (str): The message to show to the user.

    Returns:
        int: The valid integer number entered by the user.
    """
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Invalid input. Please enter an integer number.\n")



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
    
        if text.strip():
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
        try:
            return float(input(text))
        except ValueError:
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
           
            
