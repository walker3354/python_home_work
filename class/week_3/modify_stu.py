def main(student_list):
    name = input("  Please input a student's name: ")
    find_success = False
    for i in student_list:
        if i[0] == name:
            try:
                i[1] = float(input("Please input {} new score: ".format(name)))
                print("Modify {} success".format(i))
                find_success = True
            except TypeError:
                print("please enter num")
            break
    if not find_success:
        print("The name {} is not found".format(name))
