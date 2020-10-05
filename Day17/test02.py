"""

    < 예외 처리 (exception) >
    -> 예외 : 런타임 에러
        (실행 중에 발생한 에러!)

    -> 예외 처리 : try문
        형식:
            try:
                에러가 발생할 가능성이 있는 코드
            except XXError:
                XXError가 발생했을 때 실행할 코드



try:
    age = int(input("나이를 입력하세요 : "))
    print("당신의 나이는 {}살이군요~!".format(age))

except ValueError:
    print("숫자를 입력하세요.")

"""


lst = [10, 100, 30, 20, 50, 66, 1001, 55]
# 사용자에게 인덱스를 입력 받아 해당 원소 출력
# 잘못된 인덱스인 경우 except 로 "잘못된 인덱스입니다."

try:
    i = int(input('인덱스 :'))
    print('lst[{}] : {}'.format(i, lst[i]))
# 방법1
except IndexError as a:
    print(a)
    print('잘못된 인덱스입니다.')

except ValueError:
    print('정수를 입력하셔야합니다.')

# 방법2
# except [IndexError, ValueError]:  # 두 에러에 대하여 같은 처리 하려면
#     print('잘못된 입력입니다.')

# 방법3
# except Exception:  # 모든 에러에 대하여
#     print("예기치 못한 에러 발생")






