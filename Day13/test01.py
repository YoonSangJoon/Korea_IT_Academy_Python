# log.txt에 기록되어있는 모든 텍스트 출력
# 총 몇 문제였는지 출력
# log.txt : D:\071100_Python\Practice\Day12\log.txt

# 파일 내용 가져오기
#  log = open("log.txt", "r")  # 에러!
# --> '파일명'만 작성하면 이 소스파일(test01.py)이 들어있는 폴더가
#      기본 경로가 됨 (여기서는 Day13 폴더임)
# --> log.txt 는 Day12 에 있으므로 다음과 같이 쓰자
# --> 경로 구분은 '\\' 혹은 '/'

log = open("../Day12/log.txt", "r")
# 혹은 open("D:/071100_Python/Practice/Day12/log.txt", "r")

log_str = log.read()
print(log_str)

log.close()  # 한 번 읽어들인 문장은 (read()/readlines()/..) 다시 읽지 않음
             # 파일을 한 번 닫은 후 다시 열면 처음부터 다시 읽을 수 있음
log = open("../Day12/log.txt", "r")
# 총 몇 문제였니?
s_list = log.readlines()
print(s_list)
print("총 {} 문제".format(len(s_list)))

count = 0
for s in s_list:
    if s.__contains__("True"): count += 1
print("정답 수 {}개".format(count))