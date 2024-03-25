class Car:
    wheels = 4  # class variable "ALL class var can share this"

    def __init__(self, make, model, year, color):
        self.make = make  # instance variable "only obj him self can use"
        self.year = year
        self.color = color
        self.model = model

    def drive(self):
        print(f"This {self.model}'s car is driving")

    def stop(self):
        print(f"this {self.model}'s car is stopped")
