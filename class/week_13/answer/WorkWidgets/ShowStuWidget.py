from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import (
    LabelComponent,
    LineEditComponent,
    ButtonComponent,
)


class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self, client_socket):
        super().__init__()
        self.setObjectName("show_stu_widget")

        self.layout = QtWidgets.QVBoxLayout()
        self.textedit = QtWidgets.QTextEdit()
        self.header_label = LabelComponent(
            20, "Show Student", align=QtCore.Qt.AlignmentFlag.AlignLeft
        )

        self.layout.addWidget(self.header_label, stretch=1)
        self.layout.addWidget(self.textedit, stretch=3)
        self.setLayout(self.layout)

    def show_current_widget(self):
        print("now using Show widget")
