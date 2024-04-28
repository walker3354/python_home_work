from WorkWidgets.MainWidget import MainWidget
from PyQt6.QtWidgets import QApplication
import sys


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWidget()
    main_window.setFixedSize(750, 450)
    main_window.show()
    sys.exit(app.exec())
