from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import pyqtSignal, Qt


class LabelComponent(QtWidgets.QLabel):
    def __init__(self, font_size, content, color="black"):
        super().__init__()
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if color == "black":
            self.setStyleSheet(f"background-color: white; color: black;")
        elif color == "white":
            self.setStyleSheet(f"background-color: black; color: white;")

        self.setFont(QtGui.QFont("Arial", pointSize=font_size, weight=500))
        self.setText(content)


class LineEditComponent(QtWidgets.QLineEdit):
    def __init__(self, default_content="", length=10, width=250, font_size=16):
        super().__init__()
        self.setMaxLength(length)
        self.setText(default_content)
        self.setMinimumHeight(30)
        self.setMaximumWidth(width)
        self.setFont(QtGui.QFont("Arial", font_size))
        self.mousePressEvent = self.clear_editor_content

    def clear_editor_content(self, event):
        self.clear()


class ButtonComponent(QtWidgets.QPushButton):
    def __init__(self, text, font_size=16, background_color="black"):
        super().__init__()
        self.setText(text)
        self.setFont(QtGui.QFont("Arial", font_size))
        self.setStyleSheet(f"background-color: {background_color}; color: white;")
