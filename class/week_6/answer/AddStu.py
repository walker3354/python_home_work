class AddStu:
    def __init__(self, student_dict):
        self.student_dict = student_dict
        self.parameters = dict()

    def execute(self):
        self.input_student_name()
        return self.student_dict, self.parameters

    def input_student_name(self):
        while True:
            student_name = input("Please input a student's name or exit: ")
            if student_name == 'exit':
                self.parameters = {'name': "", 'score': {}}
                return
            if student_name in self.student_dict.keys():
                print("{} already exists".format(student_name))
                continue
            break
        self.student_dict[student_name] = {}
        self.parameters = {'name': student_name, 'score': {}}
        self.input_subject(student_name)
        return student_name

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
                self.student_dict[student_name][subject_name] = subject_score
                self.parameters['score'][subject_name] = subject_score
                break
            except Exception as e:
                print(e)
