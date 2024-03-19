import random

x = random.randint(1, 6)  # generate an random number between 1 to 6
y = random.random()  # generate a number between 0 to 1 (float)

# random access list
test_list = ['rock', 'paper', 'scissors']
z = random.choice(test_list)

# shuffle the list
card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'k']
random.shuffle(card_list)
print(card_list)
# [2, 'Q', 8, 5, 3, 9, 6, 7, 'J', 1, 4, 'k']
