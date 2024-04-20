from Socket_client import Socket_client


class ModifyStu:
    def __init__(self):
        self.student_name = ''
        self.socket = Socket_client()

    def check_student_name(self):
        self.socket.send_command('query', {'name': self.student_name})
        return_data = self.socket.wait_response()
        if return_data['status'] == 'OK':
            return return_data
        return False

    def input_student_name(self):
        student_name = input("Please input a student's name or exit: ")
        if student_name == 'exit':
            return
        subject_list = self.check_student_name()
        if subject_list != False:
            self.modify_student_subject(subject_list)

    def modify_student_subject(self, return_data):
        print("current subjects are ", end="")
        for subject in return_data['scores'].keys():
            print(f"{subject} ", end="")

        while True:
            changed_subject = input(
                "\nPlease input a subject you want to change: ")
            if changed_subject in return_data['scores']:
                break
            print("input input subject error please try again")

        while True:
            try:
                subject_new_score = int(input(f"Add a new subject for Test2 please input {
                                        changed_subject} score or < 0 for discarding the subject: "))
                break
            except Exception as e:
                print(e)

        return_data['scores'][changed_subject] = subject_new_score
        self.socket.send_command(
            'modify', {'name': self.student_name, 'scores_dict': return_data['scores']})
        if self.socket.wait_response()['status'] == 'OK':
            print(f"Add [{self.student_name} , {
                  changed_subject} , {subject_new_score} success")
