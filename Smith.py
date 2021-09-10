from tkinter import *
def motion(event):
    canvas.create_rectangle(150,680,450,700,fill='#fff',disabledoutline='#fff')
    x=event.x/402
    y=event.y/398
    canvas.create_text(300,690,text=f'x={x} y={y}')
    canvas.create_line(event.x,event.y+293,event.x,event.y-223,width=2)
    

root = Tk()
root.bind('<Button-1>', motion)
canvas = Canvas(root, width=650, height=700)
canvas.pack()
img = PhotoImage(file='SmithChart-1.png') #transparent image
canvas.create_image(325,345,image=img)
root.mainloop()