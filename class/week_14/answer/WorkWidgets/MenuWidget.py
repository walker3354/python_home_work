from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import pyqtSignal
from WorkWidgets.WidgetComponents import ButtonComponent
from WorkWidgets.HomeWidget import HomeWidget


# allocate size: 150*800
class MenuWidget(QtWidgets.QWidget):

    addClicked = QtCore.pyqtSignal()
    showClicked = QtCore.pyqtSignal()
    modifyClicked = QtCore.pyqtSignal()
    deleteClicked = QtCore.pyqtSignal()

    def __init__(self, update_widget_callback):
        super().__init__()
        self.layout = QtWidgets.QHBoxLayout()
        self.update_widget = update_widget_callback

        self.empty_button1 = ButtonComponent("")
        self.empty_button2 = ButtonComponent("")
        self.add_button = ButtonComponent("Add")
        self.show_button = ButtonComponent("Show")
        self.modify_button = ButtonComponent("Modify")
        self.del_button = ButtonComponent("Delete")

        self.initial_components()
        self.setLayout(self.layout)

    def initial_components(self):
        self.layout.addWidget(self.empty_button1, stretch=1)
        self.layout.addWidget(self.add_button, stretch=1)
        self.layout.addWidget(self.show_button, stretch=1)
        self.layout.addWidget(self.modify_button, stretch=1)
        self.layout.addWidget(self.del_button, stretch=1)
        self.layout.addWidget(self.empty_button2, stretch=1)

        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.buttons_clicked_connect()

    def buttons_clicked_connect(self):
        self.add_button.clicked.connect(self.add_label_clicked)
        self.show_button.clicked.connect(self.show_label_clicked)
        self.modify_button.clicked.connect(self.modify_label_clicked)
        self.del_button.clicked.connect(self.del_label_clicked)

    def refresh_color(self):
        self.add_button.setStyleSheet("background-color: black; color: white;")
        self.show_button.setStyleSheet("background-color: black; color: white;")
        self.modify_button.setStyleSheet("background-color: black; color: white;")
        self.del_button.setStyleSheet("background-color: black; color: white;")

    def add_label_clicked(self):
        self.refresh_color()
        self.add_button.setStyleSheet("background-color: gray; color: white;")
        self.addClicked.emit()
        self.update_widget("add")

    def show_label_clicked(self):
        self.refresh_color()
        self.show_button.setStyleSheet("background-color: gray; color: white;")
        self.showClicked.emit()
        self.update_widget("show")

    def modify_label_clicked(self):
        self.refresh_color()
        self.modify_button.setStyleSheet("background-color: gray; color: white;")
        self.modifyClicked.emit()
        self.update_widget("modify")

    def del_label_clicked(self):
        self.refresh_color()
        self.del_button.setStyleSheet("background-color: gray; color: white;")
        self.deleteClicked.emit()
        self.update_widget("delete")
