
"""
윤년 게산기

YEAR 를 INPUT()으로 입력 받는다.
입력된 YEAR가 윤년/평년인지 학인
# 윤년이면 True, 평년이면 False #

윤년의 기준
1. 4의 배수이면서 100의 배수가 아닌 해
2. 단 400의 배수인 해는 윤년

2019 : False
2020 : True
2300 : False
2400 : True
2500 : False
2600 : False
2700 : False
2800 : True
2900 : False
3000 : True

etc...

"""

# 1.
year = int(input("year : "))
print()
result = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
print(result)
print()
# 2.
if result:
    print("{}년은 윤년입니다.".format(year))
else:
    print("{}년은 평년입니다.".format(year))