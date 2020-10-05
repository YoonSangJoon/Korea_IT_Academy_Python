# print() 함수 사용하기
# 화면에 출력하기 위해 사용
# Ctrl + /   해당 줄 주석 설정
# Ctrl + Shift + F10   함수 실행
# Ctrl + D   현재 줄 복붙
# Tab   블럭
# 밑에 빨간 ~ 표시 나올 시 문법 오류. 실행해도 오류 발생.
# "" 와 '' 는 차이 없음

print("hello python!")   # 문자열의 형태로 화면 출력할 때 쌍따옴표 사용 or 홀따옴표 사용
print("hello python!~~~~~~~")
print('hello python!!!')
print("100")
print(25.3)
print("25.3")
print()   # 실행 시 엔터 역할 (간격 띄우기)
print("25.3"+"35.6")   # "" + "" (문자열 + 문자열 의 경우 숫자가 아닌 문자로 인식하기 때문에 뒤에 이어서 나옴)
print(25.3+35.6)
print()
print(type("25.3"))   # 실행 시 <class 'str'>   '문자열 타입'임을 알려줌.
print(type(25.3))   # 실행 시 <class 'float'>   '소수점 타입'임을 알려줌.
print()
print("""문자열 출력""")
print('''문자열 출력2''')
print()
print('T', 'E', 'S', 'T')
print("test", 100, "hello")
print()

# print 문에 사용하는 옵션
# sep  =  Seperater  =  print문 안에 주어진 인자들을 출력할 때 구분을 무엇으로 할 것인지 지정 가능 (35 참고)
#                       아무것도 지정하지 않으면 공백이 기본값임 (공백이 없음) (34 참고)

print('TEST', 'exam', 'hello', sep='')   #이 경우 각 단어는 모두 붙어서 출력
print('2019', '07', '01', sep='_')   #sep 값을 '_'로 지정할 경우 각 단어가 '_'로 구분
print("TEST", 'exam', 'hello')
print()

# Quiz : niceman@google.com  =>  sep 옵션을 써서 화면에 출력하기.

print('niceman', 'google.com', sep='@')

# end 옵션  print() 함수의 끝을 엔터가 아닌 지정한 값으로 끝나게 할 수 있음

print("\n--end 옵션--")   # \n  다음 줄로 이동
print("Welcome To", end=' ')
print("the black parade")
print("Welcome To")
print("the black parade")

#python, 컴파일러, 인터프리터 (python.org에서 설치) 설치 후 pycharm 설치