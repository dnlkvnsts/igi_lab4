import pandas as pd
import base.input as inp
import base.output as out

class AutoStatsMixin:
    def get_summary(self, data):
        return data.describe()

class PandasTaskBase:
    LIBRARY_NAME = "Pandas"

    def __init__(self, task_name):
        self._task_name = task_name
        self._dataset_name = "Automobile Dataset"

    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        if value.strip():
            self._task_name = value
        else:
            raise ValueError("Task name cannot be empty")

    def __str__(self):
        return f"Task: {self._task_name} using {self.LIBRARY_NAME}"

    def get_info(self):
        return f"Basic analysis of {self._dataset_name}"

class CarDataAnalyzer(PandasTaskBase, AutoStatsMixin):
    def __init__(self, task_name):
        super().__init__(task_name)

    def get_info(self):
        return f"Detailed analysis of {self._dataset_name} (Series & DataFrames)"

    def create_series(self):
        prices = [15000, 28000, 42000, 58000]
        brands = ['Toyota', 'BMW', 'Mercedes', 'Tesla']
        car_series = pd.Series(data=prices, index=brands)
        loc_example = car_series.loc['BMW']
        iloc_example = car_series.iloc[1]
        return car_series, loc_example, iloc_example

    def create_car_dataframe(self):
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
    while True:
        out.print_message("TASK 6: PART A - PANDAS STRUCTURES")
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
            out.output_dataframe(df_small, "DataFrame 'car_features' (Task A.6)")

            print("\n--- Summary Statistics (Mixin) ---")
            print(analyzer.get_summary(df_small))

        except (ValueError, KeyError, AttributeError) as e:
            print(f"\n Error: {e}")
        except Exception as e:
            print(f"\n Unexpected Error: {e}")

        if not inp.repeat_task():
            break