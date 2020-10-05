try:
    n1 = int(input("정수1:"))
    n2 = int(input("정수2:"))
    print("{} / {} = {}".format(n1, n2, n1/n2))
except ValueError:
    print('정수를 입력하셔야 합니다.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
finally:  # try가 정상적으로 끝났든,
          # 중간에 except가 실행되었든 상관없이
          # 무조건 마지막에 실행할 내용 (자원 해제할 때 사용)
    print("프로그램을 종료합니다.")


# finally 써야하는 예
try:
    f = open("aa.txt", 'w')
    # .....
    # .....  # 에러!
    # .....
    # .....

except Exception:
    # 에러가 났네..
    pass
finally:
    f.close()  # 중간 에러가 터져도 실행해야하기 때문






