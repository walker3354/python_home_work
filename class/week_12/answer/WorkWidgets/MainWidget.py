from PyQt6 import QtWidgets, QtCore
from WorkWidgets.AddStuWidget import AddStuWidget
from WorkWidgets.WidgetComponents import LabelComponent


class MainWidget(QtWidgets.QWidget):
    def __init__(self, client_socket):
        super().__init__()
        self.setObjectName("main_widget")
        self.layout = QtWidgets.QVBoxLayout()
        header_label = LabelComponent(
            24, "Student Management System", QtCore.Qt.AlignmentFlag.AlignLeft
        )
        self.add_stu_widget = AddStuWidget(client_socket)

        self.layout.addWidget(header_label, stretch=15)
        self.layout.addWidget(self.add_stu_widget, stretch=85)

        self.setLayout(self.layout)
