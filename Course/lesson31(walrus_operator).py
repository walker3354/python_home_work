# walurs_operator (:=) make code more efficient
# python 3.8

foods_1 = list()

while True:
    food = input('what food you want?')
    if food == 'exit':
        break
    foods_1.append(food)


foods_2 = list()

while food := input('what food you want?') != 'quit':
    foods_2.append(food)
