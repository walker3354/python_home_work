def main(student_list):  # done
    name = input("  Please input a student's name: ")
    try:
        score = float(input("  Please input {} score: ".format(name)))
    except TypeError:
        print("please enter number")
    student_list.append([name, score])
    print("add [{},{}] success".format(name, score))
