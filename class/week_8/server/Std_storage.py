import pickle


class Std_storage:
    def __init__(self, parameters={}):
        self.student_dict = dict()
        self.parameters = parameters

    def read_studet_file(self):
        try:
            with open("student_dict.db", 'rb') as fp:
                self.student_dict = pickle.load(fp)
        except Exception as e:
            # print(f"Error occur {e}")
            pass

    def store_student_file(self):
        with open('student_dict.db', 'wb') as fp:
            pickle.dump(self.student_dict, fp)

    def add(self):
        self.read_studet_file()
        student_name = self.parameters['name']
        subject = self.parameters['score']
        if student_name in self.student_dict.keys():
            return {'status': 'Fail', 'reason': 'The name already exists.'}
        else:
            self.student_dict[student_name] = subject
        self.store_student_file()
        return {'status': 'OK'}

    def show(self):
        self.read_studet_file()
        return_message = {'status': 'OK', 'parameters': {}}
        if len(self.student_dict) != 0:
            for student_name, student_subject in self.student_dict.items():
                return_message['parameters'].update(
                    {student_name: {'name': student_name, "score": student_subject}})
        return return_message
