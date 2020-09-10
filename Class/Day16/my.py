def add(a, b):
    return a + b


def sub(a, b):
    return a - b


class Person:
    def __init__(self, n="", a="0"):
        self.name = n
        self.age = a

    def print_info(self):
        print("{} / {}세".format(self.name, self.age))