from lab_python_oop.GeometricFigure import GeometricFigure
from lab_python_oop.FigureColor import FigureColor


class Rectangle(GeometricFigure):
    typeOfFigure = "Прямоугольник"

    def __init__(self, color, width, height):
        self._width = width
        self._height = height
        self._figure_color = FigureColor()
        self._figure_color.color_property = color

    def _area(self):
        return self._width * self._height

    def __repr__(self):
        return f'{Rectangle.get_figure_type()} {self._figure_color.color_property} цвета шириной {self._width} и высотой {self._height} площадью {self._area()}.'
       
