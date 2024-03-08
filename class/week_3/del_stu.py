def main(student_list):  # done
    name = input("  Please input a student's name: ")
    del_success = False
    for i in student_list:
        if i[0] == name:
            student_list.remove(i)
            del_success = True
    if del_success:
        print("Del {} success".format(name))
    else:
        print("can't find {} data".format(name))
