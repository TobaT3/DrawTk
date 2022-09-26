from glob import escape
import tkinter
from tkinter import HORIZONTAL, colorchooser
from PIL import ImageGrab


win = tkinter.Tk()
win.resizable(False, False)
win.title("TkPaint Canvas")

c = tkinter.Canvas(win, height=500, width=700, highlightthickness=0,borderwidth=0)
c.pack()

mode = "rectangle"
x = 0
y = 0
xc1 = 0
xc2 = 0
xc3 = 0
yc1 = 0
yc2 = 0
yc3 = 0
clickc = 0
roundto = 50
ids = 0
totids = 0
linec = 0
linethicc = 1
getfirstpoint = True
drawingngon = False

clickcs = []

exportlines = []

fillcolor = "#FFFFFF"
linecolor = "#000000"
isfilltransparent = True

def callback(e):
    global x,y, poslabel, snapp, roundto
    
    x = e.x
    y = e.y

    ids = totids

    roundto = snapp.get()
    if roundto == 0:
        roundto=1

    poslabel.config(text="snapped to "+str(round(x/roundto)*roundto)+"x, "+str(round(y/roundto)*roundto)+"y")
    #print("Pointer is currently at %d, %d" %(x,y))

def click(e):
    global xc1,xc2,yc1,yc2,xc3,yc3,clickc,roundto, exportlines, ids, getfirstpoint, clickcs, drawingngon, linethicc, linec, totids
    
    
    ids = totids
    clickc += 1
    print("Clicked")

    if clickc == 1:
        xc1 = round(x/roundto)*roundto
        yc1 = round(y/roundto)*roundto
    if clickc == 2:
        if mode == "ngon" and getfirstpoint == False:
            xc1 = xc2
            yc1 = yc2

        xc2 = round(x/roundto)*roundto
        yc2 = round(y/roundto)*roundto
        
        if mode=="triangle":
            
            escape
        elif mode =="ngon":
            clickc = 1
        else:
            clickc = 0

        linethicc = thicc.get()
        if mode == "rectangle":
            print(fillcolor, isfilltransparent)
            if isfilltransparent == True:
                ids += 1
                totids += 1
                c.create_rectangle(xc1,yc1,xc2,yc2, fill="", outline=linecolor, width=linethicc)
                exportlines.append("c.create_rectangle("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+", width="+str(linethicc)+",fill='', outline='"+linecolor+"')")
            elif isfilltransparent == False:
                ids += 1
                totids += 1
                c.create_rectangle(xc1,yc1,xc2,yc2, fill=fillcolor, outline=linecolor, width=linethicc)
                exportlines.append("c.create_rectangle("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+", width="+str(linethicc)+",fill='"+fillcolor+"', outline='"+linecolor+"')")
        if mode == "oval":
            if isfilltransparent == True:
                ids += 1
                totids += 1
                c.create_oval(xc1,yc1,xc2,yc2, fill="", outline=linecolor, width=linethicc)
                exportlines.append("c.create_oval("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+", width="+str(linethicc)+",fill='', outline='"+linecolor+"')")
            elif isfilltransparent == False:
                ids += 1
                totids += 1
                c.create_oval(xc1,yc1,xc2,yc2, fill=fillcolor, outline=linecolor, width=linethicc)
                exportlines.append("c.create_oval("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+", width="+str(linethicc)+",fill='"+fillcolor+"', outline='"+linecolor+"')")
        if mode == "line":
            ids += 1
            totids += 1
            c.create_line(xc1,yc1,xc2,yc2, fill=linecolor, width=linethicc)
            exportlines.append("c.create_line("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+", width="+str(linethicc)+", fill='"+linecolor+"')")
        print(exportlines)

            

    if clickc == 3:
        linethicc = thicc.get()
        if mode == "triangle":
            ids += 1
            totids += 1
            clickc=0
            xc3 = round(x/roundto)*roundto
            yc3 = round(y/roundto)*roundto

            if isfilltransparent == True:
                c.create_polygon(xc1,yc1,xc2,yc2,xc3,yc3, fill="", outline=linecolor, width=linethicc)
                exportlines.append("c.create_polygon("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+","+str(xc3)+","+str(yc3)+", fill='',outline='"+linecolor+"', width="+str(linethicc)+")")
            elif isfilltransparent == False:
                c.create_polygon(xc1,yc1,xc2,yc2,xc3,yc3, fill=fillcolor, outline=linecolor, width=linethicc)
                exportlines.append("c.create_polygon("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+","+str(xc3)+","+str(yc3)+", fill='"+fillcolor+"',outline='"+linecolor+"', width="+str(linethicc)+")")
    
    if mode == 'ngon':
        clickcs.append(round(x/roundto)*roundto)
        clickcs.append(round(y/roundto)*roundto)
        
        print(clickcs)



