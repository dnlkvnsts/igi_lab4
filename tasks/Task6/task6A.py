import pandas as pd
import base.input as inp
import base.output as out

class AutoStatsMixin:
    """Mixin to provide statistical summary for any Pandas object."""
    def get_summary(self, data):
        """Returns descriptive statistics of the provided Pandas object."""
        return data.describe()

class PandasTaskBase:
    """
    Base class for Pandas tasks.
    Demonstrates: static attributes, properties, magic methods.
    """
    # Static attribute (Requirement 4.1)
    LIBRARY_NAME = "Pandas"

    def __init__(self, task_name):
        # Dynamic attribute (Requirement 4.1)
        self._task_name = task_name
        self._dataset_name = "Automobile Dataset"

    @property
    def task_name(self):
        """Getter for task_name property (Requirement 4.6)."""
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        """Setter for task_name property (Requirement 4.5)."""
        if value.strip():
            self._task_name = value
        else:
            raise ValueError("Task name cannot be empty")

    def __str__(self):
        """Special magic method (Requirement 4.3)."""
        return f"Task: {self._task_name} using {self.LIBRARY_NAME}"

    def get_info(self):
        """Method to demonstrate polymorphism in child classes (Requirement 4.2)."""
        return f"Basic analysis of {self._dataset_name}"

class CarDataAnalyzer(PandasTaskBase, AutoStatsMixin):
    """
    Main class for Automobile Data analysis.
    Demonstrates: inheritance, super(), and mixins.
    """

    def __init__(self, task_name):
        # Use super() to call parent constructor (Requirement 4.4)
        super().__init__(task_name)

    def get_info(self):
        """Polymorphism: Specialized info for Car Analysis (Requirement 4.2)."""
        return f"Detailed analysis of {self._dataset_name} (Series & DataFrames)"

    def demonstrate_series(self):
        """
        Requirements A.2, A.3, A.5: Series creation and indexing.
        """
        # 3. Create Series from list
        prices = [15000, 28000, 42000, 58000]
        brands = ['Toyota', 'BMW', 'Mercedes', 'Tesla']
        
        # Series Creation
        car_series = pd.Series(data=prices, index=brands)
        
        # 5. Accessing elements using .loc and .iloc
        loc_example = car_series.loc['BMW']   # Label access
        iloc_example = car_series.iloc[1]     # Position access
        
        return car_series, loc_example, iloc_example

    def create_car_dataframe(self):
        """
        Requirement A.6: Create DataFrame 'car_features' from list of lists.
        Set columns and change indices.
        """
        # List of lists (Automobile dataset example)
        data = [
            ['Sedan', 150, 'Petrol', 25000],
            ['SUV', 200, 'Diesel', 45000],
            ['Hatchback', 100, 'Electric', 30000]
        ]
        
        # Define Columns
        columns = ['Body-Style', 'Horsepower', 'Fuel-Type', 'Price']
        
        # Create DataFrame
        car_features = pd.DataFrame(data, columns=columns)
        
        # Change indices to car_A, car_B, car_C
        car_features.index = ['car_A', 'car_B', 'car_C']
        
        return car_features

def run_task6A():
    """Requirement 5, 8: Main function with repeat cycle."""
    while True:
        out.print_message("TASK 6: PANDAS DATA RESEARCH")
        try:
            analyzer = CarDataAnalyzer("Automobile Research")
            print(analyzer)
            print(analyzer.get_info())

            # Task A.2 - A.5
            series_obj, val_loc, val_iloc = analyzer.demonstrate_series()
            out.print_message("Pandas Series Demo")
            print(f"Series:\n{series_obj}")
            print(f"Access .loc['BMW']: {val_loc}")
            print(f"Access .iloc[1]: {val_iloc}")

            # Task A.6
            df = analyzer.create_car_dataframe()
            # Requirement A.4: Use of formatted output
            out.output_dataframe(df, "Car Features (Requirement A.6)")

            # Mixin Use
            stats = analyzer.get_summary(df)
            out.output_dataframe(stats, "Statistical Summary (Mixin)")

        except (ValueError, KeyError, AttributeError) as e:
            
            print(f"\n[!] Data Error: {e}")
        except Exception as e:
            print(f"\n[!] Unexpected Error: {e}")

        if not inp.repeat_task():
            break