from typing import Callable, Optional

from PySide6.QtWidgets import QDialog, QLineEdit, QDialogButtonBox, QDialogButtonBox, QFormLayout, QWidget, QDoubleSpinBox, QSpinBox, QLabel, QGridLayout
from PySide6.QtGui import QPainter, QPaintEvent, QIntValidator, QDoubleValidator

from model.shape import Shape
from model.circle import Circle
from model.point import Point
from model.square import Square
from model.triangle import Triangle
from model.rectangle import Rectangle

from commands.scale_shape_command import ScaleShapeCommand
from commands.translate_shape_command import TranslateShapeCommand
from commands.command_stack import CommandStack
from commands.create_shape_command import CreateShapeCommand
from commands.clear_shape_command import ClearShapeCommand

class InputCircleDialog(QDialog):

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.x_field = QLineEdit(self)
        self.x_field.setValidator(QIntValidator(0, 1000, self))

        self.y_field = QLineEdit(self)
        self.y_field.setValidator(QIntValidator(0, 1000, self))
        self.radius_field = QLineEdit(self)
        self.radius_field.setValidator(QIntValidator(0, 1000, self))

        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("X", self.x_field)
        layout.addRow("Y", self.y_field)
        layout.addRow("radius", self.radius_field)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self) -> tuple[int, int, int]:
        return (int(self.x_field.text()), int(self.y_field.text()), int(self.radius_field.text()))


def create_circle(shapes: list[Shape], command_stack: CommandStack) -> None:
    dialog = InputCircleDialog()
    if dialog.exec():
        circle = Circle(Point(dialog.getInputs()[0], dialog.getInputs()[1]), dialog.getInputs()[2])
        command = CreateShapeCommand(circle, shapes)
        command_stack.execute(command)


class InputSquareDialog(QDialog):

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.x_field = QLineEdit(self)
        self.x_field.setValidator(QIntValidator(0, 1000, self))

        self.y_field = QLineEdit(self)
        self.y_field.setValidator(QIntValidator(0, 1000, self))
        self.side_field = QLineEdit(self)
        self.side_field.setValidator(QIntValidator(0, 1000, self))

        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("X", self.x_field)
        layout.addRow("Y", self.y_field)
        layout.addRow("side", self.side_field)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self) -> tuple[int, int, int]:
        return (int(self.x_field.text()), int(self.y_field.text()), int(self.side_field.text()))

def create_square(shapes: list[Shape], command_stack: CommandStack) -> None:
    dialog = InputSquareDialog()
    if dialog.exec():
        square = Square(Point(dialog.getInputs()[0], dialog.getInputs()[1]), dialog.getInputs()[2])
        command = CreateShapeCommand(square, shapes)
        command_stack.execute(command)

# TODO: Task 2 - Implement the InputRectangleDialog class and the create_rectangle function
class InputRectangleDialog(QDialog):

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.x_field = QLineEdit(self)
        self.x_field.setValidator(QIntValidator(0, 1000, self))

        self.y_field = QLineEdit(self)
        self.y_field.setValidator(QIntValidator(0, 1000, self))
        self.width_field = QLineEdit(self)
        self.width_field.setValidator(QIntValidator(0, 1000, self))
        self.height_field = QLineEdit(self)
        self.height_field.setValidator(QIntValidator(0, 1000, self))

        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("X", self.x_field)
        layout.addRow("Y", self.y_field)
        layout.addRow("width", self.width_field)
        layout.addRow("height", self.height_field)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self) -> tuple[int, int, int, int]:
        return (int(self.x_field.text()), int(self.y_field.text()), int(self.width_field.text()), int(self.height_field.text()))

def create_rectangle(shapes: list[Shape], command_stack: CommandStack) -> None:
    dialog = InputRectangleDialog()
    if dialog.exec():
        rectangle = Rectangle(Point(dialog.getInputs()[0], dialog.getInputs()[1]), dialog.getInputs()[2], dialog.getInputs()[3])
        command = CreateShapeCommand(rectangle, shapes)
        command_stack.execute(command)

class InputTriangleDialog(QDialog):

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self.x_field = QLineEdit(self)
        self.x_field.setValidator(QIntValidator(0, 1000, self))

        self.y_field = QLineEdit(self)
        self.y_field.setValidator(QIntValidator(0, 1000, self))
        self.side_field = QLineEdit(self)
        self.side_field.setValidator(QIntValidator(0, 1000, self))

        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("X", self.x_field)
        layout.addRow("Y", self.y_field)
        layout.addRow("side", self.side_field)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self) -> tuple[int, int, int]:
        return (int(self.x_field.text()), int(self.y_field.text()), int(self.side_field.text()))

