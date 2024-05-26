from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import pyqtSignal
from WorkWidgets.WidgetComponents import ButtonComponent


class MenuWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QHBoxLayout()

        self.add_button = ButtonComponent("Add")
        self.show_button = ButtonComponent("Show")
        self.modify_button = ButtonComponent("Modify")
        self.del_button = ButtonComponent("Delete")

        self.layout.addWidget(self.add_button, stretch=1)
        self.layout.addWidget(self.show_button, stretch=1)
        self.layout.addWidget(self.modify_button, stretch=1)
        self.layout.addWidget(self.del_button, stretch=1)

        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.button_init()
        self.setStyleSheet("QWidget { background-color: white; }")
        self.setLayout(self.layout)
        print("menu widget init")

    def button_init(self):
        self.add_button.clicked.connect(self.add_label_clicked)
        self.show_button.clicked.connect(self.show_label_clicked)
        self.modify_button.clicked.connect(self.modify_label_clicked)
        self.del_button.clicked.connect(self.del_label_clicked)

    def add_label_clicked(self):
        print("add")

    def show_label_clicked(self):
        print("show")

    def modify_label_clicked(self):
        print("modify")

    def del_label_clicked(self):
        print("del")
