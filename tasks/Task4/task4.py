"""
The task number 4

Lab 4. Working with files, classes, serializers, regular expressions, and
standard libraries

Version: 1

Developer: Danilkova Anastasia Alexandrovna

Date: 17.04.2026
"""


import abc
import math
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import base.output as out
import base.input as inp

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class FileSaverMixin:
    """
    A mixin class that provides functionality to save content to a file.
    """
    def save_description_to_file(self, filename, content):
        """
        Saves the provided text content to a specified file.

        Args:
            filename (str): The full path or name of the file to save.
            content (str): The text content to be written into the file.
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        out.print_message(f"Description saved to {os.path.basename(filename)}")


class Shape(abc.ABC):
    """
    An abstract base class representing a geometric shape.
    """
    def __init__(self, name):
        """
        Initializes the base shape with a name.

        Args:
            name (str): The name of the geometric figure.
        """
        self.name = name
    
    
    @abc.abstractmethod
    def area (self):
        """
        Abstract method to calculate the area of the shape.

        Returns:
            float: The area of the figure.
        """
        pass
    

class FigureColor:
    """
    A class to manage and store the color of a geometric figure.
    """
    def __init__(self, color_name="blue"):
        """
        Initializes the figure color.

        Args:
            color_name (str): Name of the color (default is "blue").
        """
        self._color = color_name

    @property
    def color(self):
        """
        Gets the current color of the figure.

        Returns:
            str: The color name.
        """
        return self._color

    @color.setter
    def color(self, value):
        """
        Sets the color of the figure. If value is empty, defaults to blue.

        Args:
            value (str): The new color name.
        """
        if not value:
            self._color = "blue"
        else:
            self._color = value
            
class Rhomb(Shape, FileSaverMixin):
    """
    A class representing a Rhombus figure. 
    Inherits from Shape (abstraction) and FileSaverMixin (mixin).
    """
    FIGURE_NAME = "Rhomb"  
    instance_count = 0        

    def __init__(self, side, angle, color_name, label_text):
        """
        Initializes a Rhombus instance using side, angle, color and label.

        Args:
            side (float): The length of the side.
            angle (float): The acute angle in degrees.
            color_name (str): The color of the rhomb.
            label_text (str): The text label for the rhomb.
        """
        super().__init__(self.FIGURE_NAME)
        Rhomb.instance_count += 1
        self._side = side
        self._angle = angle  
        self.color_obj = FigureColor(color_name)
        self.label_text = label_text

    @property
    def side(self):
        """
        Gets the side length of the rhomb.

        Returns:
            float: Side length.
        """
        return self._side

    @side.setter
    def side(self, value):
        """
        Sets the side length with validation.

        Args:
            value (float): New side length.

        Raises:
            ValueError: If the side is not a positive number.
        """
        if value <= 0: 
            raise ValueError("Side must be positive")
        self._side = value

    @property
    def angle(self):
        """
        Gets the acute angle of the rhomb.

        Returns:
            float: Angle in degrees.
        """
        return self._angle
    
    @angle.setter
    def angle(self, value):
        """
        Sets the angle with validation.

        Args:
            value (float): New angle in degrees.

        Raises:
            ValueError: If the angle is not between 0 and 90 degrees.
        """
        if not (0 < value < 90):
            raise ValueError("The angle must be between 0 and 90 degrees")
        self._angle = value

    def area(self):
        """
        Calculates the area of the rhomb.

        Returns:
            float: The calculated area rounded to 2 decimal places.
        """
        rad = math.radians(self._angle)
        return round(self._side**2 * math.sin(rad), 2)

    def __str__(self):
        """
        Returns a string representation of the Rhomb instance.

        Returns:
            str: Formatted string with rhomb parameters.
        """
        pattern = "Figure: {0} | Color: {1} | Side: {2} | Angle: {3} | Area: {4} | Number of figures: {5}"
        return pattern.format(
            self.name, 
            self.color_obj.color, 
            self._side, 
            self._angle, 
            self.area(),
            self.instance_count
        )

    @classmethod
    def get_figure_name(cls):
        """
        Returns the class-level figure name.

        Returns:
            str: The FIGURE_NAME attribute.
        """
        return cls.FIGURE_NAME
 
    def get_info(self):
        """
        Wrapper for __str__ to get object information.

        Returns:
            str: Detailed information about the rhomb.
        """
        return self.__str__()

    def draw(self, save_path):
        """
        Renders the rhomb using matplotlib and saves the plot to a file.

        Args:
            save_path (str): The file path where the plot image will be saved.
        """
        a = self._side
        alpha = math.radians(self._angle)
        
        v1 = [0, 0]
        v2 = [a, 0]
        v3 = [a + a * math.cos(alpha), a * math.sin(alpha)]
        v4 = [a * math.cos(alpha), a * math.sin(alpha)]
        
        fig, ax = plt.subplots()
        polygon = patches.Polygon([v1, v2, v3, v4], closed=True, 
                                  linewidth=2, edgecolor='black', 
                                  facecolor=self.color_obj.color)
        
        ax.add_patch(polygon)
        
        ax.set_xlim(-1, v3[0] + 1)
        ax.set_ylim(-1, v3[1] + 1)
        ax.set_aspect('equal')
        
        plt.title(f"{self.FIGURE_NAME}: {self.label_text}")
        plt.text(v1[0], v4[1]/2, self.label_text, fontsize=12, fontweight='bold')
        
        plt.grid(True, linestyle='--')
        plt.savefig(save_path)
        out.print_message(f"Plot saved to {os.path.basename(save_path)}")
        plt.show()
        
        
def run_task4():
    """
    Main execution loop for Task 4. Handles user input, object creation,
    visualization, and exception handling.
    """
    while True:
        out.print_message("Task 4 Rhomb")   
        side, angle, color, label = inp.input_rhomb_data()
        
        try:
                
            rhomb = Rhomb(side, angle, color, label)

            out.print_rhomb_info(rhomb)
            
            txt_path = os.path.join(CURRENT_DIR, "rhomb_info.txt")
            img_path = os.path.join(CURRENT_DIR, "rhomb_plot.png")
            
            rhomb.save_description_to_file(txt_path, rhomb.get_info())
            rhomb.draw(img_path)
            
        except ValueError as ve:
            print(f"\nValueError: {ve}")
            print("please, enter correct data")
        except OSError as oe:
            print(f"OSError: Не удалось сохранить файл. Подробности: {oe}")
        except RuntimeError as re:
            print((f"RuntimeError: Проблема при построении графика. Подробности: {re}"))
            
            

        if not inp.repeat_task():
            break
            
