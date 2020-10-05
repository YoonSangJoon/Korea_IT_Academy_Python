import random

"""
    문제1.
    두 정수를 랜덤하게 뽑는다. (범위 10 ~ 50)
    두 정수를 출력
    두 수 중 큰수 출력
"""
n1 = random.randint(10, 50)
n2 = random.randint(10, 50)

print("n1 : {}".format(n1))
print("n2 : {}".format(n2))

if n1 > n2:
    print("첫 번째 수가 더 큽니다.")
elif n1 < n2:
    print("두 번째 수가 더 큽니다.")
else:
    print("두 수가 같습니다.")

"""
    문제2.
    정수 1개를 입력 받는다. (input())
    이 정수가 2, 3, 5 배수인지 출력
    예) 4 --> 2의 배수
        6 --> 2의 배수
              3의 배수
        15 --> 3의 배수
               5의 배수
        7 --> 2, 3, 5의 배수 모두 아님
"""
n = int(input("정수 : "))
if n % 2 == 0:
    print("2의 배수")
if n % 3 == 0:
    print("3의 배수")
if n % 5 == 0:
    print("5의 배수")
if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
    print("2, 3, 5의 배수 모두 아님")

"""
    문제3. 가위바위보 게임
    컴퓨터 : 0~2 중 랜덤하게 1개 뽑기
    플레이어 : 0~2 중 입력 받기
    0 : 가위 / 1 : 바위 / 2 : 보

    컴퓨터와 플레이어가 각각 무엇을 냈는 지 출력
    누가 이겼는 지 출력
"""
gawi = 0
bawi = 1
bo = 2

com = random.randint(0, 2)  # 0 ~ 2 중 랜덤
player = int(input("가위(0), 바위(1), 보(2) : "))

# 컴퓨터, 플레이어가 각각 무엇을 냈는지
if com == gawi:
    s_com = "가위"
elif com == bawi:
    s_com = "바위"
else:
    s_com = "보"

if player == gawi:
    s_player = "가위"
elif player == bawi:
    s_player = "바위"
elif player == bo:
    s_player = "보"
else:
    s_player = "잘못된 입력입니다."
    exit(0)  # 프로그램 종료

print("컴퓨터 : {}".format(s_com))
print("플레이어 : {}".format(s_player))

# 승부 판단
# if player == gawi:
#     if com == player:
#         print("비겼다!")
#     elif com == bo:
#         print("이겼다!")
#     else:
#         print("졌다..")
# if player == bawi:
#     if com == player:
#         print("비겼다!")
#     elif com == gawi:
#         print("이겼다!")
#     else:
#         print("졌다..")
# if player == bo:
#     if com == player:
#         print("비겼다!")
#     elif com == bawi:
#         print("이겼다!")
#     else:
#         print("졌다..")

if com == player:
    print("비겼다!")
elif (player + 1) % 3 == com:
    print("졌다..")
else:
    print("이겼다!")

"""
    문제4. 구구단 문제 내기
    2단 ~ 9단 중 임의의 문제 1개를 내고
    사용자에게 답 입력 받음
    "정답!" 혹은 "땡.." 출력
"""
q1 = random.randint(2, 9)
q2 = random.randint(1, 9)

answer = int(input("문제 : {} X {}".format(q1, q2)))
if answer == q1 * q2:
    print("정답!")
else:
    print("땡..")






