from glob import escape
import tkinter
from tkinter import colorchooser

win = tkinter.Tk()
win.resizable(False, False)

c = tkinter.Canvas(win, height=500, width=700, highlightthickness=0,borderwidth=0)
c.pack()

mode = "triangle"
x = 0
y = 0
xc1 = 0
xc2 = 0
yc1 = 0
yc2 = 0
clickc = 0
roundto = 50

exportlines = []

fillcolor = "#FFFFFF"
linecolor = "#000000"
isfilltransparent = True

def callback(e):
    global x,y
    
    x = e.x
    y = e.y
    #print("Pointer is currently at %d, %d" %(x,y))

def click(e):
    global xc1,xc2,yc1,yc2,clickc,roundto, exportlines
    
    clickc += 1
    print("Clicked")
    if clickc == 1:
        xc1 = round(x/roundto)*roundto
        yc1 = round(y/roundto)*roundto
    if clickc == 2:
        xc2 = round(x/roundto)*roundto
        yc2 = round(y/roundto)*roundto
        
        if mode=="triangle" or mode=="ngon":
            
            escape
        else:
            clickc = 0

        if mode == "rectangle":
            print(fillcolor, isfilltransparent)
            if isfilltransparent == True:
                c.create_rectangle(xc1,yc1,xc2,yc2, fill="", outline=linecolor)
                exportlines.append("c.create_rectangle("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+",fill='', outline='"+linecolor+"')")
            elif isfilltransparent == False:
                c.create_rectangle(xc1,yc1,xc2,yc2, fill=fillcolor, outline=linecolor)
                exportlines.append("c.create_rectangle("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+",fill='"+fillcolor+"', outline='"+linecolor+"')")
        if mode == "oval":
            if isfilltransparent == True:
                c.create_oval(xc1,yc1,xc2,yc2, fill="", outline=linecolor)
                exportlines.append("c.create_oval("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+",fill='', outline='"+linecolor+"')")
            elif isfilltransparent == False:
                c.create_oval(xc1,yc1,xc2,yc2, fill=fillcolor, outline=linecolor)
                exportlines.append("c.create_oval("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+",fill='"+fillcolor+"', outline='"+linecolor+"')")
        if mode == "line":
            c.create_line(xc1,yc1,xc2,yc2, fill=linecolor)
            exportlines.append("c.create_line("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+", fill='"+linecolor+"')")
        print(exportlines)
    if clickc == 3:
        if mode == "triangle":
            clickc=0
            xc3 = round(x/roundto)*roundto
            yc3 = round(y/roundto)*roundto
            c.create_polygon(xc1,yc1,xc2,yc2,xc3,yc3, fill=fillcolor, outline=linecolor)
            exportlines.append("c.create_polygon("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+","+str(xc3)+","+str(yc3)+", fill='"+fillcolor+"',outline='"+linecolor+"')")
                          
    
win.bind('<Motion>',callback)
win.bind("<Button-1>", click)


def moderectangle():
    global mode
    
    mode = "rectangle"
    print(mode)
def modeoval():
    global mode
    
    mode = "oval"
    print(mode)
def modeline():
    global mode
    
    mode = "line"
    print(mode)
def modetriangle():
    global mode
    
    mode = "triangle"
    print(mode)


def opencolorpick():
    global fillcolor,colpickbut
    
    fillcolor = colorchooser.askcolor(title ="Choose Fill Color")[1]
    colpickbut.configure(bg=fillcolor)
    print(fillcolor)
    print(type(fillcolor))
def opencolorpick2():
    global linecolor,colpickbut2
    
    linecolor = colorchooser.askcolor(title ="Choose Line Color")[1]
    colpickbut2.configure(bg=linecolor)
    print(linecolor)
def togglefilltransparent():
    global isfilltransparent,filltransparentbut
    
    if isfilltransparent == True:
        isfilltransparent = False
        filltransparentbut.config(text="Toggle Fill Transparent (False)")
    else:
        isfilltransparent = True
        filltransparentbut.config(text="Toggle Fill Transparent (True)")



def generate():
    print('generating')
    fp = open('tkinter_drawing.py', 'w')
    fp.write('import tkinter')
    fp.write('\nc = tkinter.Canvas(height=500, width=700)')
    fp.write('\nc.pack()')

    for x in exportlines:
        print(x)
        fp.write('\n'+x)

    fp.close()
    print('generated')


#generate()

def deleteall():
    c.delete("all")

toolwindow = tkinter.Toplevel(win)
toolwindow.geometry("300x250")
toolwindow.title("Toolbox")
toolwindow.resizable(False, False)

#lbl = tkinter.Label(toolwindow, text="I am in this toolwindow thing right").pack()

rectanglebutton = tkinter.Button(toolwindow, text="Rectangle", command=moderectangle).pack()
ovalbutton = tkinter.Button(toolwindow, text="Oval", command=modeoval).pack()
linebutton = tkinter.Button(toolwindow, text="Line (uses OUTLINE color not FILL COLOR", command=modeline).pack()
linebutton = tkinter.Button(toolwindow, text="Triangle", command=modetriangle).pack()

colpickbut = tkinter.Button(toolwindow, text="Fill Color", command=opencolorpick, bg=fillcolor)
colpickbut.pack()

filltransparentbut = tkinter.Button(toolwindow, text="Toggle Fill Transparent (True)", command=togglefilltransparent)
filltransparentbut.pack()

colpickbut2 = tkinter.Button(toolwindow, text="Line Color", command=opencolorpick2, bg=linecolor)
colpickbut2.pack()

exportbut = tkinter.Button(toolwindow, text="export to .py", command=generate).pack()

warnlabel = tkinter.Label(toolwindow, text="WARNING: Will delete everything", fg="red").pack()
deletebut = tkinter.Button(toolwindow, text="CLEAR CANVAS", command=deleteall, bg="red").pack()

win.mainloop()
toolwindow.mainloop()
