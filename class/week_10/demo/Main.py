from WorkWidgets.MainWidget import MainWidget
from PyQt6.QtWidgets import QApplication
import sys

app = QApplication([])
main_window = MainWidget()

main_window.setFixedSize(500, 300)
main_window.show()


sys.exit(app.exec())
