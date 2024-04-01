class AddStu:
    def __init__(self):
        # if you don't use this format the sever will fuxk up
        self.parameters = {'name': "", 'score': {}}

    def execute(self):
        self.input_student_name()
        return self.parameters

    def input_student_name(self):
        while True:
            student_name = input("Please input a student's name or exit: ")
            if student_name == 'exit':
                return
            break
        self.parameters['name'] = student_name
        self.input_subject(student_name)

    def input_subject(self, student_name):
        while True:
            subject_name = input(
                "Please input a subject name or exit for ending: ")
            if subject_name == 'exit':
                break
            self.input_subject_score(subject_name, student_name)

    def input_subject_score(self, subject_name, student_name):
        while True:
            try:
                subject_score = int(
                    input(
                        "Please input {}'s {} score or < 0 for discarding the subject: ".format(student_name, subject_name)))
                if subject_score < 0:
                    break
                self.parameters['score'][subject_name] = subject_score
                break
            except Exception as e:
                print(e)
