from PyQt6 import QtWidgets, QtCore, QtGui


class LabelComponent(QtWidgets.QLabel):
    def __init__(
        self, font_size, content, align=QtCore.Qt.AlignmentFlag.AlignRight, color=""
    ):
        super().__init__()
        self.setWordWrap(True)
        self.setAlignment(align)
        if color != "":
            self.setStyleSheet(f"color: {color};")
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
    def __init__(self, text, font_size=16):
        super().__init__()
        self.setText(text)
        self.setFont(QtGui.QFont("Arial", font_size))
