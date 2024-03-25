class Prey:

    def flee(self):
        print('this animal flees')


class Predator:

    def hunt(slef):
        print('this animal is hunting')


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


fish_1 = Fish()

fish_1.flee()
fish_1.hunt()
