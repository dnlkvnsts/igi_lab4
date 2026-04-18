"""
The task number 5

Lab 4. Working with files, classes, serializers, regular expressions, and
standard libraries

Version: 1

Developer: Danilkova Anastasia Alexandrovna

Date: 17.04.2026
"""


import numpy as np
import math
import base.input as inp
import base.output as out



class MathStatsMixin:
    """
    Mixin for manual calculation of statistical metrics using mathematical formulas.
    """
    
    def calculate_manual_std(self, data_array):
        """
        Calculates the standard deviation using the mathematical formula: sqrt(sum(x - mean)^2 / n).

        Args:
            data_array (list): A list of numerical values to analyze.

        Returns:
            float: The calculated standard deviation. Returns 0.0 if the list is empty.
        """
        if not data_array:
            return 0.0
        n = len(data_array)
        mean_val = sum(data_array) / n
        sum_sq_diff = sum((x - mean_val) ** 2 for x in data_array)
        return math.sqrt(sum_sq_diff / n)

class MatrixBase:
    """
    Base class for matrix storage demonstrating static attributes and property usage.
    """
    
    DESC = "Base Matrix Object"

    def __init__(self, n, m):
        """
        Initializes the matrix object with random integers and sets its dimensions.

        Args:
            n (int): The number of rows in the matrix.
            m (int): The number of columns in the matrix.
        """
        self._n = n
        self._m = m
        self._matrix = np.random.randint(-50, 50, size=(n, m))

    @property
    def matrix(self):
        """
        Provides access to the internal NumPy matrix.

        Returns:
            np.ndarray: The current matrix storage.
        """
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        """
        Updates the matrix with a new NumPy array after validation.

        Args:
            value (np.ndarray): The new NumPy array to be stored.
        """
        if isinstance(value, np.ndarray):
            self._matrix = value

    def display_info(self):
        """
        Returns basic information about the matrix dimensions.

        Returns:
            str: A formatted string containing the description and dimensions.
        """
        return f"{self.DESC}: {self._n}x{self._m}"

    def __str__(self):
        """
        Returns a string representation of the matrix object for printing.

        Returns:
            str: A string in the format Matrix[n x m].
        """
        return f"Matrix[{self._n}x{self._m}]"
    
    def values(self):
        """
        Implementation of 'values()'.
        
        Returns:
            the matrix data as a standard nested list.
        """
        return self._matrix.tolist()

class NumpyAnalyzer(MatrixBase, MathStatsMixin):
    """
    Class for advanced matrix analysis using NumPy capabilities and Mixin methods.
    """
 
    DESC = "Numpy Analyzer" 

    def __init__(self, n, m):
        """
        Initializes the analyzer by calling the parent MatrixBase constructor.

        Args:
            n (int): The number of rows.
            m (int): The number of columns.
        """
        super().__init__(n, m)

    def demonstrate_numpy_features(self):
        """
        Demonstrates NumPy features such as specific array creation and slicing.

        Returns:
            tuple: A tuple containing a zeros matrix and a sliced portion of the main matrix.
        """
        
        
        simple_list = [10, 20, 30, 40, 50]
        arr_from_list = np.array(simple_list)
        matrix_values = self.values()
        
        
        zeros = np.zeros((2, 2))
        
        rows_limit = min(2, self.matrix.shape[0])
        cols_limit = min(2, self.matrix.shape[1])
        slice_demo = self.matrix[0:rows_limit, 0:cols_limit]
        
        return arr_from_list, matrix_values, zeros, slice_demo

    def get_general_stats(self):
        """
        Calculates general statistical metrics for the entire matrix.

        Returns:
            dict: A dictionary containing mean, median, variance, and standard deviation.
        """
        stats = {
            "Mean (mean)": np.mean(self.matrix),
            "Median (median)": np.median(self.matrix),
            "Variance (var)": np.var(self.matrix),
            "Std Deviation (std)": np.std(self.matrix)
        }
        
        if self.matrix.shape[0] > 1:
            stats["CorrCoef (row 0 vs row 1)"] = np.corrcoef(self.matrix[0], self.matrix[1])[0, 1]
            
        return stats

    def solve_individual_task(self):
        """
        Executes the individual task: filters negative odd elements and calculates their stats.

        Returns:
            dict: A dictionary with the list of elements, their absolute sum, and two types of std.
            None: If no negative odd elements are found.
        """
        
        mask = (self.matrix < 0) & (self.matrix % 2 != 0)
        target_elements = self.matrix[mask]
        
        if target_elements.size == 0:
            return None

        sum_abs = np.sum(np.abs(target_elements))

        std_numpy = np.std(target_elements)

        std_manual = self.calculate_manual_std(target_elements.tolist())

        return {
            "Negative Odd Elements": target_elements.tolist(),
            "Sum of Absolute Values": sum_abs,
            "Std (Numpy Method)": round(std_numpy, 2),
            "Std (Formula Method)": round(std_manual, 2)
        }

def run_task5():
    """
    Main execution loop for Task 5. Handles input, object creation, and result display.

    """
    while True:
        out.print_message("Task 5")
        
        try:
            n, m = inp.input_matrix_dims()

            analyzer = NumpyAnalyzer(n, m)
            print(f"Info: {analyzer.display_info()}")
            
            out.output_matrix(analyzer.matrix, "Random Matrix :")

            
            arr_from_list,mat_vals,zeros_arr, sliced_arr = analyzer.demonstrate_numpy_features()
            print(f"\n--- Numpy ---")
            print(f"Array from list (np.array): {arr_from_list}")
            print(f"Values (as standard list): {mat_vals}")
            print(f"Zeros Matrix (2x2):\n{zeros_arr}")         
            print(f"Slice of main matrix (up to 2x2):\n{sliced_arr}") 

            general_stats = analyzer.get_general_stats()
            out.output_stats(general_stats)

            
            ind_results = analyzer.solve_individual_task()
            if ind_results:
                out.output_stats(ind_results)
            else:
                out.print_message("No negative odd elements found.")

        except ValueError as ve:
            print(f"Input Error: {ve}")
        except MemoryError:
            print("\nError: The matrix size is too large to fit in memory.")
        except KeyboardInterrupt:
            print("\nProgram execution interrupted by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        if not inp.repeat_task():
            break