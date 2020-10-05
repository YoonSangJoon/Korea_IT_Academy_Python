f1 = open("user_name.txt", 'r')
# r : read mode
#  --> write() 는 못함!

# s = f1.read()  # 전체
# s = f1.read(4)   # 맨 앞의 4글자만
s = f1.readline()  # 1줄만
s2 = f1.readline()  # 1줄만
print(s)
print(s2)

f1.close()

f1 = open("user_name.txt", 'r')
s3 = f1.readlines()
print(s3)








