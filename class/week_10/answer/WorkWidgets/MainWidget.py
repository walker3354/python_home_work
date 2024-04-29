from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.AddStuWidget import AddStuWidget
from WorkWidgets.WidgetComponents import LabelComponent


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("main_widget")

        self.layout = QtWidgets.QVBoxLayout()
        header_label = LabelComponent(24, "Student Management System")
        self.add_stu_widget = AddStuWidget()

        self.layout.addWidget(header_label, stretch=15)
        self.layout.addWidget(self.add_stu_widget, stretch=85)
        self.button_init()
        self.student_dict = {"name": "", "score": {}}
        self.setLayout(self.layout)

    def button_init(self):
        self.add_stu_widget.query_button.clicked.connect(self.query)
        self.add_stu_widget.add_button.clicked.connect(self.add)
        self.add_stu_widget.send_button.clicked.connect(self.send)

    def query(self):
        self.add_stu_widget.current_info.setText("SQL student no found")
        self.set_editor_useable(True)
        self.add_stu_widget.add_button.setEnabled(True)

    def add(self):
        student_name = self.add_stu_widget.name_editor_label.text()
        subject = self.add_stu_widget.subject_editor_label.text()
        score = self.add_stu_widget.score_editor_label.text()
        self.student_dict["name"] = student_name
        self.student_dict["score"].update({subject: score})
        self.add_stu_widget.current_info.setText(
            f"add name:{student_name} {subject} {score}"
        )
        self.set_editor_useable(False)
        self.add_stu_widget.add_button.setEnabled(False)
        self.add_stu_widget.send_button.setEnabled(True)

    def send(self):
        self.add_stu_widget.current_info.setText(f"The information {self.student_dict}")
        self.student_dict.clear()
        self.student_dict = {"name": "", "score": {}}
        self.add_stu_widget.send_button.setEnabled(False)

    def set_editor_useable(self, status):
        self.add_stu_widget.subject_editor_label.setEnabled(status)
        self.add_stu_widget.score_editor_label.setEnabled(status)
