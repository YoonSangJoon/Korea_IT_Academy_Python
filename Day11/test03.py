"""

    < 함수 (function) >
    - 기능
    - input/output 이 있는 형태
    - 비슷한 작업을 자주 해야할 때 주로
      명령들을 하나의 함수로 작성하여 사용
    - 형식)
        함수 정의
        def 함수명(매개변수1, 매개변수2, ..):
            해야 할 일(들)
            return 리턴값

        ** 매개변수? 재료(input, 인자값)가 들어올 변수
                    (통로 역할)
                    재료의 개수와 일치해야 함!
                    재료가 필요없는 경우 ()만 쓰면 됨
        ** 리턴값? 함수의 결과값 (output)
                    호출 1번 당 1개의 리턴값만 받을 수 있음
                    (여러 값을 돌려주고 싶다면 튜플로 return)
            예) return a
                return b   ==> (X)

                return (a, b) ==> (o)

                return a, b   ==> (o) (얘도 튜플임)

                ==> return 명령은 '함수를 종료'시키는 기능이 있음

        함수 호출
        함수명(재료1, 재료2)
        ** 인자값 : 재료가 되는 값
                    매개변수 개수에 맞춰서 값을 넣어야 함

"""


# 함수 정의 (=함수 만들기)
def circle_area(r):  # r은 매개변수(parameter)
    area = r ** 2 * 3.14
    return area


# 함수 호출 (=함수 실행)
a = circle_area(10)  # 10 은 인자값 (argument)
b = circle_area(20)  # 20 은 인자값 (argument)
print(a)
print(b)


def func1():  # 재료 필요 없으면 매개변수 없어도 됨
    print("ㅎㅇㅎㅇ")
    # 결과값(리턴값)이 필요 없으면 return 안써도 됨


func1()
func1()
func1()


def func2(p1, p2):  # 매개변수는 ',' 로 여러 개 선언
    return p1 + p2

print( func2(10, 20) )


def func3(p1='abc', p2='def'):
    print("p1 : ", p1)
    print("p2 : ", p2)


func3()
func3(1)
func3(1, 2)
# func3(1, 2, 3)


def func4(*a):
    for e in a:
        print(e)
    print("a의 자료형 : {}".format( type(a) ))


func4(10, 20, 30, "ABC", "ㅋㅋ", True)


def func5(a):
    return a*10, a*100, a*1000


v = func5(3)
v1, v2, v3 = func5(5)

print(v)
print(v1)
print(v2)
print(v3)


# quiz01 : 정수 1개 넣고, 그 개수만큼 "*"을 출력
#  예) quiz01(3)    ==> ***
def quiz01(a):
    print('*' * a)


quiz01(2)
quiz01( int(input("별 개수:") ) )


# quiz02 : 두 수와 연산기호 1개(str)를 넣고 그 식의 결과 출력
#  예) quiz02(2, 1.1, '*')  ==> 2.2
#   연산기호는 : + - * / % 외에는 "잘못된 기호입니다" 를 출력
def quiz02_1(n1, n2, op):
    ops = ['+', '-', '*', '/', '%']
    if op in ops:
        if op == '+': return n1 + n2
        if op == '-': return n1 - n2
        if op == '*': return n1 * n2
        if op == '/': return n1 / n2
        if op == '%': return n1 % n2
    else: return '잘못된 기호입니다.'


print(quiz02_1(2, 1.1, '*'))

result = quiz02_1(2, 1.1, '*')
print(result)


def quiz02_2(n1, n2, op):
    if op == '+': print(n1 + n2)
    elif op == '-': print(n1 - n2)
    elif op == '*': print(n1 * n2)
    elif op == '/': print(n1 / n2)
    elif op == '%': print(n1 % n2)
    else: print('잘못된 기호입니다.')


quiz02_2(2, 1.1, '*')

# 참고 : 좋은 함수는 기능이 1개인 함수다!








