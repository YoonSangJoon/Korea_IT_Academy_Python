# 구구단 문제를 랜덤하게 계속 냄
# 사용자가 exit 를 입력하면 프로그램 종료
import random

s_log = ""  # 로그 기록(str)을 누적할 변수
print("종료는 exit를 입력하세요..")
while True:
    n1 = random.randint(2, 9)
    n2 = random.randint(1, 9)
    print("{} X {} = ?".format(n1, n2))
    user = input("입력 : ")
    if user == 'exit':
        break
    elif int(user) == n1 * n2:
        print("정답!")
    else:
        print("땡..")
    s_log += "{} X {}".format(n1, n2) + ", " \
          + user + ", " \
          + str( int(user) == n1 * n2 ) + "\n"
#  ==> 구구단 문제, 사용자 답, 정답 여부(True, False)를 log.txt에 저장
print(s_log)


f = open("log.txt", "w")
f.write(s_log)
f.close()

"""
    예) log.txt
    2 X 3 = 6 (True)
    3 X 3 = 11 (False)
    4 X 1 = 4 (True)

"""

# log.txt에 기록되어있는 모든 텍스트 출력
# 총 몇 문제였는지 출력
# 정답 개수 출력 ( 문자열.__contains__('찾을 문자열') )
# print( 'issell@naver.com'.__contains__('naver'))
# print( 'issell@naver.com'.__contains__('gmail'))
#
# print( '2 X 3 = 6 (True)'.__contains__('True'))