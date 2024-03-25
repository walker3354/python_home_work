class Animal:

    def eat(self):
        print('this Animal is eating')


class Rabbit(Animal):

    def eat(self):
        print('this rabbit is eating')


rabit_1 = Rabbit()
rabit_1.eat()
# out "this rabbit is eating"
