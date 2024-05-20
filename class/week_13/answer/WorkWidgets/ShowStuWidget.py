from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import (
    LabelComponent,
    LineEditComponent,
    ButtonComponent,
)


class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket
        self.student_dict = dict()
        self.setObjectName("show_stu_widget")
        self.layout = QtWidgets.QVBoxLayout()

        self.textedit = QtWidgets.QTextEdit()
        self.header_label = LabelComponent(
            20, "Show Student", align=QtCore.Qt.AlignmentFlag.AlignLeft
        )

        self.fetch_all_student_data()
        self.set_textedit_contain()

        self.layout.addWidget(self.header_label, stretch=1)
        self.layout.addWidget(self.textedit, stretch=4)
        self.setLayout(self.layout)

    def show_current_widget(self):
        print("now using Show widget")

    def fetch_all_student_data(self):
        self.client_socket.send_command("show", {})
        self.student_dict = self.client_socket.wait_response()["parameters"]

    def set_textedit_contain(self):
        self.textedit.clear()
        display_text = "\n==== student list ====\n"
        for index_1, value_1 in self.student_dict.items():
            display_text += "Name:{}\n".format(index_1)
            for index_2, value_2 in value_1["scores"].items():
                display_text += "   subject: {},score:{}\n".format(index_2, value_2)
            display_text += "\n"
        display_text += "======================"
        self.textedit.setText(display_text)
        self.textedit.setReadOnly(True)
