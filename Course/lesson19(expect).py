try:
    num_1 = int(input('please input a number to divide: '))
    num_2 = int(input("input a number to divide by: "))
except ZeroDivisionError:
    print("you can't divide zero")
except ValueError:
    print("please input number")
except Exception as e:
    print(e)
else:
    print(num_1/num_2)
finally:  # what ever waht happen the process will run this section
    print('process end')
