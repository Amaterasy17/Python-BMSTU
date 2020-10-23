from abc import ABC, abstractmethod


class GeometricFigure(ABC):
    typeOfFigure = None

    @classmethod
    def get_figure_type(cls):
        return cls.typeOfFigure

    @abstractmethod
    def _area(self):
        pass
