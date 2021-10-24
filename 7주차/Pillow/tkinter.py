from PIL import Image, ImageTk
import tkinter
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=1200, height=867)
canvas.pack()
img = Image.open('c:/temp/baby.jpg')
img_tk = ImageTk.PhotoImage(img)
canvas.create_image(600, 400, image=img_tk)
