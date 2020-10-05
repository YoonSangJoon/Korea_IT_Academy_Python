# 랜덤 수 생성하기

import random

# 1 ~ 10 중 랜덤하게 1개 뽑기
n = random.randint(1, 10)  # 1 <= ? <= 10  # 1 이상 10 이하의 정수(int)를 리턴한다.
print(n)

# 0 <= n < 1 실수 출력  # random() 함수는 0 이상 1 미만의 숫자 중에서 아무 숫자나 하나 뽑아서 돌려주는 일.
n = random.random()
print(n)

# 30% 의 확률로 승리!
if random.random() < 0.3:
    print("승리!")
else:
    print("패배..")




