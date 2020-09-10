"""
    < Quiz >
    메뉴)
        1. 도서 추가 : 사용자에게 제목, 가격 입력 받고 Book 객체 생성 후 []에 추가 ( 딕셔너리 사용 가능 )
        2. 도서 검색 : 책 ID를 입력 해서 해당 책의 모든 정보 출력
        3. 모든 도서 보기 : 모든 도서들의 모든 정보 출력
        4. 현재 기록 저장하기 : 현재 모든 도서들의 모든 정보를 파일에 저장 (book.txt)
        5. 종료
    -----------------------
    Book 클래스 만들기
        - 필드 : 책 ID, 책 제목, 가격
        - 생성자 :
            Book()
            Book("책제목")
            Book("책제목", 가격)
           ==> ID는 1부터 시작하여 자동 부여 (1씩 증가)
        - 메서드 :
            get_info() : ID, 제목, 가격을 str으로 묶어서 return
                         (print 하는 것이 아님)
"""

class Book:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.price = 0
        print("Book 클래스 생성 완료")

    def get_info(self):
#        self.set_id()
        self.name = input("제목 입력 : ")
        self.price = int(input("가격 입력 : "))
        return 'ID : {} / 제목 : {} / 가격 : {}'.format(self.id, self.name, self.price)

#    def set_id(self):
#        self.id =



while True:
    menu = "1. 도서 등록 \n" \
         + "2. 도서 검색 \n" \
         + "3. 모든 도서 등록 \n" \
         + "4. 현재 기록 저장 \n" \
         + "5. 종료 \n입력 :"
    select = int(input(menu))
    if select ==1 :
        pass
    if select ==2 :
        pass
    if select ==3 :
        pass
    if select ==4 :
        pass
    if select ==5 :
        print("프로그램 종료")
        break
    else:
        print("잘못된 입력입니다.")