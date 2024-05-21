from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIntValidator
from WorkWidgets.Execute import Execute
from WorkWidgets.WidgetComponents import (
    LabelComponent,
    LineEditComponent,
    ButtonComponent,
)


class AddStuWidget(QtWidgets.QWidget):
    def __init__(self, client_scoket):
        super().__init__()
        self.client_socket = client_scoket
        self.student_dict = {"name": "", "scores": {}}

        self.layout = QtWidgets.QGridLayout()
        self.current_info = LabelComponent(16, "", color="red")
        self.header_label = LabelComponent(
            20, "Add Student", QtCore.Qt.AlignmentFlag.AlignLeft
        )
        self.name_label = LabelComponent(18, "Name: ")
        self.subject_label = LabelComponent(16, "Subject: ")
        self.score_label = LabelComponent(18, "Score: ")

        self.name_editor_label = LineEditComponent("Name")
        self.subject_editor_label = LineEditComponent("Subject")
        self.score_editor_label = LineEditComponent("")

        self.query_button = ButtonComponent("Query")
        self.add_button = ButtonComponent("Add")
        self.send_button = ButtonComponent("Send")

        self.set_components_pos()
        self.set_layout_grid()
        self.set_buttons_init_status()
        self.set_lineEdits_init_status()
        self.setLayout(self.layout)

    def set_components_pos(self):
        self.layout.addWidget(self.current_info, 0, 3, 1, 2)
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

    def set_buttons_init_status(self):
        self.add_button.setEnabled(False)
        self.send_button.setEnabled(False)
        self.query_button.clicked.connect(self.query)
        self.add_button.clicked.connect(self.add)
        self.send_button.clicked.connect(self.send)

    def set_lineEdits_init_status(self):
        self.subject_editor_label.setEnabled(False)
        self.score_editor_label.setEnabled(False)
        self.score_editor_label.setMaxLength(3)
        self.score_editor_label.setValidator(QIntValidator())

    def set_editor_useable(self, status):
        self.subject_editor_label.setEnabled(status)
        self.score_editor_label.setEnabled(status)

    def query(self):
        self.query_result = Execute(
            "query", self.client_socket, {"name": self.name_editor_label.text()}
        )
        self.query_result.start()
        self.query_result.return_sig.connect(self.process_query)

    def process_query(self, result):
        if result["status"] == "Fail":
            self.current_info.setText("SQL student no found")
            self.set_editor_useable(True)
            self.add_button.setEnabled(True)
        else:
            self.set_editor_useable(False)
            self.add_button.setEnabled(False)
            self.current_info.setText("student already exsist")

    def add(self):
        student_name = self.name_editor_label.text()
        subject = self.subject_editor_label.text()
        score = self.score_editor_label.text()
        self.student_dict["name"] = student_name
        self.student_dict["scores"].update({subject: score})
        self.current_info.setText(f"add name:{student_name} {subject} {score}")
        self.add_button.setEnabled(True)
        self.send_button.setEnabled(True)

    def send(self):
        self.send_result = Execute("add", self.client_socket, self.student_dict)
        self.send_result.start()
        self.send_result.return_sig.connect(self.process_send)

    def process_send(self, result):
        if result["status"] == "OK":
            self.current_info.setText(f"The information {self.student_dict}")
        else:
            self.current_info.setText(f"Add Fail")
        self.student_dict = {"name": "", "scores": {}}
        self.set_editor_useable(False)
        self.add_button.setEnabled(False)
        self.send_button.setEnabled(False)

    def show_current_widget(self):
        print("now using Add widget")
