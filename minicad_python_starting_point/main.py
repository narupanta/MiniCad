import sys
from PySide6.QtWidgets import QMainWindow, QApplication

from ui.main_window import MainWindow


if __name__ == '__main__':
     app = QApplication(sys.argv)
     ex = MainWindow()
     sys.exit(app.exec())