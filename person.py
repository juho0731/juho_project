class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

    def __add__(self, other):
        new = Marriage(self, other)
        return new

class Marriage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_familly(self):
        print("[가족 구성]")
        self.x.print_name()
        self.y.print_name()

a = Person("철수")
b = Person('영희')
# a + b -> a.__add__(b)
m = a + b
m.print_familly()

