from PyQt6 import QtWidgets, QtCore
from WorkWidgets.MenuWidget import MenuWidget
from WorkWidgets.HomeWidget import HomeWidget
from WorkWidgets.WidgetComponents import LabelComponent, ButtonComponent


class MainWidget(QtWidgets.QWidget):
    def __init__(self, client_socket):
        super().__init__()
        self.layout = QtWidgets.QGridLayout()

        self.header_label = LabelComponent(24, "Student Management System", "black")
        self.function_widget = FunctionWidget(client_socket)
        self.menu_layer = MenuWidget(self.function_widget.update_widget)
        self.menu_layer_connect()

        self.layout.addWidget(self.header_label, 0, 0)
        self.layout.addWidget(self.menu_layer, 1, 0)
        self.layout.addWidget(self.function_widget, 2, 0)

        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 6)

        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

    def menu_layer_connect(self):
        self.menu_layer.addClicked.connect(
            lambda: self.header_label.setText("Add Student")
        )
        self.menu_layer.showClicked.connect(
            lambda: self.header_label.setText("Show Student")
        )
        self.menu_layer.modify_button.clicked.connect(
            lambda: self.header_label.setText("Modify Student")
        )
        self.menu_layer.deleteClicked.connect(
            lambda: self.header_label.setText("Delete Student")
        )


class FunctionWidget(QtWidgets.QStackedWidget):

    def __init__(self, client_socket):
        super().__init__()
        self.Widget_dict = {
            "home": self.addWidget(HomeWidget()),
        }
        self.update_widget("home")

    def update_widget(self, widget_name):
        self.setCurrentIndex(self.Widget_dict[widget_name])
        current_widget = self.currentWidget()
        current_widget.load()
