"""

    < while문 >
    형식:
    while 조건식:
        조건식이 True일 동안 반복할 문장들 (while문의 종속문장)

    순서:
     조건식 검사 -> True면 -> 종속문장 -> 조건식 검사 -> True -> 종속문장
     ... -> 조건식 검사 -> False면 -> 종료
"""

# 1 ~ 10 출력
n = 1
while n <= 10:
    print(n)
    n += 1
print("마지막 n :", n)

# 구구단 3단 출력
# print("{} X {} = {}".format(3, 1, 3*1))
# print("{} X {} = {}".format(3, 2, 3*2))
# print("{} X {} = {}".format(3, 3, 3*3))
# print("{} X {} = {}".format(3, 4, 3*4))
# print("{} X {} = {}".format(3, 5, 3*5))
# print("{} X {} = {}".format(3, 6, 3*6))
# print("{} X {} = {}".format(3, 7, 3*7))
# print("{} X {} = {}".format(3, 8, 3*8))
# print("{} X {} = {}".format(3, 9, 3*9))
# loop : 반복문
n = 1
while n <= 9:
    print("{} X {} = {}".format(3, n, 3*n))
    n += 1

# TODO 2단 ~ 9단을 모두 출력하기! (while문 안에 while문을 또 넣을 수 있음)
dan = 2
while dan <= 9:
    n = 1
    while n <= 9:
        print("{} X {} = {}".format(dan, n, dan * n))
        n += 1
    dan += 1



