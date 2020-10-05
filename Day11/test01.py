# 리스트 [] 관련 함수(명령어)

a = [10, 20, 30]

# a[3] = 40 # 에러! 현재 a는 3칸까지밖에 없음!

a.append(40) # 한 칸 새로 추가 후 40을 저장
print(a)

a.append([1, 2])
print(a)

b = [5, 4, 1, 6, 7, 2, 4, 3]
b.sort() # 오름차순으로 정렬
print(b)

c = ['a', 'g', 'w', 'y', 'b', 'd']
c.sort()
print(c)
# 주의! sort() 는 리스트에 원소들이 모두 같은 자료형이어야 함

c.reverse()  # 거꾸로 배치
print(c)

d = ['a', 'b', 'c', 10, 20, 30]
print(d.index('b'))  # 1
print(d.index(20))   # 4
# 리스트.index( 인덱스가 궁금한 원소 ) ==> 해당 원소의 인덱스
if 200 in d:
    print(d.index(200))
else:
    print("200은 없다")


print("삽입 전 d : {}".format(d))
d.insert(2, 1000)
# 리스트.insert(인덱스, 새 원소)
print("삽입 후 d : {}".format(d))

e = [10, 20, 30, 10, 200, 40]
e.remove(10)
# 리스트.remove(삭제할 원소) ==> 중복 원소가 있다면 1개만 삭제
print(e)

num = e.pop(2)
# 리스트.pop() ==> 가장 마지막 데이터를 우리에게 주고, 리스트에서는 삭제
# 리스트.pop(인덱스) ==> 해당 인덱스의 원소를        "
print('pop 된 데이터 : {}'.format(num))
print(e)

f = [10, 20, 30, 10, 20]
num = f.count(10)  # 10이 몇 개 있니?
print(num)  # 2

# f.extend([1, 2])
f += [1, 2]
print(f)

f.clear() # 모든 원소 삭제
print(f)

# 참고) 리스트(튜플,딕셔너리)의 원소 개수 : len( 개수 셀 대상 )
print(len(f))  # 0

g = {'a' : 10, 'b':20 , 'c':30}
print(len(g))  # 3

h = (4,5,3,123.54, 2342.123, 23)  # 6
print(len(h))







