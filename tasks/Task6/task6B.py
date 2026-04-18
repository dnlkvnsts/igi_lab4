"""
The task number 6B

Lab 4. Working with files, classes, serializers, regular expressions, and
standard libraries

Version: 1

Developer: Danilkova Anastasia Alexandrovna

Date: 17.04.2026
"""

import pandas as pd
import base.input as inp
import base.output as out
import re

class AutoStatsMixin:
    """
    Mixin class that provides utility statistical calculation methods.
    """
    
    def calculate_ratio(self, val1, val2):
        """
        Calculates the ratio between two values and rounds it.

        Args:
            val1 (float): The numerator (e.g., average of expensive cars).
            val2 (float): The denominator (e.g., average of cheap cars).

        Returns:
            float: The calculated ratio rounded to 2 decimal places.

        Raises:
            ZeroDivisionError: If the second value is zero.
        """
        if val2 == 0:
            raise ZeroDivisionError("Cannot divide by zero mileage.")
        return round(val1 / val2, 2)

class PandasTaskBase:
    """
    Base class for tasks involving the Pandas library.
    """

    LIBRARY_NAME = "Pandas"

    def __init__(self, task_name):
        """
        Initializes the base task with a name and dataset info.

        Args:
            task_name (str): The name of the specific task.
        """
        self._task_name = task_name
        self._dataset_name = "Automobile Dataset"

    @property
    def task_name(self):
        """
        Getter for the task name property.

        Returns:
            str: The current task name.
        """
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        """
        Setter for the task name property with validation using regex.

        Args:
            value (str): The new name for the task.

        Raises:
            ValueError: If the provided value is empty or consists only of whitespace.
        """

        if re.search(r'\S', value):
            self._task_name = value
        else:
            raise ValueError("Name cannot be empty or consist only of whitespace")
        
    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: Description of the task and the library used.
        """
        return f"Task: {self._task_name} using {self.LIBRARY_NAME}"

    def get_info(self):
        """
        Provides basic information about the dataset.

        Returns:
            str: Brief info string about the dataset.
        """
        return f"Analysis of {self._dataset_name}"

class CarDataAnalyzer(PandasTaskBase, AutoStatsMixin):
    """
    Specialized class for analyzing automobile data using Pandas.
    Inherits from PandasTaskBase and AutoStatsMixin.
    """
    
    def __init__(self, task_name):
        """
        Initializes the analyzer using the parent constructor.

        Args:
            task_name (str): The name of the analysis task.
        """
        super().__init__(task_name)

    def get_info(self):
        """
        Provides detailed information about the analysis scope (Polymorphism).

        Returns:
            str: Detailed task description.
        """
        return "Task B:  Statistical Analysis"

    def get_full_dataset(self):
        """
        Creates a sample DataFrame representing a collection of cars.

        Returns:
            pd.DataFrame: A DataFrame with brand, cylinders, price, and mpg columns.
        """
      
        data = {
            'brand': ['Toyota', 'BMW', 'Audi', 'Tesla', 'Ford', 'Honda', 'Lexus', 'Mazda'],
            'cylinders': [4, 6, 6, 0, 8, 4, 8, 4],
            'price': [15000, 45000, 42000, 60000, 55000, 18000, 58000, 20000],
            'mpg': [30, 20, 22, 100, 15, 28, 16, 25]
        }
        return pd.DataFrame(data)

    def analyze_cylinders_price(self, df):
        """
        Calculates the average price for cars with the maximum cylinder count.

        Args:
            df (pd.DataFrame): The automobile dataset to analyze.

        Returns:
            tuple: A tuple containing (max_cylinders, average_price).
        """
       
        max_cyl = df['cylinders'].max()
        avg_price = df[df['cylinders'] == max_cyl]['price'].mean()
        return max_cyl, round(avg_price, 2)

    def analyze_mpg_ratio(self, df):
        """
        Compares average MPG between the most expensive and cheapest car quartiles.

        Args:
            df (pd.DataFrame): The automobile dataset to analyze.

        Returns:
            tuple: A tuple containing (expensive_mpg, cheap_mpg, ratio).
        """
        
        q_low = df['price'].quantile(0.25)
        q_high = df['price'].quantile(0.75)

        
        expensive_mpg = df[df['price'] >= q_high]['mpg'].mean()
        cheap_mpg = df[df['price'] <= q_low]['mpg'].mean()

        ratio = self.calculate_ratio(expensive_mpg, cheap_mpg)
        return expensive_mpg, cheap_mpg, ratio

def run_task6B():
    """
    The main execution loop for Task 6B.
    Handles class instantiation, calculations, and repetitive user input.
    """
    while True:
        out.print_message("Task 6B")
        try:
            analyzer = CarDataAnalyzer("Car Stats Lab")
            print(analyzer.get_info())

           
            df = analyzer.get_full_dataset()
            out.output_dataframe(df, "Working Dataset")

            
            max_c, avg_p = analyzer.analyze_cylinders_price(df)
            print(f"\n[Analysis 1]")
            print(f"- Maximum cylinders found: {max_c}")
            print(f"- Average price for these cars: ${avg_p}")

            
            exp_mpg, chp_mpg, ratio = analyzer.analyze_mpg_ratio(df)
            print(f"\nAnalysis 2")
            print(f"- Avg MPG of expensive cars (Top 25% price): {exp_mpg}")
            print(f"- Avg MPG of cheap cars (Bottom 25% price): {chp_mpg}")
            print(f"- Ratio (Expensive MPG / Cheap MPG): {ratio}x")

        except ZeroDivisionError as e:
            print(f"Calculation Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

        if not inp.repeat_task():
            break
