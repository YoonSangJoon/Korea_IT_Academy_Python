# [인덱스] ==> 인덱싱
# [인덱스:인덱스] ==> 슬라이싱 (slicing)

lst = [10, 20, 30, 'A', 'B', 'C']
print(lst[0:2])    # [10, 20]
print(lst[-3:-1])  # ['A', 'B']
print(lst[:4])     # [10, 20, 30, 'A']
print(lst[2:])     # [30, 'A', 'B', 'C']
print(lst)         # [10, 20, 30, 'A', 'B', 'C']

# 참고 : 문자열(str)도 리스트다!
# "나는 피카츄다!" ---> [ "나", "는", " ", "피", "카", "츄", "다", "!" ]
s = "나는 피카츄다!"
print(s[3:6])

# quiz : 생년월일 6자리와 성별 1자리를 가지고, 나이와 생일, 성별을 출력
# 성별 : 1,2   3,4
#        1,2--> 1900대생 (1:남, 2:여)
#        3,4--> 2000대생 (3:남, 4:여)
# 191024-2  ==> 1919 10 24 여성
# 191024-3  ==> 2019 10 24 남성
info = input("YYMMDD-G : ")

year = int(info[0:2])
month = int(info[2:4])
day = int(info[4:6])
gender = int(info[-1])

if gender == 1 or gender == 2:
    year += 1900
else:
    year += 2000

if gender == 1 or gender == 3:
    gender = "남성"
else:
    gender = "여성"

###############################################
import datetime

# 프로그램이 실행되는 바로 지금 시간을 얻어옴
d = datetime.datetime.now()

# '해'를 구함
this_year = d.year
###############################################

print("생년월일 : {}년 {}월 {}일".format(year, month, day))
print("나이 : {}세".format(this_year - year + 1))
print("성별 : {}".format(gender))

