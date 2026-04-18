


# Task 1

def output_teams_table(teams_list):
    """
    Displays a list of team objects in a formatted table structure.
    
    The table includes an index number (№), the team's name, and their points.
    If the list is empty, a corresponding message is displayed to the user.

    Args:
        teams_list (list): A list of objects (expected to have 'name' and 'points' attributes).
    """
    if not teams_list:
        print("\nThe list is not contain this team.")
        return

   
    header = f"| {'№':^3} | {'Team Name':^20} | {'Points':^10} |"
    sep = "-" * len(header)

    print("\n" + sep)
    print(header)
    print(sep)

    
    for i, team in enumerate(teams_list, 1):
        print(f"| {i:^3} | {team.name:^20} | {team.points:^10} |")

    print(sep)


def print_message(msg):
    """
    Prints a formatted system message to the console.

    Args:
        msg (str): The message text to be displayed.
    """
    print(f"\n>>> {msg}")
    
# Task 2
def print_analysis_results(results):
    """
    Prints the text analysis results in a formatted table.

    Args:
        results (dict): A dictionary containing analysis results (key-value pairs).
    """
    print("\n" + "="*40)
    print(f"{'Text analysis result':^40}")
    print("="*40)
    for key, value in results.items():
        print(f"{key:.<30} {value}")
    print("="*40)
    
# Task 3

def output_math_table(data):
    """
    Prints a formatted table of Taylor series calculation results.

    Args:
        data (list): A list of dictionaries containing keys 'x', 'n', 'f_x', 'math_x', and 'eps'.

    """
    header = f"| {'x':^8} | {'n':^5} | {'F(x)':^12} | {'Math F(x)':^12} | {'eps':^10} |"
    sep = "-" * len(header)
    print("\n" + sep)
    print(header)
    print(sep)
    for row in data:
        print(f"| {row['x']:^8.2f} | {row['n']:^5} | {row['f_x']:^12.6f} | {row['math_x']:^12.6f} | {row['eps']:^10.1e} |")
    print(sep)

def output_statistics(stats):
    """
    Displays the calculated statistical results in a list with dotted alignment.

    Args:
        stats (dict): A dictionary where keys are stat names and values are float results.

    """
    print("\n--- statistics ---")
    for key, value in stats.items():
        print(f"{key:.<25} {value:.6f}")

#Task 4

def print_rhomb_info(rhomb_obj):
    """
    Displays formatted information about the Rhomb object on the screen.

    Args:
        rhomb_obj (Rhomb): An instance of the Rhomb class containing the shape's data.
    """
    print("\n" + "="*50)
    print(f"{'ДАННЫЕ ОБЪЕКТА':^50}")
    print("-"*50)
    print(rhomb_obj.get_info())
    print("="*50 + "\n")
    
#Task 5

def output_matrix(matrix, title="Matrix:"):
    """
    Prints a matrix or array to the console with a formatted title.

    Args:
        matrix (np.ndarray or list): The matrix data to be displayed.
        title (str): The header text to print above the matrix (default is "Matrix:").

    """
    print(f"\n{title}")
    print(matrix)

def output_stats(stats_dict):
    """
    Displays statistical analysis results in a structured and readable table format.
    Automatically formats float values to two decimal places and aligns text.

    Args:
        stats_dict (dict): A dictionary where keys are labels (str) and 
                           values are the results (float, int, or list).

    """

    print(f"{'Results':^50}")
    print("="*50)
    for key, value in stats_dict.items():
        if isinstance(value, float):
            print(f"{key:.<35} {value:.2f}")
        else:
            print(f"{key:.<35} {value}")
    print("="*50)
    
#Task 6

def output_dataframe(df, title="DataFrame :"):
    """
    Formats and prints a Pandas DataFrame to the console.

    Args:
        df (pd.DataFrame): The DataFrame object to display.
        title (str): The header text to print above the table.
    """
    print(f"\n--- {title} ---")
    print(df.to_string())