class Pokemon:
    def __init__(self):
        self.name = "없음"
        self.hp = 1000
        self.skill = "없음"
        print("포켓몬 생성 완료!")

    def input_info(self, name="없음", hp=0, skill="없음"):
        if name == "없음" and hp == 0 and skill == "없음":
            self.name = input("새 이름 :")
            self.hp = int(input("체력 :"))
            self.skill = input("스킬 :")
        else:
            self.name = name
            self.hp = hp
            self.skill = skill
        print("포켓몬 정보 저장 완료!")
        
    def print_info(self):
        print("{} / HP:{} / SKILL:{}".format(self.name, self.hp, self.skill))

    def input_info2(self):
        self.name = input("이름 : ")
        self.hp = int(input("체력 : "))
        self.skill = input("기술 : ")

# 포켓몬 3마리 추가
p1 = Pokemon()
p2 = Pokemon()
p3 = Pokemon()

"""
# 정보 저장
p1.input_info("피카츄", 10000, "백만볼트 공격")
p2.input_info("라이츄")
p3.input_info()
"""

p1.input_info2()
p2.input_info2()
p3.input_info2()

# 정보 출력
p1.print_info()
p2.print_info()
p3.print_info()