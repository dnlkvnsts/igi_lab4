
import pandas as pd
import base.input as inp
import base.output as out

class AutoStatsMixin:
    
    def calculate_ratio(self, val1, val2):
        if val2 == 0:
            raise ZeroDivisionError("Cannot divide by zero mileage.")
        return round(val1 / val2, 2)

class PandasTaskBase:
    
    LIBRARY_NAME = "Pandas"

    def __init__(self, task_name):
        self._task_name = task_name
        self._dataset_name = "Automobile Dataset"

    @property
    def task_name(self): return self._task_name

    @task_name.setter
    def task_name(self, value):
        if value.strip(): self._task_name = value
        else: raise ValueError("Name cannot be empty")

    def __str__(self):
        return f"Task: {self._task_name} using {self.LIBRARY_NAME}"

    def get_info(self):
        return f"Analysis of {self._dataset_name}"

class CarDataAnalyzer(PandasTaskBase, AutoStatsMixin):
    
    def __init__(self, task_name):
        super().__init__(task_name)

    def get_info(self): # Polymorphism
        return "Executing Task B: Advanced Statistical Analysis"

    def get_full_dataset(self):
      
        data = {
            'brand': ['Toyota', 'BMW', 'Audi', 'Tesla', 'Ford', 'Honda', 'Lexus', 'Mazda'],
            'cylinders': [4, 6, 6, 0, 8, 4, 8, 4],
            'price': [15000, 45000, 42000, 60000, 55000, 18000, 58000, 20000],
            'mpg': [30, 20, 22, 100, 15, 28, 16, 25]
        }
        return pd.DataFrame(data)

    def analyze_cylinders_price(self, df):
       
        max_cyl = df['cylinders'].max()
        avg_price = df[df['cylinders'] == max_cyl]['price'].mean()
        return max_cyl, round(avg_price, 2)

    def analyze_mpg_ratio(self, df):
        
        q_low = df['price'].quantile(0.25)
        q_high = df['price'].quantile(0.75)

        # Most expensive (top quartile)
        expensive_mpg = df[df['price'] >= q_high]['mpg'].mean()
        # Cheapest (bottom quartile)
        cheap_mpg = df[df['price'] <= q_low]['mpg'].mean()

        ratio = self.calculate_ratio(expensive_mpg, cheap_mpg)
        return expensive_mpg, cheap_mpg, ratio

def run_task6B():
    while True:
        out.print_message("TASK 6: PART B - STATISTICAL ANALYSIS")
        try:
            analyzer = CarDataAnalyzer("Car Stats Lab")
            print(analyzer.get_info())

            # 1. Prepare Data
            df = analyzer.get_full_dataset()
            out.output_dataframe(df, "Working Dataset")

            # 2. Analysis: Max Cylinders vs Price
            max_c, avg_p = analyzer.analyze_cylinders_price(df)
            print(f"\n[Analysis 1]")
            print(f"- Maximum cylinders found: {max_c}")
            print(f"- Average price for these cars: ${avg_p}")

            # 3. Analysis: MPG Ratio (Quartiles)
            exp_mpg, chp_mpg, ratio = analyzer.analyze_mpg_ratio(df)
            print(f"\n[Analysis 2]")
            print(f"- Avg MPG of expensive cars (Top 25% price): {exp_mpg}")
            print(f"- Avg MPG of cheap cars (Bottom 25% price): {chp_mpg}")
            print(f"- Ratio (Expensive MPG / Cheap MPG): {ratio}x")

        except ZeroDivisionError as e:
            print(f"Calculation Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

        if not inp.repeat_task():
            break
