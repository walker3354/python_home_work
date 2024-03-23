class DelStu:
    def __init__(self,student_dict):
        self.student_dict = student_dict

    def execute(self):
        while True:
            student_name = input("Please input a student's name or exit: ")
            if student_name == 'exit':
                return self.student_dict
            if student_name not in self.student_dict.keys():
                print('The name {} is not found'.format(student_name))
                return self.student_dict
            del self.student_dict[student_name]
            print('Del {} success'.format(student_name))
        return self.student_dict