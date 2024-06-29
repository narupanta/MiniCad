# Scientific Software Engineering Homework SS2023

## Prerequisites
You can download the starting point for the application from StudIP.

## Exercise 1
To make yourself familiar with the current state of the application, create a UML class diagram of the important classes to reflect the general application design. The diagram should identify the volatile and stable parts (core) of the application. To create UML diagrams you can use online services like draw.io or techdebate.io.

## Exercise 2
Your objective is to develop a new dialog feature that enables users to generate rectangles. To achieve this, you must design a new dialog class and a standalone function that creates both the dialog and the actual rectangle. Additionally, you should ensure that this function is registered within the ActionFactory. All changes need be done in ui/dialogs.py.

## Exercise 3
Implement the drawing mechanism of the class Triangle. The drawing method of the already existing shapes will give you a good orientation for the implementation of the drawing method for the new shape type.

## Exercise 4
Currently a user can translate any shape. In addition, the user should also be able to scale any shape. Implement the scaling behavior for all available shape types and the corresponding scaling dialog.

## Exercise 5
The command pattern is a proven way to implement an undo/redo mechanism. Extend the already existing CommandStack class (the invoker) to support the undo/redo mechanism accordingly.


## Final Result
A user of the mini-cad app should be able to create circles, squares, rectangles and triangles. He or she can translate and scale shapes. Additionally, the user should be able to undo and redo all of the changes.


# Run the Code
## Setup
In order to run the code using the graphical user interface, you will need to install the following packages:
- PyQSide6
- mypy


It's recommended to use a virtual environment before installing the packages.
```
python -m venv venv
source venv/bin/activate
```

Afterwards you can install the packages using the following command:
```
pip install -r requirements.txt
```