def create_triangle(shapes: list[Shape], command_stack: CommandStack) -> None:
    dialog = InputTriangleDialog()
    if dialog.exec():
        triangle = Triangle(Point(dialog.getInputs()[0], dialog.getInputs()[1]), dialog.getInputs()[2])
        command = CreateShapeCommand(triangle, shapes)
        command_stack.execute(command)

class TranslateShapeDialog(QDialog):

    def __init__(self, numberOfShapes: int, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.shapeNumber = QSpinBox(self)
        # self.shapeNumber.setMaximum(numberOfShapes - 1)
        self.shapeNumber.setMinimum(0)

        max_value = 1000

        self.delta_x = QSpinBox(self)
        self.delta_x.setMaximum(max_value)
        self.delta_x.setMinimum(-max_value)

        self.delta_y = QSpinBox(self)
        self.delta_y.setMaximum(max_value)
        self.delta_y.setMinimum(-max_value)

        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("shape number", self.shapeNumber)
        layout.addRow("delta x", self.delta_x)
        layout.addRow("delta y", self.delta_y)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self) -> tuple[int, int, int]:
        return (self.shapeNumber.value(), self.delta_x.value(), self.delta_y.value())

def translate(shapes: list[Shape], command_stack: CommandStack) -> None:
    if(len(shapes) == 0):
        return

    dialog = TranslateShapeDialog(shapes.__len__())
    if dialog.exec():
        number = dialog.getInputs()[0]
        delta_x = dialog.getInputs()[1]
        delta_y = dialog.getInputs()[2]

        shape = shapes[number]
        command = TranslateShapeCommand(shape, delta_x, delta_y)
        command_stack.execute(command)


# TODO: Task 4 - Implement the ScaleShapeDialog class and the scale function
class ScaleShapeDialog(QDialog):

    def __init__(self, numberOfShapes: int, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.shapeNumber = QSpinBox(self)
        self.shapeNumber.setMaximum(numberOfShapes - 1)
        self.shapeNumber.setMinimum(0)

        max_value = 1000

        self.scaleFactor = QSpinBox(self)
        self.scaleFactor.setMaximum(max_value)
        self.scaleFactor.setMinimum(-max_value)

        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("shape number", self.shapeNumber)
        layout.addRow("scale factor", self.scaleFactor)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self) -> tuple[int, int, int]:
        return (self.shapeNumber.value(), self.scaleFactor.value())

def scale(shapes: list[Shape], command_stack: CommandStack) -> None:
    if(len(shapes) == 0):
        return

    dialog = ScaleShapeDialog(shapes.__len__())
    if dialog.exec():
        number = dialog.getInputs()[0]
        scale_factor = dialog.getInputs()[1]

        shape = shapes[number]
        command = ScaleShapeCommand(shape, scale_factor)
        command_stack.execute(command)

class ClearShapeDialog(QDialog):

    def __init__(self, numberOfShapes: int, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.shapeNumber = QSpinBox(self)
        self.shapeNumber.setMaximum(numberOfShapes - 1)
        self.shapeNumber.setMinimum(0)

        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("shape number", self.shapeNumber)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self) -> int:
        return self.shapeNumber.value()

def clear(shapes: list[Shape], command_stack: CommandStack) -> None:
    if(len(shapes) == 0):
        return

    dialog = ClearShapeDialog(shapes.__len__())
    if dialog.exec():
        number = dialog.getInputs()

        command = ClearShapeCommand(number, shapes)
        command_stack.execute(command)



class ActionFactory:
    
        def __init__(self, shapes: list[Shape], command_stack: CommandStack) -> None:
            self.dialogs: dict[str, Callable[[list[Shape], CommandStack], None]] = {}
            self.shapes = shapes
            self.command_stack = command_stack

        def get_dialogs(self):
            self.dialogs["Circle"] = create_circle
            self.dialogs["Triangle"] = create_triangle
            self.dialogs["Rectangle"] = create_rectangle
            self.dialogs["Square"] = create_square
            self.dialogs["Translate"] = translate
            self.dialogs["Scale"] = scale
            self.dialogs["Clear"] = clear
            # TODO: Task 2 & 4: add the rectangle and scale dialogs to the dictionary of this factory 
            return self.dialogs 