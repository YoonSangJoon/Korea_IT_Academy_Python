"""
    < 레퍼런스 (reference) >
    -> 오브젝트가 위치한 메모리 주소
    -> id

    < self 변수 >
    -> self에는 오브젝트의 레퍼런스가 자동으로 들어간다.
    -> 실제 오브젝트는 '필드'만 가지고 있음
        메서드(함수)는 오브젝트가 각각 가지는 것이 아니라,
        다른 곳에 따로 만들어짐
        -> 오브젝트가 100개여도 메서드는 1개뿐!
           메서드 입장에서는 어떤 오브젝트가 자신을 호출했는지
           오브젝트 정보 (오브젝트의 주소)를 받게 되어있음.
           이것을 '0번 인자'라고 하고,
           메서드가 호출되면 이는 self에 자동으로 들어감.

"""

class person:
    def __init__(self, n="", a=0):
        self.name = n
        self.age = a

    def show(self):
        print(self.name)

p1 = person("홍길동", 10)
p2 = person("고길동", 20)
p3 = person("푸린")

print(id(p1))
print(id(p2))

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)