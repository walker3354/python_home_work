from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import pyqtSignal, Qt


class LabelComponent(QtWidgets.QLabel):
    def __init__(self, font_size, content, color="black", font="Arial"):
        super().__init__()
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if color == "black":
            self.setStyleSheet(f"background-color: white; color: black;")
        elif color == "white":
            self.setStyleSheet(f"background-color: black; color: white;")

        self.setFont(QtGui.QFont(font, pointSize=font_size, weight=500))
        self.setText(content)


class LineEditComponent(QtWidgets.QLineEdit):
    def __init__(self, default_content="", length=20, width=500, font_size=20):
        super().__init__()
        self.setMaxLength(length)
        self.setText(default_content)
        self.setMinimumHeight(100)
        self.setMaximumWidth(width)
        self.setFont(QtGui.QFont("Arial", font_size))
        self.setStyleSheet(
            """
            QLineEdit {
                background-color: white;
                color: black;
                border: 5px solid black;
                padding: 5px;
            }
        """
        )
        self.mousePressEvent = self.clear_editor_content

    def set_Enable(self, enable):
        if enable == False:
            self.setReadOnly(True)
            self.setStyleSheet(
                """
            QLineEdit {
                background-color: white;
                color: gray;
                border: 5px solid black;
                padding: 5px;
            }
        """
            )
        else:
            self.setReadOnly(False)
            self.setStyleSheet(
                """
            QLineEdit {
                background-color: white;
                color: black;
                border: 5px solid black;
                padding: 5px;
            }
        """
            )

    def clear_editor_content(self, event):
        self.clear()


class ButtonComponent(QtWidgets.QPushButton):
    def __init__(self, text, font_size=16, background_color="black"):
        super().__init__()
        self.setText(text)
        self.setFixedSize(200, 100)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFont(QtGui.QFont("Arial", font_size))
        self.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {background_color};
                color: white;
                border-radius: 15px;
            }}
            """
        )

    def set_Enable(self, enable):
        if enable == False:
            self.setEnabled(False)
            self.setStyleSheet(
                f"""
                QPushButton {{
                    background-color: gray;
                    color: white;
                    border-radius: 15px;
                }}
                """
            )
        else:
            self.setEnabled(True)
            self.setStyleSheet(
                f"""
                QPushButton {{
                    background-color: black;
                    color: white;
                    border-radius: 15px;
                }}
                """
            )


class TextEditComponent(QtWidgets.QTextEdit):
    def __init__(self, font="", font_size=20, width=750, height=160):
        super().__init__()
        self.setText(f"{font}")
        self.setFixedSize(width, height)
        self.setFont(QtGui.QFont(font, font_size))
        self.setReadOnly(True)
        self.setStyleSheet(
            """
            QLineEdit {
                background-color: gary;
                color: black;
                border: 5px solid black;
                padding: 5px;
            }
        """
        )

    def set_message(self, message):
        self.setText(f"system message:\n{message}")
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def resize(self, width, height):
        self.setFixedSize(width, height)
        self.update()


class ComboBoxComponent(QtWidgets.QComboBox):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(
            """
            QComboBox {
                background-color: white;
                color: black;
                border: 5px solid black;
                padding: 5px;
            }
        """
        )
        self.setFixedSize(500, 100)
        self.setFont(QtGui.QFont("Arial", 20))

    def set_Enable(self, enable):
        if enable == False:
            self.setEnabled(False)
            self.setStyleSheet(
                """
                QComboBox {
                    background-color: gray;
                    color: white;
                    border: 5px solid black;
                    padding: 5px;
                }
            """
            )
        else:
            self.setEnabled(True)
            self.setStyleSheet(
                """
                QComboBox {
                    background-color: white;
                    color: black;
                    border: 5px solid black;
                    padding: 5px;
                }
            """
            )


class MessageBoxComponent(QtWidgets.QMessageBox):
    def __init__(self, message):
        super().__init__()
        self.setText(message)
        self.result = False
        result = QtWidgets.QMessageBox.question(
            self,
            "Question",
            message,
            QtWidgets.QMessageBox.StandardButton.Yes
            | QtWidgets.QMessageBox.StandardButton.No,
        )
        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            self.result = True
        else:
            self.result = False