def drawngon():
    global ids, clickcs, fillcolor, linecolor, linethicc, c, linec, totids
    
    print("drawngon")

    
    linethicc = thicc.get()
    ids += 1
    totids += 1

    if isfilltransparent == True:
        test = c.create_polygon(clickcs, fill="", outline= linecolor, width=linethicc)
        print(test)
        exportlines.append("c.create_polygon("+str(clickcs)+", fill='', outline='"+linecolor+"', width="+str(linethicc)+")")
    elif isfilltransparent == False:
        c.create_polygon(clickcs, fill=fillcolor, outline= linecolor, width=linethicc)
        exportlines.append("c.create_polygon("+str(clickcs)+", fill='"+fillcolor+"', outline='"+linecolor+"', width="+str(linethicc)+")")
    
    print("still drawngon")

    del clickcs [:]

    linec = 0
    

    print("CLEARED clickcs", clickcs)
    
    print("end drawngon")

    
        

win.bind('<Motion>',callback)
win.bind("<Button-1>", click)


def moderectangle():
    global mode, rectanglebutton,ovalbutton,linebutton,trianglebutton,ngonbutton,clickc
    clickc = 0
    mode = "rectangle"
    print(mode)

    rectanglebutton.configure(bg="#BDBDBD")
    ovalbutton.configure(bg="#FFFFFF")
    linebutton.configure(bg="#FFFFFF")
    trianglebutton.configure(bg="#FFFFFF")
    ngonbutton.configure(bg="#FFFFFF")
def modeoval():
    global mode, rectanglebutton,ovalbutton,linebutton,trianglebutton,ngonbutton,clickc
    clickc = 0
    mode = "oval"
    print(mode)
    rectanglebutton.configure(bg="#FFFFFF")
    ovalbutton.configure(bg="#BDBDBD")
    linebutton.configure(bg="#FFFFFF")
    trianglebutton.configure(bg="#FFFFFF")
    ngonbutton.configure(bg="#FFFFFF")
def modeline():
    global mode, rectanglebutton,ovalbutton,linebutton,trianglebutton,ngonbutton,clickc
    clickc = 0
    mode = "line"
    print(mode)
    rectanglebutton.configure(bg="#FFFFFF")
    ovalbutton.configure(bg="#FFFFFF")
    linebutton.configure(bg="#BDBDBD")
    trianglebutton.configure(bg="#FFFFFF")
    ngonbutton.configure(bg="#FFFFFF")
def modetriangle():
    global mode, rectanglebutton,ovalbutton,linebutton,trianglebutton,ngonbutton,clickc
    clickc = 0
    mode = "triangle"
    print(mode)
    rectanglebutton.configure(bg="#FFFFFF")
    ovalbutton.configure(bg="#FFFFFF")
    linebutton.configure(bg="#FFFFFF")
    trianglebutton.configure(bg="#BDBDBD")
    ngonbutton.configure(bg="#FFFFFF")
def modengon():
    global mode, rectanglebutton,ovalbutton,linebutton,trianglebutton,ngonbutton,clickc,getfirstpoint, drawingngon
    clickc = 0
    getfirstpoint = True
    mode = "ngon"

    if drawingngon == False:
        drawingngon = True
        ngonbutton.configure(text="Polygon (click again to stop drawing)")
    elif drawingngon == True:
        ngonbutton.configure(text="Polygon (click to start drawing again)")
        drawingngon = False
        drawngon()

    print(mode)
    rectanglebutton.configure(bg="#FFFFFF")
    ovalbutton.configure(bg="#FFFFFF")
    linebutton.configure(bg="#FFFFFF")
    trianglebutton.configure(bg="#FFFFFF")
    ngonbutton.configure(bg="#BDBDBD")

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

        filltransparentbut.configure(bg="#FFFFFF")
        filltransparentbut.config(text="Toggle Fill Transparent (False)")
    else:
        isfilltransparent = True

        filltransparentbut.configure(bg="#BDBDBD")
        filltransparentbut.config(text="Toggle Fill Transparent (True)")



