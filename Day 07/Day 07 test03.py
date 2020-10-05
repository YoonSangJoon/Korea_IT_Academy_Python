# Quiz 1
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   #  또는 arr = [0] * 10

# arr에 1 ~ 100 까지의 랜덤 수 10개를 저장할 것.
# 중복 원소 상관 없음.
import random
i = 0
while i < 10:
    arr[i] = random.randint(1,100)
    i += 1

print(arr)

print()

# arr의 원소 중 짝수만 출력 (for문 사용)
print("짝수 : ", end="")  # 마지막에 '엔터' 대신 ""
for e in arr:
    if e % 2 == 0:
        print(e, end=" ")  # 마지막에 '엔터' 대신 공백 1칸

print()

# 전체 arr 원소의 평균 출력 (for문 사용)
sum = 0
for e in arr:
    sum += e
print("|n전체 평균 : {}".format( sum / 10))
print()

# input()으로 정수 1개 입력 받고 arr에 있는지 없는지 출력 (반복문 없이)
# a = int(input("정수a : "))
# print(a in arr)   ->   이거 아님 ㅜ

user = int(input("검색할 원소 : "))
if user in arr:
    print("있습니다~ {}번에 있습니다~".format(arr.index(user)))
else:
    print("없습니다~")

# 참고 : 리스트명.index( 검색할 원소 )
# --> 원소의 인덱스가 몇 번이니? (없는 원소일 경우 에러 발생 !)
print()

# input()으로 정수 1개를 입력 받고 (3을 입력했다고 하면)
# 해당 인덱스의 원소 출력 (3번 원소를 출력할 것)
#b = int(input("정수b : "))
#print(arr[b])  ->  이거 아님 ㅜ

user = int(input("인덱스 : "))
if user < -10 or user >= 10 :
    print("잘못된 인덱스입니다.")
else:
    print("arr[{}] : {}".format(user, arr[b]))

print()

# 최댓값, 최솟값 출력 (for문 사용)
max = arr[0]  # 처음에는 최대값, 최소값을 모르니까 0번 인덱스로 저장
min = arr[0]
for e in arr:  # 그 후 for문으로 계속 반복해가며 찾아보기
    if max < e:
        max = e
    if min > e:
        min = e
print("최댓값 : {} 최솟값 : {}".format(max, min))


"""
    [0] [1] [2] [3] [4] ==> 인덱스
    10  20  30  40  50  ==> 원소
        ** 인덱스 통해 접근 : 인덱싱 (indexing)
"""