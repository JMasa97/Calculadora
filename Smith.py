from tkinter import *
def motion(event):
    x, y = event.x, event.y
    x=x/402
    y=y/398
    print('{}, {}'.format(x, y))

root = Tk()
root.bind('<Button-1>', motion)
canvas = Canvas(root, width=650, height=700)
canvas.pack()
img = PhotoImage(file='SmithChart-3.png') #transparent image
background = Label(image = img)
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
root.mainloop()