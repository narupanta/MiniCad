from commands.command import Command

class CommandStack():
    def __init__(self) -> None:
        self.undoStack: list[Command] = []
        self.redoStack: list[Command] = []

    def execute(self, command: Command) -> None:
        # TODO: Task 5 - Implement the command stack
        command.execute()
        self.undoStack.append(command)
        # Clear redoStack whenever a new command is executed
        self.redoStack.clear()


    def undo(self) -> None:
        # TODO: Task 5 - Implement the command stack
        if self.undoStack:
            command = self.undoStack.pop()
            command.undo()
            self.redoStack.append(command)


    def redo(self) -> None:
        # TODO: Task 5 - Implement the command stack
        if self.redoStack:
            command = self.redoStack.pop()
            command.execute()
            self.undoStack.append(command)
