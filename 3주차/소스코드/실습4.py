nation = ["한국", "미국", "일본", "중국", "러시아", "베트남"]
a = " "
while a:
    if a == "q":
        break

    a = input("나라 이름을 입력하세요 : ")
    try:
        print(nation.index(a))
    except ValueError as e:
        f = open("c:/temp/log.txt", "a")
        f.write("%s\n"%a)
        f.close()
        print("%s 국가는 리스트에 존재하지 않습니다. 로그 기록"%e)
