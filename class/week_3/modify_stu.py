def main(student_list):
    name = input("  Please input a student's name: ")
    for i in student_list:
        if i[0] == name:
            i[1] = modify_score(name)
            return
    print("The name {} is not found".format(name))


def modify_score(name):
    while True:
        try:
            new_score = float(input(
                "Please input {} new score: ".format(name)))
            print("Modify {} success".format(new_score))
            break
        except ValueError:
            print("please enter num")
            continue
    return new_score
