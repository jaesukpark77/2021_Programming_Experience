inFp = None    # 입력 파일
inList = ""        # 읽어온 문자열

inFp = open("C:/Temp/data1.txt", "r", encoding="UTF8")

inList = inFp.readlines()
print(inList)

inFp.close()
