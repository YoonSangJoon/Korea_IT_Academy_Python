# input() 은 입력 받은 데이터를 모두 str형으로 가져오기 때문에
# 올바른 자료형으로 형변환을 해야 한다.

# a = input("정수:")
# print(int(a))
a = int(input("정수:"))  # 입력된 값을 int형으로 변환 --> a 변수에 저장
print(a)  # a는 int형 데이터가 있음

# " 와 '의 차이? 없음! --> 둘 다 문자열 표시에 사용한다.
print("나는 '피카츄'라고 해요.")
print('피카츄가 "피카피카"라고 말했다.')
print("""'피카츄'가 "피카피카"라고 말했다.""")

print("ㅋㅋㅋㅋ"
      "ㅎㅎㅎㅎ"
      "메롱메롱~")
print("""
    ㅋㅋㅋㅋ
    ㅎㅎㅎㅎ
    메롱메롱~
""")




