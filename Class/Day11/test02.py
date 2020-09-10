# 딕셔너리 주요 함수

# .keys() : key들만 리스트로 만들어서 줘
# dict_keys 자료형 : 리스트와 동일. 단, append,insert, remove 등의 원소 변경 함수가 없음
a = { "name":"홍길동", 'age':10, 'phone':'010-1111-2222'}
k = a.keys()
print(k)
print("k의 자료형 : {}".format(type(k)) )

for key in k:
    print(a[key])

print(a.values())  # value들만

pairs = a.items()  # dict_items([('name', '홍길동'), ('age', 10), ('phone', '010-1111-2222')])
pairs2 = list(pairs)

print(pairs)
print(pairs2[0])
print(pairs2[1])
print(pairs2[2])

# list( ) ==> 리스트로 만들기
t = 1, 2, 3, 4, 5   # t = ( 1, 2, 3, 4, 5 )
x = list(t)         # list(t) = [ 1, 2, 3, 4, 5 ]
print(x)












