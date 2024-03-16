def main(student_dict):
    while True:
        student_name = input("Please input a student's name or exit: ")
        if student_name == 'exit':
            return
        if student_name in student_dict:
            print("{} already exists".format(student_name))
            continue
        break
    student_dict[student_name] = {}

    while True:
        subject_name = input(
            "Please input a subject name or exit for ending: ")
        if subject_name == 'exit':
            break
        while True:
            try:
                subject_score = int(
                    input(
                        "Please input {}'s {} score or < 0 for discarding the subject: ".format(student_name, subject_name)))
                if subject_score < 0:
                    break
                student_dict[student_name][subject_name] = subject_score
                break
            except Exception as e:
                print(e)
