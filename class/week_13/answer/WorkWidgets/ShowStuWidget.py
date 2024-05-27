from PyQt6 import QtWidgets, QtCore
from WorkWidgets.Execute import Execute
from WorkWidgets.WidgetComponents import (
    LabelComponent,
    LineEditComponent,
    ButtonComponent,
)


class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket
        self.setObjectName("show_stu_widget")
        self.layout = QtWidgets.QVBoxLayout()

        self.textedit = QtWidgets.QTextEdit()
        self.header_label = LabelComponent(
            20, "Show Student", align=QtCore.Qt.AlignmentFlag.AlignLeft
        )

        self.layout.addWidget(self.header_label, stretch=1)
        self.layout.addWidget(self.textedit, stretch=4)

        self.setLayout(self.layout)

    def selected(self):
        self.fetch_all_student_data()
        print("now using Show widget")

    def fetch_all_student_data(self):
        self.send_result = Execute("show", self.client_socket, {})
        self.send_result.start()
        self.send_result.return_sig.connect(self.set_textedit_contain)
        """
        self.client_socket.send_command("show", {})
        self.student_dict = self.client_socket.wait_response()["parameters"]
        """

    def set_textedit_contain(self, respones_data):
        self.textedit.clear()
        student_dict = respones_data["parameters"]
        display_text = "\n==== student list ====\n"
        for index_1, value_1 in student_dict.items():
            display_text += f"Name:{index_1}\n"
            for index_2, value_2 in value_1["scores"].items():
                display_text += f"   subject: {index_2},score:{value_2}\n"
            display_text += "\n"
        display_text += "======================"
        self.textedit.setText(display_text)
        self.textedit.setReadOnly(True)
