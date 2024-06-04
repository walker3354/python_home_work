from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QIntValidator
from WorkWidgets.Execute import Execute
from WorkWidgets.WidgetComponents import (
    ButtonComponent,
    LineEditComponent,
    LabelComponent,
    ComboBoxComponent,
)


# allocate size: 1200*800
class ModifyWidget(QtWidgets.QWidget):

    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket
        self.student_data = dict()
        self.student_name_list = list()

        self.layout = QtWidgets.QGridLayout()

        self.name_label = LabelComponent(20, "Name", "white")
        self.subject_label = LabelComponent(20, "Subject", "white")
        self.score_label = LabelComponent(20, "Score", "white")
        self.blank_label = LabelComponent(20, "", "black")

        self.name_combo_box = ComboBoxComponent()
        self.subject_combo_box = ComboBoxComponent()
        self.score_editor = LineEditComponent()

        self.modify_button = ButtonComponent("Modify")
        self.modify_button.setFixedSize(180, 100)
        self.send_button = ButtonComponent("Send")
        self.send_button.setFixedSize(180, 150)

        self.initial_components()
        self.setLayout(self.layout)

    def load(self):
        print("Modify Function")
        self.fetch_all_student_name()

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

        self.layout.addWidget(self.name_combo_box, 1, 3, 2, 6)
        self.layout.addWidget(self.subject_combo_box, 3, 3, 2, 6)
        self.layout.addWidget(self.score_editor, 5, 3, 2, 6)

        self.layout.addWidget(self.modify_button, 5, 8, 2, 2)
        self.layout.addWidget(self.send_button, 7, 8, 3, 3)

        self.score_editor.setMaxLength(3)
        self.score_editor.setValidator(QIntValidator(0, 100))

        self.name_combo_box.currentIndexChanged.connect(self.change_student)
        self.modify_button.clicked.connect(self.modify_student_score)
        self.send_button.clicked.connect(self.send)

    def fetch_all_student_name(self):
        self.send_result = Execute("show", self.client_socket, {})
        self.send_result.start()
        self.send_result.return_sig.connect(self.insert_all_student_name)

    def insert_all_student_name(self, respones_data):
        self.student_data = respones_data["parameters"]
        self.student_name_list = list(respones_data["parameters"].keys())
        self.name_combo_box.clear()
        self.name_combo_box.addItems(self.student_name_list)

    @pyqtSlot()
    def change_student(self):
        self.subject_combo_box.addItems(
            list(self.student_data[self.student_name_list[0]]["scores"].keys())
        )
        current_name = self.name_combo_box.currentText()
        if current_name == "":
            return
        self.subject_combo_box.clear()
        self.subject_combo_box.addItems(
            list(self.student_data[current_name]["scores"].keys())
        )

    def modify_student_score(self):
        if self.score_editor.text() == "":
            return
        self.name_combo_box.set_Enable(False)
        name = self.name_combo_box.currentText()
        subject = self.subject_combo_box.currentText()
        self.student_data[name]["scores"][subject] = self.score_editor.text()

    def send(self):
        print("send")
        name = self.name_combo_box.currentText()
        scores = self.student_data[name]["scores"]
        self.send_result = Execute(
            "modify",
            self.client_socket,
            {
                "name": name,
                "scores_dict": scores,
            },
        )
        self.send_result.start()
        self.send_result.return_sig.connect(self.process_send)
        self.name_combo_box.set_Enable(True)

    def process_send(self, result):
        if result["status"] == "OK":
            print("OK")
        else:
            print("error")
        self.score_editor.clear()
