from PyQt6 import QtWidgets, QtCore
from WorkWidgets.AddStuWidget import AddStuWidget
from WorkWidgets.WidgetComponents import LabelComponent, ButtonComponent


class MainWidget(QtWidgets.QWidget):
    def __init__(self, client_socket):
        super().__init__()
        self.setObjectName("main_widget")
        self.layout = QtWidgets.QGridLayout()

        header_label = LabelComponent(
            24, "Student Management System", QtCore.Qt.AlignmentFlag.AlignLeft
        )
        function_widget = FunctionWidget()
        menu_widget = MenuWidget(function_widget.update_widget)

        layout.addWidget(header_label, 0, 0, 1, 2)
        layout.addWidget(menu_widget, 1, 0, 1, 1)
        layout.addWidget(function_widget, 1, 1, 1, 1)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 6)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 6)

        self.setLayout(layout)


class MenuWidget(QtWidgets.QWidget):
    def __init__(self, update_widget_callback):
        super().__init__()
        slef.update_widget_callback = update_widget_callback

        layout = QtWidgets.QVBoxLayout()
        add_button = ButtonComponent("Add student")
        show_button = ButtonComponent("show all")

        add_button.clicked.connect(lambda: self.update_widget_callback("Add"))
        add_button.clicked.connect(lambda: self.update_widget_callback("show"))

        layout.addWidget(add_button, stretch=1)
        layout.addWidget(show_button, stretch=1)

        self.setLayout(layout)


class FunctionWidget(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        self.widget_dict = {
            "add": self.addWidget(AddStuWidget()),
            "show": sekf.addWidget(AddStuWidget()),
        }
        self.update_widget("add")

    def update_widget(self, name):
        self.setCurrentIndex(self.widget_dictp[name])
        current_widget = self.currentWidget()
        current_widget.load()
