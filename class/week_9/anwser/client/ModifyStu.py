class ModifyStu:
    def __init__(self, socket):
        self.student_name = ""
        self.socket = socket
        self.socket_receive_data = False

    def execute(self):
        self.input_student_name()

    def check_student_name(self):
        self.socket.send_command("query", {"name": self.student_name})
        return_data = self.socket.wait_response()
        if return_data["status"] == "OK":
            return return_data
        return False

    def input_student_name(self):
        self.student_name = input("Please input a student's name or exit: ")
        self.socket_receive_data = self.check_student_name()
        if self.socket_receive_data != False:
            self.input_subject_name()

    def show_student_subject(self):
        print("current subjects are ", end="")
        for subject in self.socket_receive_data["scores"].keys():
            print(f"{subject} ", end="")

    def input_subject_name(self):
        self.show_student_subject()
        while True:
            changed_subject = input("\nPlease input a subject you want to change: ")
            if changed_subject in self.socket_receive_data["scores"]:
                break
            print("input subject error please try again")
        self.input_subject_score(changed_subject)

    def input_subject_score(self, subject_name):
        while True:
            try:
                subject_score = int(
                    input(
                        f"Add a new subject for {subject_name} please input {subject_name} score or < 0 for discarding the subject: "
                    )
                )
                break
            except Exception as e:
                print(e)
        self.send_modify_data(subject_name, subject_score)

    def send_modify_data(self, subject_name, subject_score):
        self.socket_receive_data["scores"][subject_name] = subject_score
        self.socket.send_command(
            "modify",
            {
                "name": self.student_name,
                "scores_dict": self.socket_receive_data["scores"],
            },
        )
        if self.socket.wait_response()["status"] == "OK":
            print(
                f"Add [{self.student_name} , {subject_name} , {subject_score}] success"
            )
        else:
            print(f"Add [{self.student_name} , {subject_name} , {subject_score}] fail")
