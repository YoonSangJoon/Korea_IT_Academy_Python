"""

    < Module >
    => 함수, 클래스를 모아놓은 .py 파일
    => import 모듈명

        ** 모듈(.py)은 프로젝트 폴더 안에는 있어야 함
        ** 중첩 폴더인 경우 '.'을 사용

"""
import Day16.my

n = Day16.my.add(10, 20)
m = Day16.my.sub(10, 20)

print(n)
print(m)

p = Day16.my.Person('홍길동', 25)
p.print_info()


# from Day16.my import sub
# from Day16.my import sub, add, Person
from Day16.my import *  # '*' : all


m = sub(10, 20)
print(m)

p = Person()

###################################################
import random
random.randint(1, 10)
random.randint(1, 10)
random.randint(1, 10)
###################################################
from random import randint
randint(1, 10)
randint(1, 10)
randint(1, 10)














