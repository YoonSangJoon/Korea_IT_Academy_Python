"""

< 제어문 (Control Statement) >
- 프로그램 흐름을 제어
- 조건문 : if 문
- 반복문 : while 문, for 문
- 분기문 : break, return, pass

< if문 >
- 조건식의 True / False 의 결과에 따라 종속문장을 실행
- 형식 )
- if 조건식 : 조건식이 True 면 실행할 문장들 (종속문장)

- 종속문장들은 반드시 들여쓰기 (Tab) 를 해야함 (혹은 공백 4칸)

"""

age = int(input("나이 : "))
if age >= 20 :  #  조건식
    print("성인입니다.")  #  종속문장
else:                   #  if 조건식이 False 일 경우 실행.
    print("미성년입니다.")

if age <= 7 :
    print("미취학 아동")
elif age <= 13 :
    print("초등학생")
elif age <= 16:
    print("중학생")
elif age <= 19 :
    print("고등학생")
else :
    print("대학생 혹은 일반 성인")