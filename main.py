from glob import escape
import tkinter
from tkinter import HORIZONTAL, colorchooser, filedialog, messagebox, font
import customtkinter
from PIL import ImageGrab
import pathlib
import tkfontchooser

#import pyi_splash #doesnt actually import anything; but should be uncommented when building with pyinstaller so the splash screen closes
#pyi_splash.close()

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
win = customtkinter.CTk()
win.resizable(False, False)
win.title("TkPaint Canvas")
#win.iconbitmap("drawtk.ico")

c = tkinter.Canvas(win, height=500, width=700, highlightthickness=0,borderwidth=0)
c.pack()

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
center_x = int(screen_width/2 - 700 / 2)
center_y = int(screen_height/2 - 500 / 2)
win.geometry(f'{700}x{500}+{center_x}+{center_y}')


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
text = ""
font = "Helvetica 15"
fontstr = "Helvetica 15"
textid = 999999999999

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

    poslabel.configure(text="snapped to "+str(round(x/roundto)*roundto)+"x, "+str(round(y/roundto)*roundto)+"y")
    #print("Pointer is currently at %d, %d" %(x,y))

def click(e):
    global xc1,xc2,yc1,yc2,xc3,yc3,clickc,roundto, exportlines, ids, getfirstpoint, clickcs, drawingngon, linethicc, linec, totids, thicc, textid, font
    
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
    
    if mode == 'text':
        xc1 = round(x/roundto)*roundto
        yc1 = round(y/roundto)*roundto

        c.delete(textid)
        c.create_text(xc1,yc1,text=text, font=font)
        ids += 1
        totids += 1
        textid = totids

    if mode == 'delete': # thanks https://stackoverflow.com/questions/38982313/python-tkinter-identify-object-on-click
        c.delete(c.find_closest(e.x, e.y))

def onKeyPress(event):
    global textid, totids, text, totids, ids, xc1,xc2, font
    
    if mode == "text":
        if event.keysym != "BackSpace":
            print("you pressed %s\n" % (event.char))
            text = text+event.char
        elif event.keysym == "BackSpace":
            print("backspace")
            text = text[:-1]

        c.delete(textid)
        c.create_text(xc1,yc1,text=text, font=font)
        ids += 1
        totids += 1
        textid = totids

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
def donetext():
    global textid, totids, text, totids, ids, xc1,xc2, font, exportlines

    c.delete(textid)
    c.create_text(xc1,yc1,text=text, font=font)
    exportlines.append("c.create_text("+str(xc1)+','+str(yc1)+", text='"+text+"', font='"+str(font)+"')")
    print(exportlines)
    ids += 1
    totids += 1
    textid = 999999
    text = ""



win.bind('<Motion>',callback)
win.bind("<Button-1>", click)
win.bind('<KeyPress>', onKeyPress)

def modedelete():
    global mode, rectanglebutton,ovalbutton,linebutton,trianglebutton,ngonbutton,clickc
    clickc = 0
    mode = "delete"
    print(mode)

    rectanglebutton.configure(bg="#BDBDBD")
    ovalbutton.configure(bg="#FFFFFF")
    linebutton.configure(bg="#FFFFFF")
    trianglebutton.configure(bg="#FFFFFF")
    ngonbutton.configure(bg="#FFFFFF")
    textbutton.configure(bg="#FFFFFF")

    if mode=="text":
        donetext()
        textwindow.destroy()
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
    textbutton.configure(bg="#FFFFFF")

    if mode=="text":
        donetext()
        textwindow.destroy()
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
    textbutton.configure(bg="#FFFFFF")

    if mode=="text":
        donetext()
        textwindow.destroy()
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
    textbutton.configure(bg="#FFFFFF")

    if mode=="text":
        donetext()
        textwindow.destroy()
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
    textbutton.configure(bg="#FFFFFF")

    if mode=="text":
        donetext()
        textwindow.destroy()
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
    textbutton.configure(bg="#FFFFFF")

    if mode=="text":
        donetext()
        textwindow.destroy()
def modetext():
    global mode, rectanglebutton,ovalbutton,linebutton,trianglebutton,ngonbutton,clickc,getfirstpoint, drawingngon, toolwindow, textwindow, textwindow
    clickc = 0
    mode = "text"

    createtextwindow()

    print(mode)
    rectanglebutton.configure(bg="#FFFFFF")
    ovalbutton.configure(bg="#FFFFFF")
    linebutton.configure(bg="#FFFFFF")
    trianglebutton.configure(bg="#FFFFFF")
    ngonbutton.configure(bg="#FFFFFF")
    textbutton.configure(bg='#BDBDBD')

