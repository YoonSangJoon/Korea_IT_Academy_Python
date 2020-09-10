"""

    < 학생 관리 프로그램 >
    1. 학번, 이름, 학년, 반, 번호, 점수, 등급 으로 구성된 학생 정보 1개 만들기
        (딕셔너리 사용)
        ** 학번 : 학년/반/번호 조합
                    3학년 12반 7번 : 31207
    2. 5명에 대한 정보 만들기
        (리스트 + 딕셔너리 사용)
        for문 사용하여 input()으로 입력도 각각 받고,
        모든 정보도 출력
    3. 메뉴 만들기 (최대 10명까지만 저장 가능)
      1) 학생 등록 -> 학년/반/번호/이름/점수 5개 입력 받음 (학번/등급은 자동 계산)
      2) 모든 학생 보기 -> 모든 학생들의 모든 정보
      3) 학생 검색 (학번으로 검색) -> 해당 학번을 가진 학생의 모든 정보.
                                     없는 학번이면 "미등록 학생"을 출력
      4) 학년 별 1등 학생 보기 -> 학년을 입력 받고 (1 ~ 6) 해당 학년의 학생 중 점수 1등 학생의
                                 이름과 점수 출력
      5) 종료
"""

""" 문제 1 답
grade = 3
cls = 7
num = 24
st_num = str(grade) + '{:02}'.format(cls) + '{:02}'.format(num)    # 30724
print(st_num)

st = {}
st['name'] = input("학생 이름 : ")
st['grade'] = int(input("학년 : "))
st['class'] = int(input("반 : "))
st['num'] = int(input("번호 : "))
st['st_num'] = str(st['grade']) \
               + '{:02}'.format(st['class']) \
               + '{:02}'.format(st['num'])
st['score'] = float(input("점수 : "))
if st['score'] >= 90:
    st['rating'] = 'A'
elif st['score'] >= 80:
    st['rating'] = 'B'
elif st['score'] >= 70:
    st['rating'] = 'C'
elif st['score'] >= 60:
    st['rating'] = 'D'
else:
    st['rating'] = 'F'
print(st)
"""


""" 문제 2 답 
students = [{}, {}, {}, {}, {}]

for i in range(5):  # i : 0 ~ 4
    s = {}

    # 이름
    s["name"] = input("학생 이름:")

    # 학년
    s['grade'] = input("학년 : ")

    # 반
    s['class'] = int(input("반 : "))

    # 번호
    s['num'] = int(input("번호 : "))

    # 학번 만들기
    s['st_num'] = s['grade'] + '{:02}'.format(s['class']) + '{:02}'.format(s['num'])

    # 점수
    score = float(input("점수 : "))

    # 등급
    r = 'F'
    if score >= 90:
        r = 'A'
    elif score >= 80:
        r = 'B'
    elif score >= 70:
        r = 'C'
    elif score >= 60:
        r = 'D'
    s['score'] = score
    s['rating'] = r

    # 딕셔너리 s(딕셔너리의 주소)를 students 리스트에 저장
    students[i] = s

for e in students:
    print(e)
"""


students = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
last_idx = 0  # 현재 등록된 학생 수 (= 빈 칸들 중 가장 앞 칸의 인덱스)
while True:
    print("1. 학생 등록")
    print("2. 모든 학생 보기")
    print("3. 학생 검색")
    print("4. 1등 보기")
    print("5. 종료")
    select = int(input("선택:"))
    if select == 1:
        if last_idx < 10:
            s = {}

            # 이름
            s["name"] = input("학생 이름:")

            # 학년
            s['grade'] = input("학년 : ")

            # 반
            s['class'] = int(input("반 : "))

            # 번호
            s['num'] = int(input("번호 : "))

            # 학번 만들기
            s['st_num'] = s['grade'] + '{:02}'.format(s['class']) + '{:02}'.format(s['num'])

            # 점수
            score = float(input("점수 : "))

            # 등급
            r = 'F'
            if score >= 90:
                r = 'A'
            elif score >= 80:
                r = 'B'
            elif score >= 70:
                r = 'C'
            elif score >= 60:
                r = 'D'
            s['score'] = score
            s['rating'] = r

            # 딕셔너리 s(딕셔너리의 주소)를 students 리스트에 저장
            students[last_idx] = s

            # 학생 수 1증가
            last_idx += 1
        else:
            print("학생 수 초과")
    elif select == 2:
        for i in range(last_idx):  # e.g. last_idx->3이면 range()-->0,1,2
            print("{}/{}/{}/{}".format(students[i]['st_num'],
                                       students[i]['name'],
                                       students[i]['score'],
                                       students[i]['rating']))  # 학번/이름/점수/등급
    elif select == 3:
        # 학번을 입력 받는다.
        st_num = input("학번 : ")

        # [0] ~ [last_idx] 의 학생 중 학번이 일치하는 학생을 찾는다.
        check = False  # 상태 체크용 변수 (검색 성공 시 True)

        for s in range(last_idx):

            # 있으면 학생의 정보를 출력한다.
            if students[s]['st_num'] == st_num:
                print(students[s])
                check = True

        # 없으면 "미등록 학생"을 출력한다.
        if not check:   # check == False
            print("미등록 학생")

    elif select == 4:
        # 학년 입력 받는다.
        grade = input("학년 : ")

        # [0] ~ [lst_idx]의 학생 중, 해당 학년에 부합하는 원소 찾기
        max_student = {}

        for i in range(last_idx):

            # 찾았다면 현재 최대 점수와 비교한다
            if students[i]['grade'] == grade :
                # 최초 비교거나, 더 큰 점수를 발견하면 이 학생을 1등 학생으로 기록한다.
                if max_student == {} or max_student['score'] < students[i]['score']:
                    max_student = students[i]

        # 탐색 종료 후, 1등 학생의 점수, 이름을 출력한다.
        print("1등 학생 : {} / {}점 ".format(max_student['name'], max_student['score']))

    elif select == 5:
        print("프로그램을 종료합니다.")
        exit(0)  # 프로그램 종료 (break 도 논리적으로 같은 결과)