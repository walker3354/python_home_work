from PyQt6 import QtWidgets
from WorkWidgets.WidgetComponents import LabelComponent


class HomeWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout()
        title = LabelComponent(52, "Hello", "black", font="Gabriola")
        self.layout.setSpacing(0)
        self.layout.addWidget(title)
        self.setLayout(self.layout)

    def load(self):
        print("this is home widget")
