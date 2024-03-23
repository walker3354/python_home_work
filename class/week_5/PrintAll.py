class PrintAll:
    def __init__(self,student_dict):
        self.student_dict = student_dict

    def execute(self):
        print("\n==== student list ====\n")
        for index_1, value_1 in self.student_dict.items():
            print('Name:{}'.format(index_1))
            for index_2, value_2 in value_1.items():
                print('   subject: {},score:{}'.format(index_2, value_2))
            print()
        print("======================")
        return self.student_dict