def fontchooser():
    global font, fontbutton

    font = tkfontchooser.askfont()

    font = tkinter.font.Font(root=None, family=font["family"], size=font["size"], weight=font["weight"], slant=font["slant"], underline=font["underline"], overstrike=font["overstrike"])

    print(font)

    fontstr = font["family"]+" "+str(font["size"])

    fontbutton.configure(text="Change font and size ("+fontstr+")")

def createtextwindow():
    global textwindow, fontbutton, font, fontstr

    textwindow = tkinter.Toplevel(toolwindow)
    textwindow.geometry("300x100")
    textwindow.title("Text")
    textwindow.resizable(False, False)
    textwindow.overrideredirect(True)

    x = toolwindow.winfo_x()
    y = toolwindow.winfo_y()
    textwindow.geometry(f'{300}x{60}+{x-300}+{y+235}')

    fontbutton = tkinter.Button(textwindow, text="Change font and size "+str(fontstr), command=fontchooser)
    fontbutton.pack()

    donebutton = tkinter.Button(textwindow, text="DONE", command=donetext)
    donebutton.pack()

    textwindow.bind('<KeyPress>', onKeyPress) # so you can type in both windows; annoyed me when you couldnt
    

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
        filltransparentbut.configure(text="Toggle Fill Transparent (False)")
    else:
        isfilltransparent = True

        filltransparentbut.configure(bg="#BDBDBD")
        filltransparentbut.configure(text="Toggle Fill Transparent (True)")

def load():
    global ids, totids

    fp = filedialog.askopenfile(initialdir = pathlib.Path(__file__).parent.resolve(), title = "Open a DrawTk generated .py file", filetypes=[("Python file", ".py")], defaultextension=".py")

    i = 0
    
    for x in fp:
        i += 1

        if i > 6 and x != "tkinter.mainloop()":
            exec(x)
            totids += 1
            ids += 1

def exportpy():

    fp = filedialog.asksaveasfile(initialdir = pathlib.Path(__file__).parent.resolve(), title = "Select a .py file to export to", filetypes=[("Python file", ".py")], defaultextension=".py")

    print('generating')
    #fp = open(filename, 'w')
    fp.write('#If you want to load this file make sure lines 1-6 are not modified\n')
    fp.write('\nimport tkinter')
    fp.write('\nc = tkinter.Canvas(height=500, width=700)')
    fp.write('\nc.pack()\n')
    
    for x in exportlines:
        print(x)
        fp.write('\n'+x)
    
    fp.write("\ntkinter.mainloop()")
    fp.write("\n#Made in DrawTk by TobaT3")

    fp.close()
    print('generated')


def exportpng():
    #Thanks to B.Jenkins on stack overflow for https://stackoverflow.com/a/38645917/15888488 (yes its like 6 years old but it still works)
    x=win.winfo_rootx()+c.winfo_x()
    y=win.winfo_rooty()+c.winfo_y()
    x1=x+c.winfo_width()
    y1=y+c.winfo_height()
    
    filename = filedialog.asksaveasfilename(initialdir = pathlib.Path(__file__).parent.resolve(), title = "Select an image file to export to", filetypes=[("PNG", ".png"), ("JPEG", ".jpeg"), ("TIFF", ".tiff"), ("BMP", ".bmp")], defaultextension=".png")
    ImageGrab.grab().crop((x,y,x1,y1)).save(filename)


#generate()

def undo():
    global ids, totids
    c.delete(ids)
    ids -= 1
    exportlines.pop()
    print(exportlines, type(exportlines))
    print(ids)

def deleteall():
    global exportlines

    if messagebox.askokcancel("Are you sure?", "This will delete your canvas for ever (a long time)", icon = 'warning') == False:
        print("cancelled deleteall")
    else:
        c.delete("all")
        exportlines.clear()

toolwindow = customtkinter.CTkToplevel(win)
toolwindow.geometry("300x700")
toolwindow.title("Toolbox")
#toolwindow.resizable(False, False)

screen_width = toolwindow.winfo_screenwidth()
screen_height = toolwindow.winfo_screenheight()
center_x = int(screen_width/2 - 700 / 2)
center_y = int(screen_height/2 - 500 / 2)
toolwindow.geometry(f'{300}x{700}+{center_x-310}+{center_y-175}')

def movetoolwin(e):
    x = win.winfo_x()
    y = win.winfo_y()

    toolwindow.geometry(f'{300}x{875}+{x-310}+{y-175}')

    if mode == "text":
        x = toolwindow.winfo_x()
        y = toolwindow.winfo_y()
        textwindow.geometry(f'{300}x{60}+{x-300}+{y+235}')

win.bind('<Configure>', movetoolwin)

#lbl = tkinter.Label(toolwindow, text="I am in this toolwindow thing right").pack()


poslabel = customtkinter.CTkLabel(toolwindow, text="e", text_font="Roboto 14")
poslabel.pack(pady=5)

