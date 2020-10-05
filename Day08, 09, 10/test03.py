"""

    대용량 자료형
    1. [] : 리스트

    2. () : 튜플 (tuple)
        -> 수정 불가능한 리스트
        -> 한번 태어나면 수정될 수 없음
        -> 함수의 return 값이 여러 개일 때 튜플로 묶어서 return
            (나중에 보자..)
    3. {} : 딕셔너리 (dictionary)
        -> { 키1:값1 , 키2:값2 , 키3:값3 ,   ,   }
        -> 'key'를 통해 'value'를 찾기 위함
           (검색이 편함)
"""
t = (1, 2, 3, 4, 5)
print(t)
# t[2] = 30
print(t)

t = 1, 2, 3, 4  # 이 때도 tuple형태로 (1, 2, 3, 4)가 묶여서 t에 저장
print(t)
print(t[0])
print(t[1])
print(t[2])

#####################################################
info = {
    "name": "피카츄",
    "level": 10,
    "hp": 1000,
    "skill": "백만볼트 공격"
}
print(info)

info["name"] = "라이츄"
info["level"] += 1
info["hp"] = info['level'] * 100
info['skill'] = '천만볼트 공격'
info['master'] = '지우'
print(info)
# 이미 존재하는 '키'라면 ==> value 수정
# 새로운 '키'라면 ==> 새 원소로 추가

scores = {
    10 : 90, 21 : 88, 3 : 70
}
# 키, 값 모두 자료형 상관없지만..
# 보편적으로 키의 경우 str, int를 주로 사용한다.
print(scores[10])
print(scores[21])
print(scores[3])


d = { "a":[1, 2, 3, 4] , "b":[10, 20, 30], "c":[100,200]}

# 20 출력
print(d['b'][1])





