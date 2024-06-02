from PyQt6 import QtWidgets
from WorkWidgets.Execute import Execute
from WorkWidgets.WidgetComponents import (
    LabelComponent,
    ButtonComponent,
    TextEditComponent,
    ComboBoxComponent,
    MessageBoxComponent,
)


# allocate size: 1200*800
class DeleteWidget(QtWidgets.QWidget):

    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket
        self.student_name_list = list()
        self.student_data = dict()
        self.student_name = ""
        self.layout = QtWidgets.QGridLayout()

        self.blank_label = LabelComponent(20, "", "black")
        self.student_name_label = LabelComponent(20, "Name", "white")
        self.delete_button = ButtonComponent("Delete")
        self.delete_combo_box = ComboBoxComponent()
        self.message_board = TextEditComponent("")

        self.initial_components()
        self.setLayout(self.layout)

    def load(self):
        self.fetch_all_student_name()
        print("Delete Function")

    def initial_components(self):
        for i in range(10):
            self.layout.setRowStretch(i, 1)
            self.layout.setColumnStretch(i, 1)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.layout.addWidget(self.blank_label, 0, 0, 10, 10)
        self.layout.addWidget(self.student_name_label, 1, 1, 1, 1)
        self.layout.addWidget(self.delete_combo_box, 1, 3, 1, 4)
        self.layout.addWidget(self.delete_button, 1, 8, 1, 1)
        self.layout.addWidget(self.message_board, 3, 1, 7, 9)

        self.delete_button.clicked.connect(self.confirm_delete_student)
        self.message_board.resize(960, 350)

    def fetch_all_student_name(self):
        self.send_result = Execute("show", self.client_socket, {})
        self.send_result.start()
        self.send_result.return_sig.connect(self.insert_all_student_name)

    def insert_all_student_name(self, respones_data):
        self.student_data = respones_data["parameters"]
        self.student_name_list = list(respones_data["parameters"].keys())
        self.delete_combo_box.addItems(self.student_name_list)
        print(self.student_name_list)

    def confirm_delete_student(self):
        confirm_result = MessageBoxComponent("Are you sure to delete this student?")
        if confirm_result.result == True:
            self.delete_student()

    def delete_student(self):
        self.student_name = self.delete_combo_box.currentText()
        self.send_result = Execute(
            "delete", self.client_socket, {"name": self.student_name}
        )
        self.send_result.start()
        self.send_result.return_sig.connect(self.set_textedit_contain)

    def set_textedit_contain(self, respones_data):
        self.message_board.clear()
        if respones_data["status"] == "OK":
            display_text = "Delete status: success\n"
            display_text += f"name : {self.student_name}\n"
            for subject, score in self.student_data[self.student_name][
                "scores"
            ].items():
                display_text += f"subject : {subject}\n score : {score}\n"
        self.message_board.set_message(display_text)
        self.delete_combo_box.clear()
        self.fetch_all_student_name()