def generate():
    print('generating')
    fp = open('tkinter_drawing.py', 'w')
    fp.write('#Made in DrawTk by TobaT3\n')
    fp.write('\nimport tkinter')
    fp.write('\nc = tkinter.Canvas(height=500, width=700)')
    fp.write('\nc.pack()\n')

    for x in exportlines:
        print(x)
        fp.write('\n'+x)

    fp.close()
    print('generated')


def getter():
    x=win.winfo_rootx()+c.winfo_x()
    y=win.winfo_rooty()+c.winfo_y()
    x1=x+c.winfo_width()
    y1=y+c.winfo_height()
    
    ImageGrab.grab().crop((x,y,x1,y1)).save("tkinter_drawing.png")


#generate()

def undo():
    global ids, totids
    c.delete(ids)

    ids -= 1
    exportlines.pop()
    print(exportlines, type(exportlines))
    print(ids)

def deleteall():
    c.delete("all")

toolwindow = tkinter.Toplevel(win)
toolwindow.geometry("300x705")
toolwindow.title("Toolbox")
toolwindow.resizable(False, False)

#lbl = tkinter.Label(toolwindow, text="I am in this toolwindow thing right").pack()


poslabel = tkinter.Label(toolwindow, text="", font="Roboto 14")
poslabel.pack(pady=10)

undobutton = tkinter.Button(toolwindow, text="Undo", command=undo, bg="light green").pack()

toollabel = tkinter.Label(toolwindow, text="Tools", font="Roboto 14").pack()
rectanglebutton = tkinter.Button(toolwindow, text="Rectangle", command=moderectangle, bg="#BDBDBD")
rectanglebutton.pack()
ovalbutton = tkinter.Button(toolwindow, text="Oval", command=modeoval)
ovalbutton.pack()
linebutton = tkinter.Button(toolwindow, text="Line (uses OUTLINE color not FILL COLOR", command=modeline)
linebutton.pack()
trianglebutton = tkinter.Button(toolwindow, text="Triangle", command=modetriangle)
trianglebutton.pack()
ngonbutton = tkinter.Button(toolwindow, text="Polygon (click to start drawing)", command=modengon)
ngonbutton.pack()

collabel = tkinter.Label(toolwindow, text="Colors and thickness", font="Roboto 14").pack()
colpickbut = tkinter.Button(toolwindow, text="Fill Color", command=opencolorpick, bg=fillcolor)
colpickbut.pack()

filltransparentbut = tkinter.Button(toolwindow, text="Toggle Fill Transparent (True)", command=togglefilltransparent, bg=("#BDBDBD"))
filltransparentbut.pack()

colpickbut2 = tkinter.Button(toolwindow, text="Line Color", command=opencolorpick2, bg=linecolor)
colpickbut2.pack()

thicc = tkinter.Scale(toolwindow, from_=1, to=75, orient=HORIZONTAL, tickinterval=10, length=200, label="Line Width", resolution=5)
thicc.pack()

setlabel = tkinter.Label(toolwindow, text="Other", font="Roboto 14").pack()

snapp = tkinter.Scale(toolwindow, from_=0, to=300, orient=HORIZONTAL, length=200, label="Snapping to every (0 to turn off)", resolution=5)
snapp.pack()
snapp.set(roundto)


explabel = tkinter.Label(toolwindow, text="Export", font="Roboto 14").pack()
warnlabel2 = tkinter.Label(toolwindow, text="WARNING: Will overwrite previously generated files", fg="red").pack()
warnlabel3 = tkinter.Label(toolwindow, text="Copy the tkinter_drawing files somewhere else \n if you dont want to lose them", fg="red").pack()
exportbut = tkinter.Button(toolwindow, text="export to .py", command=generate).pack()
imgbut = tkinter.Button(toolwindow, text="export to .png", command=getter).pack()

warnlabel = tkinter.Label(toolwindow, text="WARNING: Will delete everything", fg="red").pack()
deletebut = tkinter.Button(toolwindow, text="CLEAR CANVAS", command=deleteall, bg="red").pack()

melabel = tkinter.Label(toolwindow, text="Made by TobaT3", font="Roboto 8").pack()

win.mainloop()
toolwindow.mainloop()
