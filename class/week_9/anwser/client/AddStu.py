from Socket_client import Socket_client


class AddStu:
    def __init__(self):
        self.parameters = {'name': "", 'score': {}}
        self.socket = Socket_client()

    def execute(self):
        self.input_student_name()
        return self.parameters

    def input_student_name(self):
        student_name = input("Please input a student's name or exit: ")
        if student_name == 'exit':
            return
        self.parameters['name'] = student_name
        self.input_subject()

    def input_subject(self):
        while True:
            subject_name = input(
                "Please input a subject name or exit for ending: ")
            if subject_name == 'exit':
                break
            self.input_subject_score(subject_name)
        self.send_message_to_socket()

    def input_subject_score(self, subject_name):
        while True:
            try:
                subject_score = int(
                    input("Please input {}'s {} score or < 0 for discarding the subject: ".format(self.parameters['name'], subject_name)))
                if subject_score < 0:
                    break
                self.parameters['score'][subject_name] = subject_score
                break
            except Exception as e:
                print(e)

    def send_message_to_socket(self):
        self.socket.send_command('add', self.parameters)
        if self.socket.wait_response()['status'] == 'OK':
            print(f"Add {self.parameters} success")
        else:
            print(f"Add {self.parameters} fail")
