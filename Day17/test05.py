# 상속 (원본 클래스를 물려받은 새클래스를 만드는 것)

class Animal:
    def walk(self):
        print("이동중..")

    def eat(self):
        print("먹는중..")


class Dog(Animal):
    def __init__(self):
        self.name = "강아지"

class Cat(Animal):
    def __init__(self):
        self.name = "고양이"

a1 = Dog()
a2 = Cat()

print(a1.name)
a1.eat()
a1.walk()

print(a2.name)
a2.eat()
a2.walk()