
import csv
import pickle
import os

import base.validation as val
import base.output as out
import base.input as inp


class FileMixin:
    def to_dict(self):
        return {"name": self.name, "points": self.points}
    
    

class BaseEntity:
    def __init__(self, name):
        self._name = name 
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value
        
   
   
        
class Team(BaseEntity, FileMixin):
    teams_count = 0
    
    def __init__(self, name, points):
        super().__init__(name)
        self._points = points
        Team.teams_count += 1
    
    @property
    def points(self):
        return self._points
    
    @points.setter
    def points(self, value):
        if value < 0:
            raise ValueError("Points cannot be negative")
        self._points = value

    
    def __str__(self):
        return f"Team: {self.name} Points: {self.points}"
    
   
   
    
class Competition:
    def __init__(self):
        self.teams = []

    def add_team(self, name, points):
        self.teams.append(Team(name, points))

    def sort_by_rank(self):
        """Sorts teams by points descending."""
        self.teams.sort(key=lambda x: x.points, reverse=True)

    def find_team_by_name(self, search_name):
        """Searches for a team (Case-insensitive)."""
        return [t for t in self.teams if t.name.lower() == search_name.lower()]
    
    def save_csv(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["name", "points"])
            writer.writeheader()
            for t in self.teams:
                writer.writerow(t.to_dict())

    def load_csv(self, filename):
        if not os.path.exists(filename): return False
        self.teams = []
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.add_team(row['name'], int(row['points']))
        return True

    def save_pickle(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.teams, f)

    def load_pickle(self, filename):
        if not os.path.exists(filename): return False
        with open(filename, 'rb') as f:
            self.teams = pickle.load(f)
        return True
  
  
  


  
def run_task1():
    comp = Competition()
    
    initial_dict = {"Spartak": 15, "Zenit": 20, "Dynamo": 12}
    for n, p in initial_dict.items():
        comp.add_team(n, p)

    while True:
        print("\n--- TASK 1 MENU (Variant 6) ---")
        print("1. Add team")
        print("2. Show Leaderboard (Sorted)")
        print("3. Find First Place")
        print("4. Search by Name")
        print("5. CSV (Save/Load)")
        print("6. Pickle (Save/Load)")
        print("0. Back")

        choice = val.get_int_input("\nSelect operation: ")

        try:
            if choice == 1:
                n, p = inp.input_team_data()
                comp.add_team(n, p)
                out.print_message("Team added successfully.")

            elif choice == 2:
                comp.sort_by_rank()
                out.output_teams_table(comp.teams)

            elif choice == 3:
                comp.sort_by_rank()
                if comp.teams:
                    out.print_message(f"FIRST PLACE: {comp.teams[0]}")
                else:
                    out.print_message("List is empty.")

            elif choice == 4:
                while True:
                    s_name = val.get_string("Enter name to search : ")
                    results = comp.find_team_by_name(s_name)
                    if results:
                        out.output_teams_table(results)
                        break  
                    else:
                        out.print_message(f"Team '{s_name}' not found. Please try again.")

            elif choice == 5:
                sub = val.get_int_input("1. Save CSV | 2. Load CSV: ")
                fname = inp.input_filename(".csv")
                if sub == 1: 
                    comp.save_csv(fname)
                    out.print_message("Saved.")
                else: 
                    if comp.load_csv(fname): out.print_message("Loaded.")
                    else: out.print_message("File not found.")

            elif choice == 6:
                sub = val.get_int_input("1. Save Pickle | 2. Load Pickle: ")
                fname = inp.input_filename(".pkl")
                if sub == 1: 
                    comp.save_pickle(fname)
                    out.print_message("Saved.")
                else: 
                    if comp.load_pickle(fname): out.print_message("Loaded.")
                    else: out.rint_message("File not found.")

            elif choice == 0:
                break
            
            if not inp.repeat_task():
                break

        except Exception as e:
            out.print_message(f"Error : {e}")