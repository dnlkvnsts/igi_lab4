import numpy as np
import math
import base.input as inp
import base.output as out



class MathStatsMixin:
    """Mixin for manual calculation of statistical metrics using formulas."""
    
    def calculate_manual_std(self, data_array):
        """Calculates standard deviation using the formula: sqrt(sum(x - mean)^2 / n)."""
        if not data_array:
            return 0.0
        n = len(data_array)
        mean_val = sum(data_array) / n
        sum_sq_diff = sum((x - mean_val) ** 2 for x in data_array)
        return math.sqrt(sum_sq_diff / n)

class MatrixBase:
    """Base class for matrix storage demonstrating static attributes and properties."""
    
    # Static attribute
    DESC = "Base Matrix Object"

    def __init__(self, n, m):
        self._n = n
        self._m = m
        # Create integer matrix using random generator (Requirement a)
        self._matrix = np.random.randint(-50, 50, size=(n, m))

    @property
    def matrix(self):
        """Property: Getter for the matrix."""
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        """Property: Setter for the matrix (demonstrates validation/logic)."""
        if isinstance(value, np.ndarray):
            self._matrix = value

    def display_info(self):
        """Demonstrates polymorphism (can be overridden)."""
        return f"{self.DESC}: {self._n}x{self._m}"

    def __str__(self):
        """Magic method for object string representation."""
        return f"Matrix[{self._n}x{self._m}]"

class NumpyAnalyzer(MatrixBase, MathStatsMixin):
    """Class for advanced matrix analysis using NumPy and Mixins."""
    
    DESC = "Advanced Numpy Analyzer" # Static attribute override

    def __init__(self, n, m):
        # Use super() to initialize parent class
        super().__init__(n, m)

    def demonstrate_numpy_features(self):
        """Shows NumPy features: array creation, slicing, and universal functions."""
        # Specific creation (Requirement a.2)
        zeros = np.zeros((2, 2))
        
        # Slicing (Requirement a.3)
        # Take first 2 rows and 2 columns if matrix is large enough
        rows_limit = min(2, self.matrix.shape[0])
        cols_limit = min(2, self.matrix.shape[1])
        slice_demo = self.matrix[0:rows_limit, 0:cols_limit]
        
        return zeros, slice_demo

    def get_general_stats(self):
        """Requirement b: General mathematical and statistical operations."""
        # Handling potential empty matrix or 1-row matrix for corrcoef
        stats = {
            "Mean (mean)": np.mean(self.matrix),
            "Median (median)": np.median(self.matrix),
            "Variance (var)": np.var(self.matrix),
            "Std Deviation (std)": np.std(self.matrix)
        }
        
        if self.matrix.shape[0] > 1:
            # Correlation coefficient (Requirement b.3)
            stats["CorrCoef (row 0 vs row 1)"] = np.corrcoef(self.matrix[0], self.matrix[1])[0, 1]
            
        return stats

    def solve_individual_task(self):
        """
        Individual task:
        1. Find sum of absolute values of negative odd elements.
        2. Calculate standard deviation in two ways (built-in and formula).
        """
        # Boolean indexing/Slicing to find negative (<0) and odd (%2 != 0)
        mask = (self.matrix < 0) & (self.matrix % 2 != 0)
        target_elements = self.matrix[mask]
        
        if target_elements.size == 0:
            return None

        # Sum of absolute values
        sum_abs = np.sum(np.abs(target_elements))

        # Std Deviation - Method 1: NumPy built-in
        std_numpy = np.std(target_elements)

        # Std Deviation - Method 2: Manual formula (via Mixin)
        std_manual = self.calculate_manual_std(target_elements.tolist())

        return {
            "Negative Odd Elements": target_elements.tolist(),
            "Sum of Absolute Values": sum_abs,
            "Std (Numpy Method)": round(std_numpy, 2),
            "Std (Formula Method)": round(std_manual, 2)
        }

def run_task5():
    """Main execution function for Task 5 testing."""
    while True:
        out.print_message("STARTING TASK 5: NUMPY RESEARCH")
        
        try:
            # Input using your specified function
            n, m = inp.input_matrix_dims()
            
            # Instance of child class
            analyzer = NumpyAnalyzer(n, m)
            print(f"Object Info: {analyzer.display_info()}")
            
            # Display Matrix
            out.output_matrix(analyzer.matrix, "Generated Random Matrix A:")

            # a) Numpy Demo
            zeros_arr, sliced_arr = analyzer.demonstrate_numpy_features()
            print(f"\n--- Numpy Feature Demo ---\nZeros (2x2):\n{zeros_arr}\nSlice (up to 2x2):\n{sliced_arr}")

            # b) Statistical Analysis
            general_stats = analyzer.get_general_stats()
            out.output_stats(general_stats)

            # Individual Task
            ind_results = analyzer.solve_individual_task()
            if ind_results:
                out.print_message("INDIVIDUAL TASK RESULTS")
                out.output_stats(ind_results)
            else:
                out.print_message("No negative odd elements found.")

        except Exception as e:
            # Point 9: Handling exceptions
            print(f"An error occurred: {e}")

        if not inp.repeat_task():
            break