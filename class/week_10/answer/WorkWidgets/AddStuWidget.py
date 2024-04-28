from PyQt6 import QtWidgets, QtCore
from WorkWidgets.WidgetComponents import (
    LabelComponent,
    LineEditComponent,
    ButtonComponent,
)


class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QGridLayout()
        self.header_label = LabelComponent(20, "Add Student")
        self.name_label = LabelComponent(
            18, "Name: ", QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.subject_label = LabelComponent(
            16, "Subject: ", QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.score_label = LabelComponent(
            18, "Score: ", QtCore.Qt.AlignmentFlag.AlignRight
        )

        self.name_editor_label = LineEditComponent("Name")
        self.subject_editor_label = LineEditComponent("Subject")
        self.score_editor_label = LineEditComponent("")

        self.query_button = ButtonComponent("Query")
        self.add_button = ButtonComponent("Add")
        self.send_button = ButtonComponent("Send")

        self.query_button.clicked.connect(self.confirm_action)
        self.set_components_pos()
        self.set_layout_grid()
        self.setLayout(self.layout)

    def set_components_pos(self):
        # (component,pos_row,pos_column,take_row,take_column)
        self.layout.addWidget(self.header_label, 0, 0, 1, 2)
        self.layout.addWidget(self.name_label, 1, 0, 1, 1)
        self.layout.addWidget(self.subject_label, 2, 0, 1, 1)
        self.layout.addWidget(self.score_label, 3, 0, 1, 1)

        self.layout.addWidget(self.name_editor_label, 1, 1, 1, 1)
        self.layout.addWidget(self.subject_editor_label, 2, 1, 1, 1)
        self.layout.addWidget(self.score_editor_label, 3, 1, 1, 1)

        self.layout.addWidget(self.query_button, 1, 2, 1, 1)
        self.layout.addWidget(self.add_button, 3, 2, 1, 1)
        self.layout.addWidget(self.send_button, 5, 3, 1, 1)

    def set_layout_grid(self):
        self.layout.setColumnStretch(0, 2)
        self.layout.setColumnStretch(1, 10)
        self.layout.setColumnStretch(2, 2)
        self.layout.setColumnStretch(3, 3)

        self.layout.setRowStretch(0, 3)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 1)
        self.layout.setRowStretch(3, 1)
        self.layout.setRowStretch(4, 4)
        self.layout.setRowStretch(5, 1)

    def confirm_action(self):
        print(self.name_editor_label.text())
