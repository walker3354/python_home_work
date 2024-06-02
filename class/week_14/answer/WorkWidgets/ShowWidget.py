from PyQt6 import QtWidgets
from WorkWidgets.Execute import Execute
from WorkWidgets.WidgetComponents import LabelComponent, TextEditComponent


# allocate size: 1200*800
class ShowWidget(QtWidgets.QWidget):

    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket
        self.layout = QtWidgets.QGridLayout()

        self.blank_label = LabelComponent(20, "", "black")
        self.message_board = TextEditComponent("")

        self.initial_components()
        self.setLayout(self.layout)

    def load(self):
        self.fetch_all_student_data()
        print("Show Function")

    def initial_components(self):
        for i in range(10):
            self.layout.setRowStretch(i, 1)
            self.layout.setColumnStretch(i, 1)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.layout.addWidget(self.blank_label, 0, 0, 10, 10)
        self.layout.addWidget(self.message_board, 1, 1, 9, 8)

        self.message_board.resize(810, 500)

    def fetch_all_student_data(self):
        self.send_result = Execute("show", self.client_socket, {})
        self.send_result.start()
        self.send_result.return_sig.connect(self.set_textedit_contain)

    def set_textedit_contain(self, respones_data):
        self.message_board.clear()
        student_dict = respones_data["parameters"]
        display_text = "\n==== student list ====\n"
        for index_1, value_1 in student_dict.items():
            display_text += f"Name:{index_1}\n"
            for index_2, value_2 in value_1["scores"].items():
                display_text += f"   subject: {index_2},score:{value_2}\n"
            display_text += "\n"
        display_text += "======================"
        self.message_board.set_message(display_text)
