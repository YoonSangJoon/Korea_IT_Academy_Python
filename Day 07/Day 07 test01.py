"""

    <list>
    - 데이터를 저장할 수 있는 메모리
    - []
    - 인덱스 : 각 칸의 번호
    - [0]번부터 시작한다.
    - 거꾸로도 가능.
    - 원소 (Element) : 리스트에 들어있는 데이터

"""

lst = [10, 20, 30, 40, 50]  # [] 사용으로 여러개 데이터 넣을 수 있음.
#      0 , 1 , 2 , 3 , 4  번 데이터
print(lst)

print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])

lst[2] = 300
print(lst)

print(lst[-1])
print(lst[-2])
print(lst[-3])
print(lst[-4])
print(lst[-5])

lst2 = ["홍길동", "피카츄", ["푸린", 5], 3.14, lst]
print(lst2)

print(lst2[0])
print(lst2[1])
print(lst2[2])
print(lst2[3])
print(lst2[4])

lst2[2][1] = 50   #   lst2의 3번째 원소의 2번째 값을 50으로
print(lst2)

lst2[4][2] = "ㅋㅋㅋㅋㅋ"
print(lst2)   #   lst2의 5번째 원소 (lst) 의 3번째 값 (300) 을 'ㅋㅋㅋㅋㅋ' 으로

print(lst)   #  [10, 20, 'ㅋㅋㅋㅋㅋ', 40, 50]  # lst2 에서 lst 값을 바꾸면 원래의 lst 값도 바뀜.

print("lst의 위치 : {}".format(id(lst)))  # same
print("lst2의 위치 : {}".format(id(lst2)))
print("lst2[4] (lst가 있는 곳) : {}".format(id(lst2[4])))  # same
# id(대상) ==> 대상의 위치 (메모리 주소)

# list 는 해당 리스트의 메모리 주소로 처리됨
# ==> list 이름 == list의 시작 주소
a = [1, 2, 3, 4]
#b = a;  # 얕은 복사
b = a.copy()  # 깊은 복사

b[2] = 1000
print(a)  #  [1, 2, 1000, 4]  # b = a;
print(b)  #  [1, 2, 1000, 4]

print(a)  #  [1, 2, 3, 4]  # b = a.copy()
print(b)  #  [1, 2, 1000, 4]