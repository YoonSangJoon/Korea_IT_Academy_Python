"""
    < for문 주의사항 >

"""
arr = [1, 2, 3, 4, 5]
i = 0
while i < 5:
    arr[i] = 10
    i += 1
print("while문 후 arr : {}".format(arr))
# 모두 10으로 변경됨

arr = [1, 2, 3, 4, 5]
for a in range(5):  # 0 <= a < 5
    arr[a] = 10

print("for (range 적용) 후 arr : {}".format(arr))
# 모두 10으로 변경됨

arr = [1, 2, 3, 4, 5]
for n in arr:
    n = 10
print("for (일반 for문) 후 arr : {}".format(arr))
# 변경 안됨
# 읽기 전용 (원소를 수정하지 않을 때 사용)
