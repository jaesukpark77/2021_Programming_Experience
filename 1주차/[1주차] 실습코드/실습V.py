print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.')
print('1) 햄버거')
print('2) 치킨')
print('3) 피자')
menu = input('1에서 3까지의 메뉴를 선택하세요 : ')
while True:
    if menu == '1':
        print('햄버거를 선택하였습니다.')
        break
    elif menu == '2':
        print('치킨를 선택하였습니다.')
        break
    elif menu == '3':
        print('피자를 선택하였습니다.')
        break
    else:
        menu = input('메뉴를 다시 입력하세요: ')
