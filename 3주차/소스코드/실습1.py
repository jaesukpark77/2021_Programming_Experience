#1-1

f = open("c:/Temp/Text.txt",'w')
f.write("1 2 3 4 5 6 7 8 9 10")
f.close()

#1-2
f = open("c:/Temp/Text.txt", "w")
for i in range(0, 101, 2):
    f.writelines(str(i) + " ")
f.close()
