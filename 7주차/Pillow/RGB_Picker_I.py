import tkinter

root = tkinter.Tk()
cv = tkinter.Canvas(root, width=500, height=300)
def click(event):                              
    print("클릭 위치 :", event.x, event.y)     

cv.bind("<Button-1>", click)                      
cv.pack()

root.mainloop()
