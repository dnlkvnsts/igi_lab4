"""
The task number 6A

Lab 4. Working with files, classes, serializers, regular expressions, and
standard libraries

Version: 1

Developer: Danilkova Anastasia Alexandrovna

Date: 17.04.2026
"""


import pandas as pd
import base.input as inp
import base.output as out

class AutoStatsMixin:
    def get_summary(self, data):
        """
        Generates descriptive statistics for a given DataFrame.

        Args:
            data (pd.DataFrame): The DataFrame to analyze.

        Returns:
            pd.DataFrame: A summary containing count, mean, std, min, max, etc.
        """
        return data.describe().round(2)

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
        Setter for the task name property with validation.

        Args:
            value (str): The new name for the task.

        Raises:
            ValueError: If the provided value is empty or consists only of whitespace.
        """
        if value.strip():
            self._task_name = value
        else:
            raise ValueError("Task name cannot be empty")

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
        return f"Basic analysis of {self._dataset_name}"

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
            str: Detailed info string.
        """
        return f"Detailed analysis of {self._dataset_name} (Series & DataFrames)"

    def create_series(self):
        """
        Creates a Pandas Series and demonstrates indexing.

        Returns:
            tuple: A tuple containing:
                - car_series (pd.Series): The created series.
                - loc_example (int): Value accessed by label.
                - iloc_example (int): Value accessed by position.
        """
        prices = [15000, 28000, 42000, 58000]
        brands = ['Toyota', 'BMW', 'Mercedes', 'Tesla']
        car_series = pd.Series(data=prices, index=brands)
        loc_example = car_series.loc['BMW']
        iloc_example = car_series.iloc[1]
        return car_series, loc_example, iloc_example

    def create_car_dataframe(self):
        """
        Creates a DataFrame from a list of lists and sets custom indexes.

        Returns:
            pd.DataFrame: The resulting DataFrame with specified columns and row labels.
        """
        data = [
            ['Sedan', 150, 'Petrol', 25000],
            ['SUV', 200, 'Diesel', 45000],
            ['Hatchback', 100, 'Electric', 30000]
        ]
        columns = ['Body-Style', 'Horsepower', 'Fuel-Type', 'Price']
        car_features = pd.DataFrame(data, columns=columns)
        car_features.index = ['car_A', 'car_B', 'car_C']
        return car_features

def run_task6A():
    """
    The main execution loop for Task 6A. 
    Handles class instantiation, data processing, and repetition logic.
    """
    while True:
        out.print_message("Task 6A: ")
        try:
            analyzer = CarDataAnalyzer("Automobile Research")
            print(analyzer)
            print(analyzer.get_info())

            series_obj, val_loc, val_iloc = analyzer.create_series()
            print(f"\n--- Pandas Series ---")
            print(series_obj)
            print(f"Access via .loc['BMW']: {val_loc}")
            print(f"Access via .iloc[1]: {val_iloc}")
            
            df_small = analyzer.create_car_dataframe()
            out.output_dataframe(df_small, "DataFrame 'car_features' ")

            print("\n--- Statistics  ---")
            print(analyzer.get_summary(df_small))

        except (ValueError, KeyError, AttributeError) as e:
            print(f"\n Error: {e}")
        except Exception as e:
            print(f"\n Unexpected Error: {e}")

        if not inp.repeat_task():
            break