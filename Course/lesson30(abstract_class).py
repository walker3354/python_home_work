from abc import ABC, abstractclassmethod


class Vehicle:
    @abstractclassmethod
    def go(self):
        pass

    def stop(self):
        print('Stop')


class Car(Vehicle):
    def go(self):
        print('You drive the car')


class Motorcycle(Vehicle):
    def go(self):
        print('You drive the motorcycle')


# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()
