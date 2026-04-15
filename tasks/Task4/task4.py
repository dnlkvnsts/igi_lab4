import abc
import math
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import base.validation as val
import base.output as out
import base.input as inp

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class FileSaverMixin:
    def save_description_to_file(self, filename, content):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        out.print_message(f"Description saved to {os.path.basename(filename)}")


class Shape(abc.ABC):
    @abc.abstractmethod
    def area (self): pass
    

class FigureColor:
    def __init__(self, color_name="blue"):
        self._color = color_name

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not value:
            self._color = "blue"
        else:
            self._color = value
            
class Rhomb(Shape, FileSaverMixin):
    FIGURE_NAME = "Rhomb"  
    instance_count = 0        

    def __init__(self, side, angle, color_name, label_text):
        Rhomb.instance_count += 1
        self._side = side
        self._angle = angle  
        self.color_obj = FigureColor(color_name)
        self.label_text = label_text

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value <= 0: 
            raise ValueError("Side must be positive")
        self._side = value

    @property
    def angle(self):
        return self._angle
    
    @angle.setter
    def angle(self, value):
        if not (0 < value < 90):
            raise ValueError("The angle must be between 0 and 90 degrees")
        self._angle = value

    def area(self):
        rad = math.radians(self._angle)
        return round(self._side**2 * math.sin(rad), 2)

    def __str__(self):
        pattern = "Figure: {0} | Color: {1} | Side: {2} | Angle: {3}° | Area: {4}"
        return pattern.format(
            self.FIGURE_NAME, 
            self.color_obj.color, 
            self._side, 
            self._angle, 
            self.area()
        )

    def get_info(self):
        return self.__str__()

    def draw(self, save_path):
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
            
        except Exception as e:
            print(f"Error: {e}")

        if not inp.repeat_task():
            break
            
