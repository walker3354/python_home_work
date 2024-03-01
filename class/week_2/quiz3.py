def quiz3():
    int_usr_num = int(input("Please input odd number:"))
    while int_usr_num % 2 == 0:
        int_usr_num = int(input("Please input odd number:"))
    for i in range(1, int_usr_num + 1):
        print(" " * (int_usr_num - i) + "*" * (2 * i - 1))
    for i in range(int_usr_num - 1, 0, -1):
        print(" " * (int_usr_num - i) + "*" * (2 * i - 1))
