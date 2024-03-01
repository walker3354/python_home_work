import quiz1, quiz2, quiz3, quiz4, quiz5
# made by walker(109360723)


def main():
    keep_going = "y"
    while keep_going == "y":
        print("1. Print double triangle")
        print("2.Print spacing triangle")
        print("3. Print diamond")
        print("4.Print grid")
        print("5. Guessing game")
        usr_chose = int(input("Please enter quiz's number: "))
        if usr_chose == 1:
            quiz1.quiz1()
        elif usr_chose == 2:
            quiz2.quiz2()
        elif usr_chose == 3:
            quiz3.quiz3()
        elif usr_chose == 4:
            quiz4.quiz4()
        elif usr_chose == 5:
            quiz5.quiz5()
        else:
            print("invaild input please try again!")
        keep_going = input("Test again(y)?")


main()
