from model.shape import Shape
from model.point import Point

from PySide6.QtGui import QPainter
from PySide6.QtCore import QRectF, QPoint

import math


class Triangle(Shape):
    def __init__(self, center: Point, side: float):
        super().__init__(center)
        self._side = side

    # TODO: Task 4 - Implement the scale method

    def draw(self, painter: QPainter) -> None:
        # TODO: Task 3 - Implement the drawing mechanism for a triangle
        height = self._side * math.sin(math.pi/3)
        base = self._side * math.cos(math.pi/3)
        point1 = QPoint(self._center.x, self._center.y - height/2)
        point2 = QPoint(self._center.x - base/2, self._center.y + height/2)
        point3 = QPoint(self._center.x + base/2, self._center.y + height/2)
        painter.drawPolygon([point1, point2, point3])

        painter.drawText(self._center.x, self._center.y, str(self._id))

