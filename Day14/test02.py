"""

    클래스 : Student
    멤버변수(=필드)
        - 이름
        - 국어 점수
        - 영어 점수
        - 수학 점수
        - 평균 점수
        - 등급
            (A, B, C, D, F 중 하나)
            (100, 80, 60, 40, 10)

    멤버함수(=메서드)
        - print_student() : 모든 정보 출력
        - input_student() : 모든 정보 입력 (input() 사용)
                        ==> 이름, 국, 영, 수 는 input()
                        ==> 평균, 등급은 컴퓨터가 계산

    문제 1) 학생 object 1개 만들고, 정보들을 저장 및 출력.
    문제 2) 학생 object 4개 만들고, 정보들을 저장 및 출력.
            ** 힌트 : 리스트를 사용하면 좋다.
    문제 3) 2번째 학생의 영어 점수를 30점으로 수정하고 모든 정보 출력.
            (이때, 평균과 등급도 재계산되도록)
    문제 4) 위의 2번 문제에서 생성된 4개의 학생 객체 중 가장 평균 점수가 높은 학생의 이름, 평균 점수 출력.

"""

class Student:
    def __init__(self):
        self.name = ""  # 값은 어차피 바뀔 것이기 때문에 대충 지어도 됨.
        self.kr = 0
        self.en = 0
        self.ma = 0
        self.avg = 0
        self.grade = "A"
        print("학생 오브젝트 생성 완료 !")

    def print_student(self):    # 오브젝트의 필드 정보를 출력하는 함수
                                # 정보들을 str으로 변환하는 작업은 get_info()에게 맡김.
        print(self.get_info())

    def get_info(self):     # 오브젝트의 필드 정보를 하나의 str으로 묶는 함수.
        return '{} / 국 {} / 영 {} / 수 {} / 평균 {} / {}'\
            .format(self.name, self.kr, self.en, self.ma, self.avg, self.grade)
    def input_student(self):
        self.name = input("이름 : ")
        self.kr = int(input("국어 점수 : "))
        self.en = int(input("영어 점수 : "))
        self.ma = int(input("수학 점수 : "))
        self.set_average()
        self.set_grade()

    def set_average(self):
        self.avg = int(self.ma + self.en + self.kr) / 3
        return self.avg

    def set_grade(self):
        if self.avg >= 90:
            self.grade = "A"
        elif self.avg >= 80:
            self.grade = "B"
        elif self.avg >= 70:
            self.grade = "C"
        elif self.avg >= 60:
            self.grade = "D"
        else:
            self.grade = "F"

"""
# 문제 1) 학생 object 1개 만들고, 정보들을 저장 및 출력.
s = Student()
s.input_student()   # 정보 입력
s.print_student()   # 정보 출력
"""

"""
# 문제 2) 학생 object 4개 만들고, 정보들을 저장 및 출력.
             ** 힌트 : 리스트를 사용하면 좋다.
"""
s = [Student(), Student(), Student(), Student()]
for i in range(len(s)): # len(리스트명) : 리스트의 현재 원소 갯수(int형)
    s[i].input_student()

for st in s:
    st.print_student()

"""
# 문제 3) 2번째 학생의 영어 점수를 30점으로 수정하고 모든 정보 출력.
             (이때, 평균과 등급도 재계산되도록)
"""
s[1].en = 30
s[1].set_average()  # 평균 재계산
s[1].set_grade()    # 학점 재계산
s[1].print_student()

"""
# 문제 4) 위의 2번 문제에서 생성된 4개의 학생 객체 중 가장 평균 점수가 높은 학생의 이름, 평균 점수 출력.
"""
max_st = s[0]
for st in s:
    if max_st.avg < st.avg:
        max_st = st

print("1등 학생 이름 {} (점수 : ()점)".format(max_st.name, max_st.avg))

"""
a = Student()
b = Student()
c = Student()
d = Student()
e = Student()

의 경우 반복문 사용 불가
"""

s = [Student(), Student(), Student(), Student()]
# s =  s[0]       s[1]       s[2]        s[3]

for i in range(4):  # i = 0 ~ 3
    s[i].input_student()
    s[i].print_student()