from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.FigureColor import FigureColor
import math


class Circle(GeometricFigure):
    typeOfFigure = "Круг"

    def __init__(self, color, radius):
        self.radius = radius
        self.figure_color = FigureColor()
        self.figure_color.color_property = color

    def _area(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return f'{Circle.get_figure_type()} {self.figure_color.color_property} цвета радиусом {self.radius} площадью {self._area()}.'
         
