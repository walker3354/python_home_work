from test_folder.Car import Car

car_1 = Car('chevy', 'corvette', 2021, 'blue')
car_2 = Car('toyota', 'rover', 2022, 'black')

Car.wheels = 2

print(car_1.wheels)
print(car_2.wheels)

# car_1.wheels = 4
# print(car_1.wheels)  => 4
