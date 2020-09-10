"""

    < Up & Down 게임 >
    1. 난수 생성 ( 1 ~ 100 )
    2. 사용자는 숫자를 맞춰야 함
       정답 > 사용자입력 : Up 출력
       정답 < 사용자입력 : Down 출력
       정답 == 사용자입력 : Correct! 출력 (반복 종료)
    3. 총 몇 회가 입력되었는 지 출력
        5회 이하 : WIN!
        아니면 : LOSE..
"""
import random

com = random.randint(1, 100)
cnt = 0
while True:
    cnt += 1
    player = int(input("1 ~ 100 : "))
    if com > player:
        print("Up")
    elif com < player:
        print("Down")
    elif com == player:
        print("Correct!")
        break

print("총 {} 회".format(cnt))
if cnt <= 5:
    print("WIN")
else:
    print("LOSE")
















