# 파일 입출력


f = open("aa.txt", 'w')
# aa.txt 을 열어라!
# w : write mode (쓰기모드)
# r : read mode
# rw : read, write (쓰기, 읽기 모두 가능)


f.write("메롱메롱\n")
f.write("hihi\n")
f.close()

print("파일 저장 완료!")

# 사용자에게 이름 5개를 입력받고
# user_name.txt 파일에 저장



f = open("user_name.txt", "a")
# a : append mode ( 추가 모드 )
# w : write mode ( 처음부터 다시 씀 )

for i in range(1, 6):
    name = input("{} 번째 이름 입력 : ".format(i))
    f.write(name + "\n")

f.close()








