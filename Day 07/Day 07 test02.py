nums = [400, 1, 656, 235, 6564, 232]

# 이 배열에 656 이 들어있니?
print(656 in nums)  # True / False

print()
# 반복문으로 원소 출력하기

# 방법1. while문
i = 0
while i < 6:   # i는 0부터 5까지만
    print(nums[i])
    i += 1   # i는 1씩 커질 것이다.

print()

# 방법2. for문
for n in nums:
    print(n)