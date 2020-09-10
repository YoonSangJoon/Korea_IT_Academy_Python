"""

    < 재귀호출 (recursive call) >
    - 함수가 함수 자신을 호출하는 것
    - def a():
        a() <-- 요거!

"""


def a(num):  # num : 5
    print("현재 num:", num)
    if num == 0:
        return
    a(num-1)  # a(4)
    print("a() 마지막 문장 num:", num)


a(5)


# factorial 함수 만들기
def fact(n):  # 4
    if n == 1:
        return n
    return n * fact(n-1)

print("4! : {}".format( fact(4) ) )  # 24
print("3! : {}".format( fact(3) ) )
print("10! : {}".format( fact(10) ) )








