import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
cv = tkinter.Canvas(root, width=500, height=300)
def click(event):                                #클릭이벤트 (매개변수 : 이벤트 정보)
    print("클릭 위치 :", event.x, event.y)       #이벤트 내 x,y좌표 
    r, g, b = img.getpixel((event.x, event.y))   #해당좌표 픽셀 정보
    print("R:%d  G:%d  B:%d"%(r,g,b))

cv.bind("<Button-1>", click)                     #<Button-1> 이벤트 바인딩
cv.pack()

img = Image.open('baby.jpg')
img_tk = ImageTk.PhotoImage(img)                 #이미지 형식 tkinter
cv.create_image(250,250, image=img_tk)           #캔버스에 이미지 출력

root.mainloop()
