def main(student_dict):
    student_name = input("Please input a student's name or exit: ")
    if student_name not in student_dict.keys():
        print("can't find  {} date".format(student_name))
        return

    subject_list = ""
    for subject in student_dict[student_name].keys():
        subject_list = subject_list + subject + " "
    print("current subject are {}".format(subject_list))
    change_subject = input("please input the subject you want to change: ")

    if change_subject not in student_dict[student_name].keys():
        print("subject error {} not in the std_list".format(change_subject))
        return
    while True:
        try:
            change_score = float(input("Please input {}'s new score of {}:".format(
                student_name, change_subject)))
            break
        except Exception as e:
            print(e)
    student_dict[student_name][change_subject] = change_score
    print(" Modify [{}, {}, {}] success".format(
        student_name, change_subject, change_score))
