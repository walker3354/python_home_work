import random


def quiz5(min=0, max=100, limit=10):
    counter = 0
    answer = random.randint(min, max)
    while counter < limit:
        usr_guess = int(
            input("Please guess a number from {} to {}: ".format(min, max)))
        if usr_guess == answer:
            print("You pass")
            break
        elif usr_guess > min and usr_guess < answer:
            min = usr_guess
        elif usr_guess < max and usr_guess > answer:
            max = usr_guess
        counter += 1
