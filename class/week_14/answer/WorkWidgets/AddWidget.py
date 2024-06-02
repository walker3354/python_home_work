from PyQt6 import QtWidgets
from PyQt6.QtGui import QIntValidator
from WorkWidgets.Execute import Execute
from WorkWidgets.WidgetComponents import (
    ButtonComponent,
    LineEditComponent,
    LabelComponent,
    TextEditComponent,
)


# allocate size: 1200*800
class AddWidget(QtWidgets.QWidget):

    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket
        self.student_dict = {"name": "", "scores": {}}

        self.layout = QtWidgets.QGridLayout()
        self.message_board = TextEditComponent()

        self.name_label = LabelComponent(20, "Name", "white")
        self.subject_label = LabelComponent(20, "Subject", "white")
        self.score_label = LabelComponent(20, "Score", "white")
        self.blank_label = LabelComponent(20, "", "black")

        self.name_editor = LineEditComponent("student name")
        self.subject_editor = LineEditComponent("subject name")
        self.score_editor = LineEditComponent("subject score")

        self.query_button = ButtonComponent("Query")
        self.query_button.setFixedSize(180, 100)
        self.add_button = ButtonComponent("Add")
        self.add_button.setFixedSize(180, 100)
        self.send_button = ButtonComponent("Send")
        self.send_button.setFixedSize(180, 150)

        self.initial_components()
        self.setLayout(self.layout)

    def load(self):
        print("Add Function")

    def initial_components(self):
        for i in range(10):
            self.layout.setRowStretch(i, 1)
            self.layout.setColumnStretch(i, 1)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.layout.addWidget(self.blank_label, 0, 0, 10, 10)
        self.layout.addWidget(self.name_label, 1, 1, 2, 1)
        self.layout.addWidget(self.subject_label, 3, 1, 2, 1)
        self.layout.addWidget(self.score_label, 5, 1, 2, 1)

        self.layout.addWidget(self.name_editor, 1, 3, 2, 6)
        self.layout.addWidget(self.subject_editor, 3, 3, 2, 6)
        self.layout.addWidget(self.score_editor, 5, 3, 2, 6)

        self.layout.addWidget(self.query_button, 1, 8, 2, 2)
        self.layout.addWidget(self.add_button, 5, 8, 2, 2)
        self.layout.addWidget(self.send_button, 7, 8, 3, 3)

        self.layout.addWidget(self.message_board, 7, 1, 3, 6)

        self.score_editor.setMaxLength(3)
        self.score_editor.setValidator(QIntValidator(0, 100))

        self.query_button.clicked.connect(self.query)
        self.add_button.clicked.connect(self.add)
        self.send_button.clicked.connect(self.send)

    def query(self):
        message_pack = {"name": self.name_editor.text()}
        self.query_result = Execute("query", self.client_socket, message_pack)
        self.query_result.start()
        self.query_result.return_sig.connect(self.process_query)

    def process_query(self, result):
        name = self.name_editor.text()
        if result["status"] == "Fail":
            self.message_board.set_message(f"{name} not exsist")
        else:
            self.message_board.set_message(f"{name} exsist")

    def add(self):
        student_name = self.name_editor.text()
        subject = self.subject_editor.text()
        score = self.score_editor.text()
        self.student_dict["name"] = student_name
        self.student_dict["scores"].update({subject: score})
        self.message_board.set_message(
            f"Successful Add info: \nstudent name: {student_name} \nsubject: {subject}\tscore: {score}"
        )

    def send(self):
        self.send_result = Execute("add", self.client_socket, self.student_dict)
        self.send_result.start()
        self.send_result.return_sig.connect(self.process_send)

    def process_send(self, result):
        if result["status"] == "OK":
            self.message_board.set_message(f"Send {self.student_dict}")
        else:
            self.message_board.set_message(f"Add Fail")
        self.student_dict = {"name": "", "scores": {}}
