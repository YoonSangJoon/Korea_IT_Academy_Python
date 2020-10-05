class MyError(Exception):  # 나만의 예외 클래스 만들기
    def __str__(self):     # 에러가 나면 이 부분이 메시지로 뜸
        return '오답'


from random import randint


def gugudan_quiz():
    n1 = randint(1, 9)
    n2 = randint(1, 9)
    answer = int(input('{} X {} = '.format(n1, n2)))
    if answer == n1*n2:
        print("정답!!")
    else:
        raise MyError()   # MyError 를 발생시킴

if __name__ == '__main__':
    try:
        gugudan_quiz()
    except MyError as my:
        print(my)
        print("MyError!! 아마도 오답이었나봄")