undobutton = customtkinter.CTkButton(toolwindow, text="Undo", command=undo, fg_color="green", hover_color="dark green").pack(pady=5)
delobjbutton = customtkinter.CTkButton(toolwindow, text="Delete object", command=modedelete, bg="#BDBDBD")
delobjbutton.pack(pady=5)

toollabel = customtkinter.CTkLabel(toolwindow, text="Tools", text_font="Roboto 14").pack(pady=5)
rectanglebutton = customtkinter.CTkButton(toolwindow, text="Rectangle", command=moderectangle, bg="#BDBDBD")
rectanglebutton.pack(pady=5)
ovalbutton = customtkinter.CTkButton(toolwindow, text="Oval", command=modeoval)
ovalbutton.pack(pady=5)
linebutton = customtkinter.CTkButton(toolwindow, text="Line (uses OUTLINE color not FILL COLOR", command=modeline)
linebutton.pack(pady=5)
trianglebutton = customtkinter.CTkButton(toolwindow, text="Triangle", command=modetriangle)
trianglebutton.pack(pady=5)
ngonbutton = customtkinter.CTkButton(toolwindow, text="Polygon (click to start drawing)", command=modengon)
ngonbutton.pack(pady=5)
textbutton = customtkinter.CTkButton(toolwindow, text="Text", command=modetext)
textbutton.pack(pady=5)

collabel = customtkinter.CTkLabel(toolwindow, text="Colors and thickness", text_font="Roboto 14").pack(pady=10)
colpickbut = customtkinter.CTkButton(toolwindow, text="Fill Color", command=opencolorpick, bg=fillcolor)
colpickbut.pack(pady=5)

filltransparentbut = customtkinter.CTkButton(toolwindow, text="Toggle Fill Transparent (True)", command=togglefilltransparent, bg=("#BDBDBD"))
filltransparentbut.pack(pady=5)

colpickbut2 = customtkinter.CTkButton(toolwindow, text="Outline Color", command=opencolorpick2, bg=linecolor)
colpickbut2.pack(pady=5)

def thiccupgrade(value):
    global thiccvaluelabel
    if value == 0:
        thiccvaluelabel.configure(text="Off")
    else:    
        thiccvaluelabel.configure(text=str(round((value))))

snappinglabel = customtkinter.CTkLabel(toolwindow, text="Snapping").pack(pady=5)
thicc = customtkinter.CTkSlider(toolwindow, from_=1, to=75, orient=HORIZONTAL, width=200, number_of_steps=5) # label="Line Width",
thicc.pack()
thicc.set(linethicc)
thiccvaluelabel = customtkinter.CTkLabel(toolwindow, text="50")
thiccvaluelabel.pack(pady=0)

deletebut = customtkinter.CTkButton(toolwindow, text="Load", command=load).pack(pady=5)

setlabel = customtkinter.CTkLabel(toolwindow, text="Other", text_font="Roboto 14").pack(pady=5)

def snappupgrade(value):
    global snappingvaluelabel
    if value == 0:
        snappingvaluelabel.configure(text="Off")
    else:    
        snappingvaluelabel.configure(text=str(round((value))))

snappinglabel = customtkinter.CTkLabel(toolwindow, text="Snapping").pack(pady=5)
snapp = customtkinter.CTkSlider(toolwindow, from_=0, to=300, orient=HORIZONTAL, width=200, number_of_steps=60, command=snappupgrade) #label="Snapping to every (0 to turn off)",
snapp.pack()
snapp.set(roundto)
snappingvaluelabel = customtkinter.CTkLabel(toolwindow, text="50")
snappingvaluelabel.pack(pady=0)

explabel = customtkinter.CTkLabel(toolwindow, text="Save and Export", text_font="Roboto 14").pack(pady=5)
#warnlabel2 = tkinter.Label(toolwindow, text="WARNING: Will overwrite previously generated files", fg="red").pack()
#warnlabel3 = tkinter.Label(toolwindow, text="Copy the tkinter_drawing files somewhere else \n if you dont want to lose them", fg="red").pack()
exportbut = customtkinter.CTkButton(toolwindow, text="Save - export to .py", command=exportpy).pack(pady=5)
imgbut = customtkinter.CTkButton(toolwindow, text="export to image", command=exportpng).pack(pady=5)

#warnlabel = customtkinter.CTkLabel(toolwindow, text="WARNING: Will delete everything", fg="red").pack(pady=5)
deletebut = customtkinter.CTkButton(toolwindow, text="CLEAR CANVAS", command=deleteall, fg_color="red", hover_color="red").pack(pady=5)

melabel = customtkinter.CTkLabel(toolwindow, text="Made by TobaT3", text_font="Roboto 8").pack()


win.mainloop()
toolwindow.mainloop()