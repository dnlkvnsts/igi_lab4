



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