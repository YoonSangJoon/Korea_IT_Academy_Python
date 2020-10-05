"""

    break : loop 종료하라!

    ** 줄 정렬 : ctrl + alt + L
"""
price = 0
while True:
    print("------ 메 뉴 ------")
    print("1. 짜장면 주문하기(3000원)")
    print("2. 짬뽕 주문하기(4000원)")
    print("3. 탕수육 주문하기(10000원)")
    print("4. 결제하기")
    print("5. 종료하기")
    menu = int(input("선택 : "))
    if menu == 1:
        price += 3000  # price = 3000
        print("짜장면 선택! 현재 결제예상액 : {}".format(price))
    elif menu == 2:
        price += 4000
        print("짬뽕 선택! 현재 결제예상액 : {}".format(price))
    elif menu == 3:
        price += 10000
        print("탕수육 선택! 현재 결제예상액 : {}".format(price))
    elif menu == 4:
        print("{}원 결제되었습니다. 또 오세요~~".format(price))
        price += 0
    elif menu == 5:
        print("프로그램을 종료합니다.")
        break  # 반복 종료!)
    else:
        print("잘못된 입력입니다.")
print("----------- 끝 -----------")
