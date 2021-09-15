from tkinter import *
def motion(event):
    canvas.delete("all")
    canvas.create_image(325,345,image=img)
    canvas.create_rectangle(150,680,450,700,fill='#fff',disabledoutline='#fff')
    x=event.x/402
    y=event.y/398
    canvas.create_text(300,690,text=f'x={x} y={y}')
    canvas.create_oval(event.x+3,event.y+3,event.x-3,event.y-3)
    if  y>0.7 and y<0.8:
        canvas.create_line(event.x,event.y+460,event.x,event.y-270)
    elif  y>0.8 and y<0.9:
        canvas.create_line(event.x,event.y+280,event.x,event.y-300)
    elif  y>0.6 and y<0.7:
        canvas.create_line(event.x,event.y+410,event.x,event.y-300)    
    elif  y>0.5 and y<0.6:
        canvas.create_line(event.x,event.y+430,event.x,event.y-300)
    elif  y>0.4 and y<0.5:
        canvas.create_line(event.x,event.y+500,event.x,event.y-300)
    elif  y>0.3 and y<0.4:
        canvas.create_line(event.x,event.y+500,event.x,event.y-300)
    elif  y>0.9 and y<1.0:
        canvas.create_line(event.x,event.y+260,event.x,event.y-300)    
    elif  y>1.0 and y<1.1:
        canvas.create_line(event.x,event.y+220,event.x,event.y-300)
    elif  y>1.1 and y<1.2:
        canvas.create_line(event.x,event.y+200,event.x,event.y-300)
    elif  y>1.2 and y<1.32:
        canvas.create_line(event.x,event.y+125,event.x,event.y-410)
root = Tk()
root.bind('<Button-1>', motion)
canvas = Canvas(root, width=650, height=700)
canvas.pack()
img = PhotoImage(file='SmithChart-1.png') #transparent image
canvas.create_image(325,345,image=img)
root.mainloop()