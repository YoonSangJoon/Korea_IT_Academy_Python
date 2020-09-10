
a = range(1, 11)  # 1 <= ? < 11 에 해당하는 모든 정수
print(a)

for n in a:  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print(n)

print("")
print()

for n in range(20, 41, 3):
    print(n)

"""
    pass : 건너뛰어라 
    (if, 반복문 모두에 적용) 
"""

# 4의 배수를 제외한 1 ~ 20까지의 수 출력
for num in range(1, 21):
    if(num % 4 == 0):
        pass
    else:
        print(num)