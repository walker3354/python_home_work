# *arg => function parament omly have only and store with tuple format

def add(*test_arg):
    sum = 0
    for i in test_arg:
        sum += i
    return sum


def add_change_able(*test_arg):
    temp = list(test_arg)
    for i in range(len(test_arg)):
        temp[i] += 1
    return temp


print(add_change_able(1, 2, 3, 4, 5, 6))
