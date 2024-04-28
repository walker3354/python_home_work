from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import (
    LabelComponent,
    LineEditComponent,
    ButtonComponent,
)


class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("add_stu_widget")

        layout = QtWidgets.QGridLayout()

        header_label = LabelComponent(20, "Add Student")
        content_label = LabelComponent(16, "Name: ")
        self.editor_label = LineEditComponent("Name")
        self.editor_label.mousePressEvent = self.clear_editor_content
        button = ButtonComponent("Confirm")
        button.clicked.connect(self.confirm_action)

        layout.addWidget(header_label, 0, 0, 1, 1)
        layout.addWidget(content_label, 1, 0, 1, 1)
        layout.addWidget(self.editor_label, 1, 1, 1, 1)
        layout.addWidget(button, 2, 1, 2, 1)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 9)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 5)

        self.setLayout(layout)

    def clear_editor_content(self, event):
        self.editor_label.clear()

    def confirm_action(self):
        print(self.editor_label.text())
