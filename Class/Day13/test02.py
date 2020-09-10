"""

    < 클래스 >
    - Object(객체, 물체)
      Class (Object를 만들 때 사용하는 틀, 설계도)
    - 클래스 안에 정의하는 '함수' ==> 메서드 (Method)
"""
class Unit:  # 클래스 정의 ( 설계도 만들기 )
    def __init__(self):  # __init__() : 생성자 메서드
                         # Object를 생성할 때 자동으로 실행되는 메서드
                         # 이 안에는 '멤버변수(=field)'를 생성한다.
        self.name = "없음"  # self.변수명 : 클래스의 멤버변수(=field)
        self.hp = 100
        self.ap = 100

    def attack(self):
        print("{}의 공격개시! 공격력 : {}".format(self.name, self.ap))

    def info(self):
        print("이름 :", self.name)
        print("체력 :", self.hp)
        print("공격력 :", self.ap)


w = Unit()  # 클래스명() --> 해당 클래스의 생성자 메서드 실행
            #           --> 새로운 Object 생성 (클래스 모양 대로)
            #           --> 자동으로 해당 클래스의 __init__()이 실행됨

w.name = "전사"  # '.' : ~의
w.hp = 1000
w.ap = 200

m = Unit()
m.name = "법사"
m.hp = 200
m.ap = 500

t = Unit()
t.name = "탱커"
t.hp = 10000
t.ap = 50

w.info()
m.info()
t.info()

w.attack()
m.attack()
t.attack()