def print_star(num_stars):
    print("*" * num_stars)


def quiz1():
    int_usr_num = int(input("Please enter a value: "))
    for i in range(int_usr_num, 0, -1):
        print_star(i)
    for i in range(2, int_usr_num + 1):
        print_star(i)
