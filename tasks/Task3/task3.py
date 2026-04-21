"""
The task number 3

Lab 4. Working with files, classes, serializers, regular expressions, and
standard libraries

Version: 1

Developer: Danilkova Anastasia Alexandrovna

Date: 17.04.2026
"""


import math
import statistics
import matplotlib.pyplot as plt
import os
import base.validation as val
import base.output as out
import base.input as inp


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class StatsMixin:
    """
    A mixin class providing statistical calculation methods.
    """
    def calculate_stats(self, data_sequence):
        """
        Calculates basic statistics for a given sequence of numbers.

        Args:
            data_sequence (list): A list of float numbers.

        Returns:
            dict: A dictionary containing Mean, Median, Mode, Variance, and Std Deviation.
        """
        if not data_sequence:
            return {}
        return {
            "Mean": statistics.mean(data_sequence),
            "Median": statistics.median(data_sequence),
            "Mode": statistics.mode(data_sequence),
            "Variance": statistics.variance(data_sequence) if len(data_sequence) > 1 else 0,
            "Std Deviation": statistics.stdev(data_sequence) if len(data_sequence) > 1 else 0
        }


class MathFunction:
    """
    Base class representing a mathematical function range and precision.
    """
    def __init__(self, x_start, x_end, step, eps):
        """
        Initializes the math function parameters.

        Args:
            x_start (float): Start of the interval.
            x_end (float): End of the interval.
            step (float): Increment step.
            eps (float): Precision for calculations.
        """
        self.x_start = x_start
        self.x_end = x_end
        self.step = step
        self.eps = eps

    @property
    def x_start(self):
        """
        Gets the starting value of the interval.

        Returns:
            float: The value of the interval start.
        """
        return self._x_start

    @x_start.setter
    def x_start(self, value):
        """
        Sets the starting value of the interval.

        Args:
            value (float): New starting value.
        """
        self._x_start = value

    @property
    def x_end(self):
        """
        Gets the ending value of the interval.

        Returns:
            float: The value of the interval end.
        """
        return self._x_end

    @x_end.setter
    def x_end(self, value):
        """
        Sets the ending value of the interval.

        Args:
            value (float): New ending value.
        """
        self._x_end = value

    @property
    def step(self):
        """
        Gets the calculation step.

        Returns:
            float: The current step value.
        """
        return self._step

    @step.setter
    def step(self, value):
        """
        Sets the calculation step and validates that it is positive.

        Args:
            value (float): New step value (must be > 0).

        Raises:
            ValueError: If the step is zero or negative.
        """
        if value <= 0:
            raise ValueError("Step must be positive!")
        self._step = value

    @property
    def eps(self):
        """
        Gets the precision value (epsilon).

        Returns:
            float: The current precision threshold.
        """
        return self._eps

    @eps.setter
    def eps(self, value):
        """
        Sets the precision value and validates its range.

        Args:
            value (float): New precision value (must be between 0 and 1).

        Raises:
            ValueError: If the value is outside the (0, 1) range.
        """
        if value <= 0 or value >= 1:
            raise ValueError("Precision (eps) must be between 0 and 1!")
        self._eps = value

    def __str__(self):
        """
        Returns a string representation of the function range.

        Returns:
            str: Formatted string with range and step.
        """
        return f"Function range: [{self.x_start}, {self.x_end}] with step {self.step}"


class SinAnalyzer(MathFunction, StatsMixin):
    """
    Analyzer for sine function using Taylor series expansion.
    """
    def __init__(self, x_start, x_end, step, eps):
        """
        Initializes the analyzer with range and precision parameters.
        """
        super().__init__(x_start, x_end, step, eps)
        self.results = []

    def calculate_sine_series(self, x, eps):
        """
        Calculates the sine of x using Taylor series expansion.

        Args:
            x (float): The value in radians.
            eps (float): The precision threshold.

        Returns:
            tuple: (sum_sin, n) where sum_sin is the result and n is the number of terms.
        """
        n = 0
        term = x
        sum_sin = term
        while abs(term) > eps and n < 1000:
            n += 1
            term *= -x**2 / ((2 * n) * (2 * n + 1))
            sum_sin += term
        return sum_sin, n

    def process(self):
        """
        Executes calculations over the specified range.

        Returns:
            list: A list of dictionaries containing calculation results for each step.
        """
        self.results = []
        
        curr_x = self.x_start
        while curr_x <= self.x_end + 0.000001:
            f_x, n = self.calculate_sine_series(curr_x, self.eps)
            math_x = math.sin(curr_x)
            self.results.append({
                "x": curr_x,
                "n": n,
                "f_x": f_x,
                "math_x": math_x,
                "eps": self.eps
            })
            curr_x += self.step
        return self.results

    def build_plot(self, save_path="plot_task3.png"):
        """
        Creates and saves a comparison plot between Taylor series and math.sin.

        Args:
            save_path (str): The file path where the plot will be saved.
        """
        
        if not self.results:
            print("No data available to build a plot.")
            return

        try:
            x_vals = [r['x'] for r in self.results]
            y_taylor = [r['f_x'] for r in self.results]
            y_math = [r['math_x'] for r in self.results]

            plt.figure(figsize=(10, 6))
            plt.plot(x_vals, y_taylor, 'ro-', label='Taylor F(x)', markersize=4)
            plt.plot(x_vals, y_math, 'b--', label='Math sin(x)', linewidth=2)
            
            plt.axhline(0, color='black', linewidth=1)
            plt.axvline(0, color='black', linewidth=1)
            plt.grid(True, linestyle=':')
            
            plt.title("Taylor Series Comparison: sin(x)")
            plt.xlabel("X Axis")
            plt.ylabel("Y Axis")
            plt.legend()
            
            plt.annotate('Origin', xy=(0, 0), xytext=(0.1, 0.1),
                         arrowprops=dict(
                             arrowstyle='->',  
                             color='black',   
                             lw=1.5            
                         ))
            
            plt.text(x_vals[1], y_taylor[0], f"Start eps={self.eps}")
            
            
            plt.savefig(save_path)
            out.print_message(f"Plot saved to {save_path}")
            plt.show()

        except PermissionError:
            print(f"Error: Permission denied. Cannot save plot to '{save_path}'. "
                  "Close the file if it is open in another program.")
        except FileNotFoundError:
            print(f"Error: The directory for '{save_path}' does not exist.")
        except Exception as e: 
            print(f"An unexpected error occurred while building the plot: {e}")
        finally:
            plt.close()

def run_task3():
    """
    Main loop for Task 3: handles user input, processing, and output.
    
    This function coordinates the interactive part of the application, 
    ensuring data validation and repeat capability.
    """
    while True:
        try:
            out.print_message("Task 3")
            
            x_start = val.get_float_input("Enter X start: ")
            x_end = val.get_float_input("Enter X end: ")
            step = val.get_float_positive_input("Enter step: ")
            eps = val.get_float_positive_input("Enter precision (eps): ")

           
            analyzer = SinAnalyzer(x_start, x_end, step, eps)
            print(f"\n {analyzer}")

            data = analyzer.process()
            out.output_math_table(data)

            sequence_fx = [r['f_x'] for r in data]
            stats = analyzer.calculate_stats(sequence_fx)
            out.output_statistics(stats)

            plot_filename = os.path.join(CURRENT_DIR, "plot_task3.png")
            analyzer.build_plot(plot_filename)

        except ValueError as e:
            print(f"\nInput Error: {e}")

        if not inp.repeat_task():
            break
