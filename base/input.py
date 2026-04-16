


import base.validation as val


#Task 1

def input_team_data():
    
    name = val.get_string("Enter team name: ")
    points = val.get_int_input("Enter points: ")
    return name, points

def input_filename(extension=".csv"):
    name = val.get_string(f"Enter filename (default will add {extension}): ")
    if not name.endswith(extension):
        name += extension
    return name


#Task 4

def input_rhomb_data():
    """Отдельная функция для ввода данных ромба"""
    print("\n--- Ввод данных ромба ---")
    side = val.get_float_input("Введите сторону ромба (a): ")
    
    while True:
        angle = val.get_float_input("Введите угол в градусах (0 < angle < 90): ")
        if 0 < angle < 90:
            break
        print("Ошибка: для данной задачи угол должен быть от 0 до 90 градусов.")
        
    color = val.get_string("Введите цвет фигуры (например, red, blue): ")
    label = val.get_string("Введите подпись для фигуры: ")
    
    return side, angle, color, label


#Task 5

def input_matrix_dims():
    """Gets matrix dimensions from user."""
    n = val.get_int_input("Enter the number of rows (n): ")
    m = val.get_int_input("Enter the number of columns (m): ")
    return n, m





    
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
                
                
