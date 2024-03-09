def main(student_list):  # done
    name = input("  Please input a student's name: ")
    while True:
        try:
            score = float(input("  Please input {} score: ".format(name)))
            break
        except ValueError:
            print("please enter number")
            pass
    student_list.append([name, score])
    print("add [{},{}] success".format(name, score))
