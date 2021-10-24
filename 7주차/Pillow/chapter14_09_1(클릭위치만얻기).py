import tkinter

root = tkinter.Tk()
cv = tkinter.Canvas(root, width=500, height=300)
def click(event):                              # 클릭 이벤트
    print("클릭 위치 :", event.x, event.y)     # event.x는 클릭이벤트시의 x좌표

cv.bind("<Button-1>", click)                   #<Button-1>은 마우스 왼쪽클릭      
cv.pack()

root.mainloop()
