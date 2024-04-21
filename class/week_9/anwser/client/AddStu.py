from Socket_client import Socket_client


class AddStu:
    def __init__(self):
        self.parameters = {"name": "", "scores": {}}
        self.socket = Socket_client()

    def execute(self):
        self.input_student_name()
        return self.parameters

    def input_student_name(self):
        student_name = input("Please input a student's name or exit: ")
        if student_name == "exit":
            return
        if self.check_student_name():
            self.parameters["name"] = student_name
            self.input_subject()

    def check_student_name(self, name):
        self.socket.send_command("query", {"name": name})
        if self.socket.wait_response()["status"] == "Fail":
            return True
        return False

    def input_subject(self):
        while True:
            subject_name = input("Please input a subject name or exit for ending: ")
            if subject_name == "exit":
                break
            self.input_subject_score(subject_name)
        self.send_message_to_socket()

    def input_subject_score(self, subject_name):
        while True:
            try:
                subject_score = int(input(f"Please input {self.parameters["name"]}'s {subject_name} score or < 0 for discarding the subject: "))
                if subject_score < 0:
                    break
                self.parameters["scores"][subject_name] = subject_score
                break
            except Exception as e:
                print(e)

    def send_message_to_socket(self):
        self.socket.send_command("add", self.parameters)
        if self.socket.wait_response()["status"] == "OK":
            print(f"Add {self.parameters} success")
        else:
            print(f"Add {self.parameters} fail")
