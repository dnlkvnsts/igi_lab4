import math
import statistics
import matplotlib.pyplot as plt
import os
import base.validation as val
import base.output as out
import base.input as inp

class StatsMixin:
    def calculate_stats(self, data_sequence):
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
    def __init__(self, x_start, x_end, step, eps):
        
        self.x_start = x_start
        self.x_end = x_end
        self.step = step
        self.eps = eps

    @property
    def x_start(self):
        return self._x_start

    @x_start.setter
    def x_start(self, value):
        self._x_start = value

    @property
    def x_end(self):
        return self._x_end

    @x_end.setter
    def x_end(self, value):
        self._x_end = value

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        if value <= 0:
            raise ValueError("Step must be positive!")
        self._step = value

    @property
    def eps(self):
        return self._eps

    @eps.setter
    def eps(self, value):
        if value <= 0 or value >= 1:
            raise ValueError("Precision (eps) must be between 0 and 1!")
        self._eps = value

    def __str__(self):
        
        return f"Function range: [{self.x_start}, {self.x_end}] with step {self.step}"


class SinAnalyzer(MathFunction, StatsMixin):
    def __init__(self, x_start, x_end, step, eps):
        super().__init__(x_start, x_end, step, eps)
        self.results = []

    def calculate_sine_series(self, x, eps):
        n = 0
        term = x
        sum_sin = term
        while abs(term) > eps and n < 1000:
            n += 1
            term *= -x**2 / ((2 * n) * (2 * n + 1))
            sum_sin += term
        return sum_sin, n

    def process(self):
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
        
        plt.annotate('Origin', xy=(0, 0), xytext=(0.5, 0.5),
             arrowprops=dict(
                 arrowstyle='->',  
                 color='black',   
                 lw=1.5            
             ))
        
        
        plt.text(x_vals[0], y_taylor[0], f"Start eps={self.eps}")
        
        plt.savefig(save_path)
        out.print_message(f"Plot saved to {save_path}")
        plt.show()

def run_task3():
    while True:
        try:
            out.print_message("TASK 3: TAYLOR SERIES (SIN X)")
            
            x_start = val.get_float_input("Enter X start: ")
            x_end = val.get_float_input("Enter X end: ")
            step = val.get_float_positive_input("Enter step: ")
            eps = val.get_float_positive_input("Enter precision (eps): ")

           
            analyzer = SinAnalyzer(x_start, x_end, step, eps)
            print(f"\n[i] {analyzer}")

            data = analyzer.process()
            out.output_math_table(data)

            sequence_fx = [r['f_x'] for r in data]
            stats = analyzer.calculate_stats(sequence_fx)
            out.output_statistics(stats)

            analyzer.build_plot()

        except ValueError as e:
            print(f"\n[!] Input Error: {e}")

        if not inp.repeat_task():
            break
