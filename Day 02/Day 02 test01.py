"""

# 정수 : int
# 실수 : float (double)
# 문자 : str  ( 문자열 데이터의 '+' 연산 : 두 단어를 합쳐라. 다른 자료형 데이터와는 덧셈 불가 )
# 참/거짓 : bool

"""

a = 10 + 20
b = '10' + '20'
# c = 10 + "20"  # 에러 !

print(a)  # 30
print(b)  # 1020

# 실행 : ctrl + shift + f10

# < 변수 (variables) >
# 데이터 1개를 보관하는 그릇 역할의 메모리
# 위의 a, b를 변수라 칭함
# 변수에 값을 저장 : 변수명 = 값
# 용도 : 값을 보관
# 변수 이름은 마음대로 정한다. (단, 숫자로 시작하면 안됨. 띄어쓰기 포함 안됨. 특수기호는 '$, _' 만 가능)
# 주의사항 : 변수는 '값 대입' 부터 시작한다.  -> 최초의 값 대입 시점에 변수가 생성됨.
# 예를들어
# num = 1
# print( num + 10 )
# 이 경우는 '11' 도출
# num = 1 없이 print ( num + 10 ) 만 입력할 경우 에러 발생.


"""
n1 = 1  # "=" 은 'equal'의 의미가 아님.
n2 = 2

n1 = n2         와    n2 = n1 은 다르다.
n1 : 2  n2 : 2        n2 : 1 n2 : 1

"""

a = 'b'
print(a)  # = b
print('a')  # = a

a = input( "a 정수 1개를 입력하시오..." )  # 무슨 값을 입력해야할 경우 먼저 변수부터 마련해야함. (변수에 값을 보관)
b = input( "b 정수 1개를 또 입력하시오..." )


print("a : ", a, "b : ", b)

# a 와 b의 값을 서로 교환하기 (swap)
c = a
a = b
b = c
print("a : ", a, "b : ", b)
