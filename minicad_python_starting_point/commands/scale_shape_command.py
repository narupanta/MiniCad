from commands.command import Command

from model.circle import Circle
from model.point import Point
from model.shape import Shape

class ScaleShapeCommand(Command):
    def __init__(self, shape: Shape, scalingFactor: float):
        self._shape = shape
        self._scalingFactor = scalingFactor

    def execute(self) -> None:
        self._shape.scale(self._scalingFactor)

    def undo(self) -> None:
        self._shape.scale(1 / self._scalingFactor)

    def redo(self) -> None:
        self.execute()
         