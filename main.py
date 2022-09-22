import tkinter

win = tkinter.Tk()

c = tkinter.Canvas(win, height=500, width=700)
c.pack()

mode = "rectangle"
x = 0
y = 0
xc1 = 0
xc2 = 0
yc1 = 0
yc2 = 0
clickc = 0
roundto = 50

def callback(e):
    global x,y
    
    x = e.x
    y = e.y
    print("Pointer is currently at %d, %d" %(x,y))

def click(e):
    global xc1,xc2,yc1,yc2,clickc,roundto
    
    clickc += 1
    print("Clicked")
    if clickc == 1:
        xc1 = round(x/roundto)*roundto
        yc1 = round(y/roundto)*roundto
    if clickc == 2:
        xc2 = round(x/roundto)*roundto
        yc2 = round(y/roundto)*roundto
        
        clickc = 0

        if mode == "rectangle":
            c.create_rectangle(xc1,yc1,xc2,yc2)
        

    
win.bind('<Motion>',callback)
win.bind("<Button-1>", click)
win.mainloop()
