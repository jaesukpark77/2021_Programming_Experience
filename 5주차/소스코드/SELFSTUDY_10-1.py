from tkinter import*
window = Tk()

photo = PhotoImage(file='../gif/cat.gif')
photo2 = PhotoImage(file='../gif/cat2.gif')

label1 = Label(window, image = photo)
label2 = Label(window, image = photo2)

label1.pack(side=LEFT);
label2.pack(side=LEFT);

window.mainloop()



