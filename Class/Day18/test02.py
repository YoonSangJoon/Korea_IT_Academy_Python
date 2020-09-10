"""

    부모클래스 Book
        필드 : 책제목, 저자, 가격
        메서드 :
            print_info()  : 책제목, 저자, 가격 출력
            print_genre()  : pass
"""
class Book:
    def __init__(self, title="", writer="", price=0):
        self.title = title
        self.writer = writer
        self.price = price
        print("Book 오브젝트 생성!")

    def print_info(self):
        print("제목 : {}".format(self.title))
        print("저자 : {}".format(self.writer))
        print("가격 : {}".format(self.price))
        print("장르 : {}".format(self.print_genre()))
    def print_genre(self):
        pass
"""
    자식클래스 
     1) Novel
        print_genre() : '소설' 출력
"""
class Novel(Book):
    def print_genre(self):
        return "소설"

"""
     2) Textbook 
         print_genre() : '교과서' 출력
"""
class Textbook(Book):
    def print_genre(self):
        return "교과서"
"""

    
     3) Comic
        print_genre() : '만화' 출력
    
     .. 등등 여러 자식클래스 선언 + 오버라이드 해보기
     각 자식 클래스를 객체화 하여 print_info(), print_genre 출력
"""
class Comic(Book):
    def print_genre(self):
        return "만화"

"""
     메뉴) 
        1. 소설 추가
        2. 교과서 추가 
        3. 만화 도서 추가
        4. 모든 도서 보기
        5. 도서 검색 
            1) 장르로 검색 
            2) 제목으로 검색
        0. 종료
"""
books = []
while True:
    print("1. 소설 추가")
    print("2. 교과서 추가")
    print("3. 만화 도서 추가")
    print("4. 모든 도서 보기")
    print("5. 도서 검색")
    print("0. 종료")
    select = int(input("입력:"))
    if select == 0:
        print("프로그램 종료")
        break
    elif select == 1:
        n = Novel()
        n.title = input("소설 제목 :")
        n.writer = input("저자 :")
        n.price = int(input("가격 :"))
        books.append(n)  # 책 리스트에 새 소설 오브젝트 추가

    elif select == 2:
        t = Textbook()
        t.title = input("교과서 제목 :")
        t.writer = input("저자 :")
        t.price = int(input("가격 :"))
        books.append(t)  # 책 리스트에 새 소설 오브젝트 추가
    elif select == 3:
        c = Novel()
        c.title = input("만화책 제목 :")
        c.writer = input("저자 :")
        c.price = int(input("가격 :"))
        books.append(c)  # 책 리스트에 새 소설 오브젝트 추가
    elif select == 4:
        for b in books:
            b.print_info()
            b.print_genre()
    elif select == 5:
        print("1) 장르로 검색")
        print("2) 제목으로 검색")
        select2 = int(input("입력 :"))
        if select2 == 1:
            s = input("검색할 장르 :")
            for b in books:
                if s == b.print_genre():
                    b.print_info()
        elif select2 == 2:
            s = input("검색할 제목 :")
            for b in books:
                if s == b.title:
                    b.print_info()
    else:
        print("잘못된 입력")









