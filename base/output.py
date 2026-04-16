


# Task 1

def output_teams_table(teams_list):
    
        if not teams_list:
            print("\n[!] The list is not contain this team.")
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
    print(f"\n>>> {msg}")
    
# Task 2
def print_analysis_results(results):
    """Helper for Task 2 to print dictionary results nicely."""
    print("\n" + "="*40)
    print(f"{'TEXT ANALYSIS RESULTS':^40}")
    print("="*40)
    for key, value in results.items():
        print(f"{key:.<30} {value}")
    print("="*40)
    
# Task 3

def output_math_table(data):
    header = f"| {'x':^8} | {'n':^5} | {'F(x)':^12} | {'Math F(x)':^12} | {'eps':^10} |"
    sep = "-" * len(header)
    print("\n" + sep)
    print(header)
    print(sep)
    for row in data:
        print(f"| {row['x']:^8.2f} | {row['n']:^5} | {row['f_x']:^12.6f} | {row['math_x']:^12.6f} | {row['eps']:^10.1e} |")
    print(sep)

def output_statistics(stats):
    print("\n--- SEQUENCE STATISTICS ---")
    for key, value in stats.items():
        print(f"{key:.<25} {value:.6f}")

#Task 4

def print_rhomb_info(rhomb_obj):
    print("\n" + "="*50)
    print(f"{'ДАННЫЕ ОБЪЕКТА':^50}")
    print("-"*50)
    print(rhomb_obj.get_info())
    print("="*50 + "\n")
    
#Task 5

def output_matrix(matrix, title="Matrix:"):
    print(f"\n{title}")
    print(matrix)

def output_stats(stats_dict):
    print("\n" + "="*50)
    print(f"{'STATISTICAL ANALYSIS RESULTS':^50}")
    print("="*50)
    for key, value in stats_dict.items():
        if isinstance(value, float):
            print(f"{key:.<35} {value:.2f}")
        else:
            print(f"{key:.<35} {value}")
    print("="*50)
    
#Task 6

def output_dataframe(df, title="DataFrame Content:"):
    """Displays a Pandas DataFrame with a title."""
    print(f"\n--- {title} ---")
    print(df.to_string())