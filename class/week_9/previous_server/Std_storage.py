import pickle


# structure {'student_name' : {'subject_1' : subject_1's score}}
class Std_storage:
    def __init__(self, parameters={}):
        self.student_dict = dict()
        self.parameters = parameters

    def read_studet_file(self):
        try:
            with open("student_dict.db", "rb") as fp:
                self.student_dict = pickle.load(fp)
        except:
            pass

    def store_student_file(self):
        with open("student_dict.db", "wb") as fp:
            pickle.dump(self.student_dict, fp)

    def add(self):
        try:
            self.read_studet_file()
            student_name = self.parameters["name"]
            self.student_dict[student_name] = self.parameters["scores"]
            self.store_student_file()
        except Exception as e:
            print(e)
        return {"status": "OK"}

    def show(self):
        self.read_studet_file()
        return_message = {"status": "OK", "parameters": {}}
        if len(self.student_dict) != 0:
            for student_name, student_subject in self.student_dict.items():
                return_message["parameters"].update({student_name: {"name": student_name, "scores": student_subject}})
        return return_message

    def query(self):
        self.read_studet_file()
        if self.parameters["name"] in self.student_dict.keys():
            return {"status": "OK","scores": self.student_dict[self.parameters["name"]]}
        else:
            return {"status": "Fail", "reason": "student no find"}

    def modify(self):
        self.read_studet_file()
        self.student_dict[self.parameters["name"]] = self.parameters["scores_dict"]
        self.store_student_file()
        print(f"Modify {self.parameters['name']} success")
        return {"status": "OK"}

    def delete(self):
        self.read_studet_file()
        del self.student_dict[self.parameters['name']]
        print(f'Del {self.parameters['name']} success')
        self.store_student_file()
        return {'status':'OK'}
