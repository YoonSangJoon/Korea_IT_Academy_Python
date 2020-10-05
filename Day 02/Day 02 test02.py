"""

< input() 함수 >
키보드로 값을 입력 받는 명령

방법 1.   input()  -  아무 메시지 없이 입력 받음.

방법 2.   input(문자열)  -  문자열을 메시지로 출력한 뒤 입력 받음.
                       -  입력된 데이터는 무조건 문자형 데이터로 인식한다. (아무리 숫자를 입력해도...)
                       -  문자형 데이터를 다른 형태로 변경해야한다. ("형변환" 이라고 일컫는다.)
"""

# a = input()
# b = input("아무거나 : ")

a = input("정수1 : ")  # 10
b = input("정수2 : ")  # 20
print(a)  # 10
print(b)  # 20
print(a + b)  # 1020
print(int(a) + int(b))  # 30   (형변환)

"""
        < 형변환(casting) >
        - 데이터를 다른 자료형으로 잠깐 변환
        - int(데이터) -> 정수형으로 변환
        - float(데이터) -> 실수형으로 변환
        - str(데이터) -> 문자형으로 변환
        - bool(데이터) -> true/false 로 변환     
"""

a = int("1004")
b = int(3.99999)  # int 사용시 반올림없음. 소숫점 뒷자리 다 삭제됨.
c = str(10)
d = bool(0)
e = bool("AAA")
print(a, type(a))  # type : 변수가 어떤 형식의 자료인지를 나타내는 함수
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))

# 참고 : 다른 자료형 데이터의 True/False 의 기준 (bool)
# --> 0, "", 0.0 등의 내용물이 없거나 0인 데이터는 False
# --> 데이터가 1개라도 들어있거나 0이 아닌 모든 데이터는 True