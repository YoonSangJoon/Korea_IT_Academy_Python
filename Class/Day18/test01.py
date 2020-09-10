"""

    < 상속 >
    - 원본클래스를 재사용하여 새 클래스를 만드는 것
    - 원본 : 부모 클래스 (=슈퍼클래스, 상위클래스)
      새   : 자식 클래스 (=서브클래스, 하위클래스)

    - 형식)
        class 자식클래스명(부모클래스명):
            ...

    < Override >
    - 메서드 재정의
    - 부모가 물려준 메서드의 바디(본문) 부분을
       자식 클래스가 다시 작성하는 것

"""

class Hero:
    def attack(self):
        print("영웅, 공격 개시!!!")

class Superman(Hero):  # Hero 의 자식 클래스 Superman
    def attack(self):  # 물려받은 attack() 오버라이드
        print("슈퍼맨, 핵주먹 공격!!!")

class Batman(Hero):
    def attack(self):
        print("배트맨, 최첨단 무기로 공격!!")

class Spiderman(Hero):
    def attack(self):
        print("스파이더맨, 거미줄 공격!")

"""
su = Superman()
su.attack()

ba = Batman()
ba.attack()

sp = Spiderman()
sp.attack()
"""

heros = [Superman(), Batman(), Spiderman()]
for h in heros:
    h.attack()

