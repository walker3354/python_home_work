class Car:

    def turn_on(self):
        print('You start the engine')
        return self

    def drive(self):
        print('You drive the car')
        return self

    def brake(self):
        print('You step on the brakes')
        return self

    def turn_off(self):
        print('You turn off the engine')
        return self


car = Car()
car.turn_on().drive()  # You start the engine + You drive the car

'''
class StringBuilder:
    def __init__(self):
        self.string = ""

    def append(self, text):
        self.string += text
        return self  # 返回自己以支持方法鏈

    def reverse(self):
        self.string = self.string[::-1]
        return self

    def uppercase(self):
        self.string = self.string.upper()
        return self

# 使用方法鏈
result = StringBuilder().append("hello").reverse().uppercase().append(" world").reverse().uppercase().string
print(result)  # 輸出: DLROW OLLEH
'''
