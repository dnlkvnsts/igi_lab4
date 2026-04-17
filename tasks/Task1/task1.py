"""
The task number 1

Lab 4. Working with files, classes, serializers, regular expressions, and
standard libraries

Version: 1

Developer: Danilkova Anastasia Alexandrovna

Date: 17.04.2026
"""


import csv
import pickle
import os
import re
import base.validation as val
import base.output as out
import base.input as inp


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class FileMixin:
    """
    A mixin class to provide dictionary conversion functionality for file serialization.
    """
    def to_dict(self):
        """
        Converts the object's core attributes into a dictionary format.

        Returns:
            dict: A dictionary containing the name and points of the entity.
        """
        return {"name": self.name, "points": self.points}
    
    

class BaseEntity:
    """
    A base class representing an entity with a name attribute.
    """
    def __init__(self, name):
        """
        Initializes the BaseEntity with a name.

        Args:
            name (str): The name of the entity.
        """
        self._name = name 
    
    @property
    def name(self):
        """
        Gets or sets the name of the entity. Includes validation for empty strings.

        Returns:
            str: The name of the entity.
            
        Raises:
            ValueError: If the provided name is empty or consists only of spaces.
        """
        return self._name
    
    @name.setter
    def name(self, value):
        if not re.search(r'\S', value):
            raise ValueError("Name cannot be empty or only spaces")
        self._name = value
        

       
class Team(BaseEntity, FileMixin):
    """
    A class representing a sports team, inheriting from BaseEntity and FileMixin.
    
    Attributes:
        teams_count (int): A static attribute tracking the total number of Team instances.
    """
    teams_count = 0
    
    def __init__(self, name, points):
        """
        Initializes a new Team instance.

        Args:
            name (str): The name of the team.
            points (int): The initial points earned by the team.
        """
        super().__init__(name)
        self.points = points
        Team.teams_count += 1
    
    @property
    def points(self):
        """
        Gets or sets the team's points. Includes validation for negative values.

        Returns:
            int: The current points of the team.

        Raises:
            ValueError: If the points value is less than zero.
        """
        return self._points
    
    @points.setter
    def points(self, value):
        if value < 0:
            raise ValueError("Points cannot be negative")
        self._points = value

    def __str__(self):
        """
        Returns a string representation of the team.

        Returns:
            str: Formatted string with team name and points.
        """
        return f"Team: {self.name} Points: {self.points}"
    
   
    
class Competition:
    """
    A class to manage a collection of Team objects and perform operations like sorting and saving.
    """
    def __init__(self):
        """
        Initializes the Competition with an empty list of teams.
        """
        self.teams = []

    def add_team(self, name, points):
        """
        Creates a new Team object and adds it to the competition list.

        Args:
            name (str): Name of the team.
            points (int): Points of the team.
        """
        self.teams.append(Team(name, points))

    def sort_by_rank(self):
        """
        Sorts the competition teams in descending order based on their points.
        """
        self.teams.sort(key=lambda x: x.points, reverse=True)

    def find_team_by_name(self, search_name):
        """
        Searches for teams in the competition that match the given name (case-insensitive).

        Args:
            search_name (str): The name to search for.

        Returns:
            list: A list of Team objects that match the search name.
        """
        pattern = re.escape(search_name)
        return [t for t in self.teams if re.fullmatch(pattern, t.name, re.IGNORECASE)]
    
    def save_csv(self, filename):
        """
        Saves the current list of teams to a CSV file.

        Args:
            filename (str): The path/name of the file to save data.
        """
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["name", "points"])
            writer.writeheader()
            for t in self.teams:
                writer.writerow(t.to_dict())

    def load_csv(self, filename):
        """
        Loads team data from a CSV file into the competition.

        Args:
            filename (str): The path/name of the file to load.

        Returns:
            bool: True if loading was successful, False if the file does not exist.
        """
        if not os.path.exists(filename): return False
        self.teams = []
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.add_team(row['name'], int(row['points']))
        return True

    def save_pickle(self, filename):
        """
        Serializes the list of team objects to a file using the pickle module.

        Args:
            filename (str): The path/name of the file to save data.
        """
        with open(filename, 'wb') as f:
            pickle.dump(self.teams, f)

    def load_pickle(self, filename):
        """
        Deserializes team objects from a pickle file.

        Args:
            filename (str): The path/name of the file to load.

        Returns:
            bool: True if loading was successful, False if the file does not exist.
        """
        if not os.path.exists(filename): return False
        with open(filename, 'rb') as f:
            self.teams = pickle.load(f)
        return True
  
  
def run_task1():
    """
    The main execution function for Task 1. 
    Manages the user interface menu and coordinates competition operations.
    """
    comp = Competition()
    
    initial_dict = {"Spartak": 15, "Zenit": 20, "Dynamo": 12}
    for n, p in initial_dict.items():
        comp.add_team(n, p)

    while True:
        print("\n--- TASK 1 MENU  ---")
        print("1. Add team")
        print("2. Show board")
        print("3. Find first place")
        print("4. Search by name")
        print("5. CSV (Save/Load)")
        print("6. Pickle (Save/Load)")
        print("0. Back")

        choice = val.get_int_input("\nSelect operation: ")

        if choice == 1:
            try:
                n, p = inp.input_team_data()
                comp.add_team(n, p)
                out.print_message("Team added successfully.")
            except ValueError as e:
                out.print_message(f"Error creation of team: {e}")

        elif choice == 2:
            comp.sort_by_rank()
            out.output_teams_table(comp.teams)

        elif choice == 3:
            comp.sort_by_rank()
            if comp.teams:
                out.print_message(f"First place: {comp.teams[0]}")
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
            while True:
                try:
                    sub = val.get_int_input("1. Save CSV | 2. Load CSV: ")
                    if sub not in [1, 2]:
                        print("Invalid choice. Please enter 1 or 2.")
                        continue
                    fname = inp.input_filename(".csv")
                    full_path = os.path.join(CURRENT_DIR, fname)
                    if sub == 1: 
                        comp.save_csv(full_path)
                        out.print_message("Saved successfully.")
                        break
                    else: 
                        if comp.load_csv(full_path): 
                            out.print_message("Loaded successfully.")
                            break
                        else: 
                            out.print_message("File not found.")
                except (IOError, PermissionError) as e:
                    out.print_message(f"File error: {e}")
                except Exception as e:
                    out.print_message(f"Unexpected error: {e}")

        elif choice == 6:
            while True:
                try:
                    sub = val.get_int_input("1. Save Pickle | 2. Load Pickle: ")
                    if sub not in [1, 2]:
                        print("Invalid choice. Please enter 1 or 2.")
                        continue
                    fname = inp.input_filename(".pkl")
                    full_path = os.path.join(CURRENT_DIR, fname)
                    if sub == 1: 
                        comp.save_pickle(full_path)
                        out.print_message("Saved successfully.")
                        break
                    else: 
                        if comp.load_pickle(full_path): 
                            out.print_message("Loaded successfully.")
                            break
                        else: 
                            out.print_message("File not found.")
                except (pickle.PickleError, EOFError, IOError) as e:
                    out.print_message(f"Serialization error: {e}")

        elif choice == 0:
            break
            
        if not inp.repeat_task():
            break
