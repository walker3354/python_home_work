class ModifyStu:
    def __init__(self,student_dict):
        self.student_dict = student_dict

    def execute(self):
        student_name = input("Please input a student's name or exit: ")
        if student_name not in self.student_dict.keys():
            print("can't find  {} date , inserting...".format(student_name))
            return self.student_dict

        subject_list = ""
        for subject in self.student_dict[student_name].keys():
            subject_list = subject_list + subject + " "
        print("current subject are {}".format(subject_list))
        change_subject = input("please input the subject you want to change: ")

        if change_subject not in self.student_dict[student_name].keys():
            print("subject error {} not in the std_list".format(change_subject))
            while True:
                try:
                    subject_score = int(
                        input(
                            "Please input {}'s {} score or < 0 for discarding the subject: ".format(student_name, change_subject)))
                    if subject_score < 0:
                        break
                    self.student_dict[student_name][change_subject] = subject_score
                    break
                except Exception as e:
                    print(e)
            return self.student_dict
        while True:
            try:
                change_score = float(input("Please input {}'s new score of {}:".format(
                    student_name, change_subject)))
                break
            except Exception as e:
                print(e)
        self.student_dict[student_name][change_subject] = change_score
        print(" Modify [{}, {}, {}] success".format(
            student_name, change_subject, change_score))
        return self.student_dict