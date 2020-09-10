# 여러 변수, 여러 데이터를 한꺼번에 출력하는 방법
age = 10
name = "홍길동"
tall = 110.4

print(name, "의 나이는", age, "세이며, 키는", tall, "cm 이다.")
print("{}의 나이는 {}세이며, 키는 {}cm 이다.".format(name, age, tall))

# 차이점 : 1번 방법은 tuple형. 2번 방법은 str형
message1 = name, "의 나이는", age, "세이며, 키는", tall, "cm 이다."
message2 = "{}의 나이는 {}세이며, 키는 {}cm 이다.".format(name, age, tall)

print(message1)
print(message2)
print(type(message1))
print(type(message2))

############################################################
a, b = 10, 20
print(a)
print(b)

print("변환 전 a, b : {}, {}".format(a, b) )
a, b = b, a
print("변환 후 a, b : {}, {}".format(a, b) )
############################################################
# 연산자 (operators) : 연산 기호들

"""
    < 산술 연산자 >
    +, -, *, /, //, %, **
    // : 몫
    %  : 나머지 (mod 연산)
    ** : 제승

"""
print(10 / 4)  # 2.5
print(10 // 4) # 2  (몫만)
print(10 % 3)  # 1  (나머지만)
print(10 ** 3) # 10의 3제곱 (1000)

# 퀴즈 : 정수를 1개 입력(input()) 분/초 출력
# 입력 예 : 200
# 출력 예 : 3분 20초

sec = int(input("초:"))
print("{}분 {}초".format( sec // 60 , sec % 60 ))

"""
    < 대입 연산자 >
    =, +=, -=, *=, /=, **=, //= 
    
    a -= b   ---> a = a - b
    a **= 10 ---> a = a ** 10

"""
score = 0
score += 10  # score = score + 10
score += 10  # score = score + 10
score += 10  # score = score + 10
print("최종 점수 :", score)

"""
    < 비교 연산자 >
    두 수을 비교 (크냐 작냐 같냐)
    <, <=, >, >=, ==, !=
    
    == : 같다
    != : 같지 않다
    
    ** 비교연산자의 결과값은 bool형 (True, False)

"""

# quiz : 아까 입력한 '초'가 3의 배수인지 True/False 로 출력
print( sec % 3 == 0 )

"""

    < 논리 연산자 >
    and, or, not
    a and b : a와 b 둘 다 True 여야 최종 결과 True (논리 AND 연산자)
    a or b  : a와 b 둘 중 하나라도 True 면 최종 결과 True (논리 OR 연산자)
    not a   : a가 True 면 최종 결과 False 
                  False 면 최종 결과 True (논리 NOT 연산자)
"""

num = int(input("정수:"))
print(num >= 10 and num % 2 == 0)  # num 이 10 이상이고 짝수니?
print(num >= 10 or num % 2 == 0)   # num 이 10 이상이거나 짝수니?

# 3의 배수니?
print(not num % 3)

print(not 0)
print(not -2.134)
print(0 or -100 and 10 >= 10)











