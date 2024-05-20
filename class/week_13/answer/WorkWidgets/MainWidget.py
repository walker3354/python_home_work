from PyQt6 import QtWidgets, QtCore
from WorkWidgets.AddStuWidget import AddStuWidget
from WorkWidgets.ShowStuWidget import ShowStuWidget
from WorkWidgets.WidgetComponents import LabelComponent, ButtonComponent


class MainWidget(QtWidgets.QWidget):
    def __init__(self, client_socket):
        super().__init__()
        self.setObjectName("main_widget")
        self.layout = QtWidgets.QGridLayout()

        header_label = LabelComponent(
            24, "Student Management System", QtCore.Qt.AlignmentFlag.AlignLeft
        )
        function_widget = FunctionWidget(client_socket)
        menu_widget = MenuWidget(function_widget.update_widget)

        self.layout.addWidget(header_label, 0, 0, 1, 2)
        self.layout.addWidget(menu_widget, 1, 0, 1, 1)
        self.layout.addWidget(function_widget, 1, 1, 1, 1)

        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 6)
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 6)

        self.setLayout(self.layout)


class MenuWidget(QtWidgets.QWidget):
    def __init__(self, update_widget_callback):
        super().__init__()
        self.update_widget_callback = update_widget_callback

        layout = QtWidgets.QVBoxLayout()
        add_button = ButtonComponent("Add student")
        show_button = ButtonComponent("show all")

        add_button.clicked.connect(lambda: self.update_widget_callback("add"))
        show_button.clicked.connect(lambda: self.update_widget_callback("show"))

        layout.addWidget(add_button, stretch=1)
        layout.addWidget(show_button, stretch=1)

        self.setLayout(layout)


class FunctionWidget(QtWidgets.QStackedWidget):
    def __init__(self, client_socket):
        super().__init__()
        self.widget_dict = {
            "add": self.addWidget(AddStuWidget(client_socket)),
            "show": self.addWidget(ShowStuWidget(client_socket)),
        }
        self.update_widget("add")

    def update_widget(self, name):
        self.setCurrentIndex(self.widget_dict[name])
        current_widget = self.currentWidget()
        current_widget.show_current_widget()
