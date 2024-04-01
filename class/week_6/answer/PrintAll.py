class PrintAll:

    def execute(self, student_dict):
        print("\n==== student list ====\n")
        for index_1, value_1 in student_dict.items():
            print('Name:{}'.format(index_1))
            for index_2, value_2 in value_1.items():
                print('   subject: {},score:{}'.format(index_2, value_2))
            print()
        print("======================")
