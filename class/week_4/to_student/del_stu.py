def main(student_dict):
    while True:
        student_name = input("Please input a student's name or exit: ")
        if student_name == 'exit':
            return
        if student_name not in student_dict.keys():
            print('The name {} is not found'.format(student_name))
            return
        del student_dict[student_name]
        print('Del {} success'.format(student_name))
