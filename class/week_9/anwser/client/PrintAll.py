from Socket_client import Socket_client


class PrintAll:

    def __init__(self):
        self.socket = Socket_client()
        self.socket.send_command('show', {})
        self.student_dict = self.socket.wait_response()['parameters']

    def execute(self):
        print("\n==== student list ====\n")
        for index_1, value_1 in self.student_dict.items():
            print('Name:{}'.format(index_1))
            for index_2, value_2 in value_1['scores'].items():
                print('   subject: {},score:{}'.format(index_2, value_2))
            print()
        print("======================")

    '''
    def show_student_subject(self, student_name):
        print('  current subjects are', end="")
        studen_subject = list()
        for subject in self.student_dict[student_name].keys():
            print(f"{subject} ")
            studen_subject.append(subject)
        return studen_subject
    '''
