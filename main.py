import glob
import tkinter
from tkinter import HORIZONTAL, colorchooser, filedialog, messagebox, font, PhotoImage, StringVar
from PIL import ImageGrab, Image
import pathlib
import os, sys
import tkfontchooser

try:
    import pyi_splash
    pyi_splash.close()
except:
    pass #for pyisntaller

CANVAS_HEIGHT = 500
CANVAS_WIDTH = 700


win = tkinter.Tk()
win.resizable(False, False)
win.title("TkPaint Canvas")

bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__))) # i have no idea what this does but it fixed my pyinstaller problems! thanks stack overflow

path_to_ico = os.path.abspath(os.path.join(bundle_dir, 'drawtk.ico'))
irectangle = PhotoImage(file= os.path.abspath(os.path.join(bundle_dir, 'irectangle.png')))
ioval = PhotoImage(file=os.path.abspath(os.path.join(bundle_dir, 'ioval.png')))
iline = PhotoImage(file=os.path.abspath(os.path.join(bundle_dir, 'iline.png')))
ingon = PhotoImage(file=os.path.abspath(os.path.join(bundle_dir, 'ingon.png')))
itext = PhotoImage(file=os.path.abspath(os.path.join(bundle_dir, 'itext.png')))

# win.iconbitmap(path_to_ico) #DOESNT WORK ON LINUX

c = tkinter.Canvas(win, height=CANVAS_HEIGHT, width=CANVAS_WIDTH, highlightthickness=0,borderwidth=0)
c.pack()

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
center_x = int(screen_width/2 - CANVAS_WIDTH / 2)
center_y = int(screen_height/2 - CANVAS_HEIGHT / 2)
win.geometry(f'{CANVAS_WIDTH}x{CANVAS_HEIGHT}+{center_x}+{center_y}')

#deafult values
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
idlist = []
linec = 0
linethicc = 1
getfirstpoint = True
drawingngon = False
text = ""
font = "Helvetica 15"
fontstr = "Helvetica 15"
textid = 999999999999
previewid = None
previewobj = None
preview = False
pwcoordc = 1 #preview coordinate count (eg. xc2,yc2 exist for triangles and stuff)
clickcs = []
exportlines = []
exportobjdict = {} #a dictionary which contains the object ids of objects that will be exported with their corresponding id in the exportlines list.

fillcolor = "#FFFFFF"
linecolor = "#000000"
isfilltransparent = True

#animation variables deafult values:
isanimation = False
animationfolder = None
frame = 0
gifms = StringVar()

def callback(e): # mouse movement
    global c,x,y, poslabel, snapp, roundto,xc1,yc1,xc2,yc2,previewid,ids,preview, linethicc, isfilltransparent, fillcolor, linecolor, pwcoordc, mode, idlist, previewid, drawingngon, previewobj, clickcs
    
    x = e.x
    y = e.y

    rx = round(x/roundto)*roundto
    ry = round(y/roundto)*roundto

    roundto = snapp.get()
    if roundto == 0:
        roundto=1
    linethicc = thicc.get()

    poslabel.config(text="snapped to "+str(round(x/roundto)*roundto)+"x, "+str(round(y/roundto)*roundto)+"y")
    #print("Pointer is currently at %d, %d" %(x,y))

    if preview == True:
        ids +=1
        c.delete(previewobj)
        previewobj = None
        if mode == "rectangle":
            if isfilltransparent == True:
                previewobj = c.create_rectangle(xc1,yc1,rx,ry, fill="", outline=linecolor, width=linethicc, dash=(5,2))
            elif isfilltransparent == False:
                previewobj = c.create_rectangle(xc1,yc1,rx,ry, fill=fillcolor, outline=linecolor, width=linethicc, dash=(5,2))
        if mode == "oval":
            if isfilltransparent == True:
                previewobj = c.create_oval(xc1,yc1,rx,ry, fill="", outline=linecolor, width=linethicc, dash=(5,2))
            elif isfilltransparent == False:
                previewobj = c.create_oval(xc1,yc1,rx,ry, fill=fillcolor, outline=linecolor, width=linethicc, dash=(5,2))
        if mode == "line":
            previewobj = c.create_line(xc1,yc1,rx,ry, fill=linecolor, width=linethicc, dash=(5,2))
        if mode == "triangle":
            if pwcoordc == 1:
                previewobj = c.create_line(xc1,yc1,rx,ry, fill=linecolor, width=linethicc, dash=(5,2))
            elif pwcoordc == 2:
                if isfilltransparent == True:
                    previewobj = c.create_polygon(xc1,yc1,xc2,yc2,rx,ry, fill="", width = linethicc, outline=linecolor, dash=(5,2))
                elif isfilltransparent == False:
                    previewobj = c.create_polygon(xc1,yc1,xc2,yc2,rx,ry, fill=fillcolor, width = linethicc, outline=linecolor, dash=(5,2))
        if mode == "ngon":
            if isfilltransparent == True:
                previewobj = c.create_polygon(clickcs,rx,ry, fill="", width=linethicc, outline=linecolor, dash=(5,2)) #sure it appears closed even if it isnt but a better solution with lines would have been way too complicated
            elif isfilltransparent == False:
                previewobj = c.create_polygon(clickcs,rx,ry, fill=fillcolor, width=linethicc, outline=linecolor, dash=(5,2)) #sure it appears closed even if it isnt but a better solution with lines would have been way too complicated


def click(e):
    global xc1,xc2,yc1,yc2,xc3,yc3,clickc,roundto, exportlines, ids, getfirstpoint, clickcs, drawingngon, linethicc, linec, thicc, textid, font, idlist, preview, pwcoordc,previewid
    
    clickc += 1
    pwcoordc += 1
    print("Clicked")
    print(exportlines)
    print(exportobjdict)
    print(idlist)
    print(ids)
    
    c.delete(previewid)
    c.delete(textid) #sometimes for some reason the deleting screws up, so this is another override

    if clickc == 1:
        xc1 = round(x/roundto)*roundto
        yc1 = round(y/roundto)*roundto
        preview = True
    if clickc == 2:
        if mode == "ngon" and getfirstpoint == False:
            xc1 = xc2
            yc1 = yc2

        xc2 = round(x/roundto)*roundto
        yc2 = round(y/roundto)*roundto
        
        if mode=="triangle":
            glob.escape
        elif mode =="ngon":
            clickc = 1
        else:
            clickc = 0
            preview = False
            pwcoordc = 0
            

        if mode == "rectangle":
            print(fillcolor, isfilltransparent)
            if isfilltransparent == True:
                c.create_rectangle(xc1,yc1,xc2,yc2, fill="", outline=linecolor, width=linethicc)
                exportlines.append("c.create_rectangle("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+", width="+str(linethicc)+",fill='', outline='"+linecolor+"')")
            elif isfilltransparent == False:
                c.create_rectangle(xc1,yc1,xc2,yc2, fill=fillcolor, outline=linecolor, width=linethicc)
                exportlines.append("c.create_rectangle("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+", width="+str(linethicc)+",fill='"+fillcolor+"', outline='"+linecolor+"')")
        if mode == "oval":
            if isfilltransparent == True:
                c.create_oval(xc1,yc1,xc2,yc2, fill="", outline=linecolor, width=linethicc)
                exportlines.append("c.create_oval("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+", width="+str(linethicc)+",fill='', outline='"+linecolor+"')")
            elif isfilltransparent == False:
                c.create_oval(xc1,yc1,xc2,yc2, fill=fillcolor, outline=linecolor, width=linethicc)
                exportlines.append("c.create_oval("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+", width="+str(linethicc)+",fill='"+fillcolor+"', outline='"+linecolor+"')")
        if mode == "line":

            c.create_line(xc1,yc1,xc2,yc2, fill=linecolor, width=linethicc)
            exportlines.append("c.create_line("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+", width="+str(linethicc)+", fill='"+linecolor+"')")
        
        ids += 1
        idlist.append(ids)
        c.delete(previewobj)
        exportobjdict.update({ids: len(exportlines)})

            

    if clickc == 3:
        linethicc = thicc.get()
        if mode == "triangle":
            ids += 1
            idlist.append(ids)
            c.delete(previewobj)
            clickc=0
            preview = False
            pwcoordc = 0

            xc3 = round(x/roundto)*roundto
            yc3 = round(y/roundto)*roundto

            if isfilltransparent == True:
                c.create_polygon(xc1,yc1,xc2,yc2,xc3,yc3, fill="", outline=linecolor, width=linethicc)
                exportlines.append("c.create_polygon("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+","+str(xc3)+","+str(yc3)+", fill='',outline='"+linecolor+"', width="+str(linethicc)+")")
            elif isfilltransparent == False:
                c.create_polygon(xc1,yc1,xc2,yc2,xc3,yc3, fill=fillcolor, outline=linecolor, width=linethicc)
                exportlines.append("c.create_polygon("+str(xc1)+","+str(yc1)+","+str(xc2)+","+str(yc2)+","+str(xc3)+","+str(yc3)+", fill='"+fillcolor+"',outline='"+linecolor+"', width="+str(linethicc)+")")
            
            exportobjdict.update({ids: len(exportlines)})
    
    if mode == 'ngon':

        rx = round(x/roundto)*roundto
        ry = round(y/roundto)*roundto

        if len(clickcs) >> 2: #to avoid an IndexError; could have done a try except but whatever
            print(clickcs[0], clickcs[1])
            print(x, y)
            if clickcs[0] == rx and clickcs[1] == ry:
                print("drawngon")

                ids += 1
                idlist.append(ids)

                if isfilltransparent == True:
                    test = c.create_polygon(clickcs, fill="", outline= linecolor, width=linethicc)
                    print(test)
                    exportlines.append("c.create_polygon("+str(clickcs)+", fill='', outline='"+linecolor+"', width="+str(linethicc)+")")
                elif isfilltransparent == False:
                    c.create_polygon(clickcs, fill=fillcolor, outline= linecolor, width=linethicc)
                    exportlines.append("c.create_polygon("+str(clickcs)+", fill='"+fillcolor+"', outline='"+linecolor+"', width="+str(linethicc)+")")

                c.delete(previewobj)
                exportobjdict.update({ids: len(exportlines)})

                preview = False
                pwcoordc = 0
                
                print("still drawngon")

                del clickcs [:]
                clickc = 0
                linec = 0
            else:
                clickcs.append(rx)
                clickcs.append(ry)
        else:
            print("error", clickcs)
            clickcs.append(rx)
            clickcs.append(ry)

    
    if mode == 'text':
        xc1 = round(x/roundto)*roundto
        yc1 = round(y/roundto)*roundto

        c.delete(textid)
        textid = c.create_text(xc1,yc1,text=text, font=font)
        print(exportlines)
        ids += 1

    if mode == 'delete': # thanks https://stackoverflow.com/questions/38982313/python-tkinter-identify-object-on-click
        
        delid = (c.find_closest(e.x, e.y)[0])
        print(exportlines, delid)
        if len(exportlines) > 1:
            popinexportlines = exportobjdict[delid]
            exportlines.pop(popinexportlines)
            moveExportObjDict(popinexportlines)
        
        
        c.delete(delid)
        idinlist = idlist.index(delid)
        idinlist = idlist.pop(idinlist)

        print(exportlines)
        


def onKeyPress(event):
    global textid, text, idlist, ids, xc1,xc2, font
    
    isshift = (event.state & 0x1) != 0 #bool

    if mode == "text":
        if event.keysym == "BackSpace":
            print("backspace")
            text = text[:-1]
        elif not(isshift) and event.keysym == "Return": #Return is keysym for Enter
            donetext()
        else:
            print("you pressed %s\n" % (event.char))
            text = text+event.char

        c.delete(textid)
        textid = c.create_text(xc1,yc1,text=text, font=font)
        ids += 1

        

def drawngon():
    global ids, clickcs, fillcolor, linecolor, linethicc, c, linec, idlist,preview, clickc

    print("CLEARED clickcs", clickcs)
    
    print("end drawngon")
def donetext():
    global textid, text, idlist, ids, xc1,xc2, font, exportlines

    print("DONE TEXT")

    c.delete(textid)
    c.create_text(xc1,yc1,text=text, font=font)
    exportlines.append("c.create_text("+str(xc1)+','+str(yc1)+", text='"+text+"', font='"+str(font)+"')")
    ids += 1
    idlist.append(ids)
    preview = False
    textid = 999999
    text = ""
    exportobjdict.update({ids: len(exportlines)})



win.bind('<Motion>',callback)
win.bind("<Button-1>", click)
win.bind('<KeyPress>', onKeyPress)


def modedelete():
    global mode, rectanglebutton,ovalbutton,linebutton,trianglebutton,ngonbutton,clickc, delobjbutton
    clickc = 0
    mode = "delete"
    print(mode)

    rectanglebutton.configure(bg="#FFFFFF")
    ovalbutton.configure(bg="#FFFFFF")
    linebutton.configure(bg="#FFFFFF")
    ngonbutton.configure(bg="#FFFFFF")
    # textbutton.configure(bg="#FFFFFF")
    delobjbutton.configure(bg="#BDBDBD")

    if mode=="text":
        donetext()
        textwindow.destroy()
def moderectangle():
    global mode, rectanglebutton,ovalbutton,linebutton,trianglebutton,ngonbutton,clickc, delobjbutton
    clickc = 0
    mode = "rectangle"
    print(mode)

    rectanglebutton.configure(bg="#BDBDBD")
    ovalbutton.configure(bg="#FFFFFF")
    linebutton.configure(bg="#FFFFFF")
    ngonbutton.configure(bg="#FFFFFF")
    # textbutton.configure(bg="#FFFFFF")
    delobjbutton.configure(bg="#FFFFFF")

    if mode=="text":
        donetext()
        textwindow.destroy()
def modeoval():
    global mode, rectanglebutton,ovalbutton,linebutton,trianglebutton,ngonbutton,clickc, delobjbutton
    clickc = 0
    mode = "oval"
    print(mode)
    rectanglebutton.configure(bg="#FFFFFF")
    ovalbutton.configure(bg="#BDBDBD")
    linebutton.configure(bg="#FFFFFF")
    ngonbutton.configure(bg="#FFFFFF")
    # textbutton.configure(bg="#FFFFFF")
    delobjbutton.configure(bg="#FFFFFF")

    if mode=="text":
        donetext()
        textwindow.destroy()
def modeline():
    global mode, rectanglebutton,ovalbutton,linebutton,trianglebutton,ngonbutton,clickc, delobjbutton
    clickc = 0
    mode = "line"
    print(mode)
    rectanglebutton.configure(bg="#FFFFFF")
    ovalbutton.configure(bg="#FFFFFF")
    linebutton.configure(bg="#BDBDBD")
    ngonbutton.configure(bg="#FFFFFF")
    # textbutton.configure(bg="#FFFFFF")
    delobjbutton.configure(bg="#FFFFFF")

    if mode=="text":
        donetext()
        textwindow.destroy()
def modetriangle():
    global mode, rectanglebutton,ovalbutton,linebutton,trianglebutton,ngonbutton,clickc, delobjbutton
    clickc = 0
    mode = "triangle"
    print(mode)
    rectanglebutton.configure(bg="#FFFFFF")
    ovalbutton.configure(bg="#FFFFFF")
    linebutton.configure(bg="#FFFFFF")
    ngonbutton.configure(bg="#FFFFFF")
    # textbutton.configure(bg="#FFFFFF")
    delobjbutton.configure(bg="#FFFFFF")

    if mode=="text":
        donetext()
        textwindow.destroy()
def modengon():
    global mode, rectanglebutton,ovalbutton,linebutton,trianglebutton,ngonbutton,clickc,getfirstpoint, drawingngon, delobjbutton
    clickc = 0
    getfirstpoint = True
    mode = "ngon"

    print(mode)
    rectanglebutton.configure(bg="#FFFFFF")
    ovalbutton.configure(bg="#FFFFFF")
    linebutton.configure(bg="#FFFFFF")
    ngonbutton.configure(bg="#BDBDBD")
    # textbutton.configure(bg="#FFFFFF")
    delobjbutton.configure(bg="#FFFFFF")

    if mode=="text":
        donetext()
        textwindow.destroy()
def modetext():
    global mode, rectanglebutton,ovalbutton,linebutton,trianglebutton,ngonbutton,clickc,getfirstpoint, drawingngon, toolwindow, textwindow, textwindow, delobjbutton
    clickc = 0
    mode = "text"

    #createtextwindow()
    fontchooser()

    print(mode)
    rectanglebutton.configure(bg="#FFFFFF")
    ovalbutton.configure(bg="#FFFFFF")
    linebutton.configure(bg="#FFFFFF")
    ngonbutton.configure(bg="#FFFFFF")
    # textbutton.configure(bg='#BDBDBD')
    delobjbutton.configure(bg="#FFFFFF")

def fontchooser():
    global font, toolwindow

    font = tkfontchooser.askfont(master=toolwindow, title="Pick a font", text="Text will look like this")

    font = tkinter.font.Font(root=None, family=font["family"], size=font["size"], weight=font["weight"], slant=font["slant"], underline=font["underline"], overstrike=font["overstrike"])

def updategiflengthl(arg1, arg2, arg3): #args are useless but im using the stringvar callback thing so it passes them along
    global giflengthl

    frames = [Image.open(image) for image in glob.glob(f"{animationfolder}/*.PNG")]
    frames = len(frames)
    giflengthl.configure(text=f"Frames: {frames}, Total length: {(int(gifms.get())/1000)*frames}s")

def creategifexportwindow():
    global gifexwindow, gifms, giflengthl

    gifexwindow = tkinter.Toplevel(toolwindow)
    gifexwindow.title("Export animation")
    gifexwindow.resizable(False, False)
    gifexwindow.overrideredirect(False)

    entryms = tkinter.Entry(gifexwindow, textvariable=gifms, justify="right", )
    entryms.insert(0, "100")
    entryms.grid(column=0, row=0)

    tkinter.Label(gifexwindow, text="miliseconds/frame").grid(column=1, row=0)

    frames = [Image.open(image) for image in glob.glob(f"{animationfolder}/*.PNG")]
    frames = len(frames)
    giflengthl = tkinter.Label(gifexwindow, text=f"Frames: {frames}, Total length: {(int(gifms.get())/1000)*frames}s")
    giflengthl.grid(column=0, row=1)

    tkinter.Button(gifexwindow, text="Export", command=exportgif).grid(column=1,row=1)

    x = toolwindow.winfo_x()
    y = toolwindow.winfo_y()
    gifexwindow.geometry(f'{300}x{60}') #+{x-300}+{y+235}
    
    gifms.trace_add("write", updategiflengthl)


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
        filltransparentbut.config(text="Fill Transparent (F)")
    else:
        isfilltransparent = True

        filltransparentbut.configure(bg="#BDBDBD")
        filltransparentbut.config(text="Fill Transparent (T)")

"""When something is popped from export lines, exportobjdict needs to be changed accordingly. Changes every value in the dict after 'afterId' by one. This is horrible code lmao"""
def moveExportObjDict(afterId: int) -> None:
    for k in exportobjdict:
        if exportobjdict[k] > afterId:
            exportobjdict[k] = exportobjdict[k]-1


def load():
    global ids, idlist, exportlines

    fp = filedialog.askopenfile(initialdir = pathlib.Path(__file__).parent.resolve(), title = "Open a DrawTk generated .py file", filetypes=[("Python file", ".py")], defaultextension=".py")

    i = 0
    
    for x in fp:
        i += 1

        if i > 6 and x != "tkinter.mainloop()":
            exec(x)
            exportlines.append(x)
            ids += 1
            idlist.append(ids)
    
    fp.close()

def exportpy():

    fp = filedialog.asksaveasfile(initialdir = pathlib.Path(__file__).parent.resolve(), title = "Select a .py file to export to", filetypes=[("Python file", ".py")], defaultextension=".py")

    print('generating')
    #filename = "test.py"
    #fp = open(filename, 'w')
    fp.write('#If you want to load this file make sure lines 1-6 are not modified\n')
    fp.write('\nimport tkinter')
    fp.write(f'\nc = tkinter.Canvas(height={CANVAS_HEIGHT}, width={CANVAS_WIDTH})')
    fp.write('\nc.pack()\n')
    
    for x in exportlines:
        print(x)
        fp.write('\n'+x)
    
    fp.write("\ntkinter.mainloop()") #tkinter.mainloop() istecnhically not needed, but if it is excluded the generated file doesnt run in vscode only via IDLE so i just keep it
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


def exportgif():
    global animationfolder, gifms, gifexwindow

    if animationfolder == None:
        animationfolder = filedialog.askdirectory(initialdir=pathlib.Path(__file__).parent.resolve(), title="Select folder with images")
    expgifname = filedialog.asksaveasfilename(initialdir = pathlib.Path(__file__).parent.resolve(), title = "", filetypes=[("GIF", ".gif")], defaultextension=".gif")

    gifms = int(gifms.get())

    frames = [Image.open(image) for image in glob.glob(f"{animationfolder}/*.PNG")] #FINALLY A SOLUTION THAT WORKED https://www.blog.pythonlibrary.org/2021/06/23/creating-an-animated-gif-with-python/ i love plagiarism
    frame_one = frames[0]
    frame_one.save(expgifname, format="GIF", append_images=frames,
               save_all=True, duration=gifms, loop=0)
    
    gifexwindow.destroy()

#generate()

def undo():
    global ids, idlist, exportlines, c
    
    c.delete(idlist[len(idlist)-1])
    idlist.pop()
    exportlines.pop()
    #moveExportObjDict(len(exportlines)) shouldnt be needed. leaving it here if neccessary 


    print(exportlines, type(exportlines))
    print(ids, idlist)

def deleteall():
    global exportlines

    if messagebox.askokcancel("Are you sure?", "This will delete your canvas forever", icon = 'warning') == False:
        print("cancelled deleteall")
    else:
        c.delete("all")
        exportlines.clear()

toolwindow = tkinter.Toplevel(win)
toolwindow.title("Toolbox")
toolwindow.resizable(False, False)
# toolwindow.iconbitmap(path_to_ico) #DOESNT WORK ON LINUX

def movetoolwin(e):
    x = win.winfo_x()
    y = win.winfo_y()

    toolwindow.geometry(f'{300}x{480}+{x-310}+{y}')


def canvaswidth():
    CANVAS_WIDTH = tkinter.simpledialog.askinteger("Change Canvas Size", "Enter Canvas WIDTH")
    CANVAS_HEIGHT = tkinter.simpledialog.askinteger("Change Canvas Size", "Enter Canvas HEIGHT")


    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    center_x = int(screen_width/2 - CANVAS_WIDTH / 2)
    center_y = int(screen_height/2 - CANVAS_HEIGHT / 2)
    win.geometry(f'{CANVAS_WIDTH}x{CANVAS_HEIGHT}+{center_x}+{center_y}')

    movetoolwin(e=0)

def initanimation():
    global animationfolder,frame

    
    animationfolder = filedialog.askdirectory(initialdir=pathlib.Path(__file__).parent.resolve(), title="Select where to store the animation frames")

    isanimationmodelabel.configure(text="Animation folder: \n"+animationfolder)
    
    frame = 0
    loadframe(0)
    

    
def unloadframe(frame):
    global exportlines

    if animationfolder == None:
        print("animationfolder == None")
        return
        

    if exportlines == []:
        return

    #runs a slightly modified version of exportpy and exportpng(). sure its gonna make things harder LATER, but its easier NOW


    print("cleared screen, on to writing")

    filename = f"{animationfolder}\{frame}.py"

    fp = open(filename, 'w')
    fp.write('#DrawTk Animation frame\n')
    fp.write('\nimport tkinter')
    fp.write(f'\nc = tkinter.Canvas(height={CANVAS_HEIGHT}, width={CANVAS_WIDTH})')
    fp.write('\nc.pack()\n')
    
    for x in exportlines:
        print(x)
        fp.write('\n'+x)

    fp.close()

    x=win.winfo_rootx()+c.winfo_x()
    y=win.winfo_rooty()+c.winfo_y()
    x1=x+c.winfo_width()
    y1=y+c.winfo_height()
    
    filename = f"{animationfolder}\{frame}.png"
    ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
    c.delete("all")
    exportlines.clear()

    print("done unloading")

    
def loadframe(frame):
    global ids, idlist, exportlines
    print(f"loading {frame}")

    if animationfolder == None:
        return

    if os.path.isfile(f"{animationfolder}\{frame}.py") == False:
        return

    fp = open(f"{animationfolder}\{frame}.py", 'r')

    i = 0
    
    for x in fp:
        i += 1

        if i > 6 and x != "tkinter.mainloop()":
            exec(x)
            exportlines.append(x)
            ids += 1
            idlist.append(ids)
    
    print(f"loaded {frame}")
    fp.close()

    

def changeframe(byhowmuch):
    global frame, framelabel

    print(f"changeframe {byhowmuch}")

    if animationfolder == None:
        print("SOMETHING WENT BIG WRONG; ANIMATION FOLDER NOT SPECIFIED")
        return
    
    #if frame + byhowmuch < 0:
        #return
    print(frame, byhowmuch)

    unloadframe(frame)
    frame = frame + byhowmuch
    loadframe(frame)

    framelabel.configure(text=f"Frame {frame}")

def changeframeminus():
    changeframe(-1)
def changeframeplus():
    changeframe(1)

win.bind('<Configure>', movetoolwin)

#lbl = tkinter.Label(toolwindow, text="I am in this toolwindow thing right").pack()

menu = tkinter.Menu(toolwindow)
toolwindow.configure(menu=menu)

filemenu = tkinter.Menu(menu)
filemenu.add_command(label="Load", command=load)
filemenu.add_separator()
filemenu.add_command(label="Save/Export to .py", command=exportpy)
filemenu.add_command(label="Export image", command=exportpng)
filemenu.add_command(label="Export animation as .gif", command=creategifexportwindow)
menu.add_cascade(label="File", menu=filemenu)

editmenu = tkinter.Menu(menu)
editmenu.add_command(label="Clear Canvas", command=deleteall)
editmenu.add_separator()
editmenu.add_command(label="Change Canvas Size", command=canvaswidth)
menu.add_cascade(label="Edit", menu=editmenu)

animationmenu =tkinter.Menu(menu)
animationmenu.add_command(label="Select Animation folder", command=initanimation)
menu.add_cascade(label="Animation", menu=animationmenu)

poslabel = tkinter.Label(toolwindow, text="", font="Roboto 14")
poslabel.pack()

topgrid = tkinter.Frame(toolwindow)
topgrid.pack()

undobutton = tkinter.Button(topgrid, text="Undo", command=undo, bg="light green").grid(row=1,column=0)
delobjbutton = tkinter.Button(topgrid, text="Delete object", command=modedelete, bg="#FFFFFF")
delobjbutton.grid(row=1, column=1)


toolgrid = tkinter.Frame(toolwindow)
toolgrid.pack()


toollabel = tkinter.Label(toolgrid, text="Tools", font="Roboto 14").grid(row=0, column=0, columnspan=3)
rectanglebutton = tkinter.Button(toolgrid, image=irectangle, command=moderectangle, bg="#BDBDBD")
rectanglebutton.grid(row=1, column=0)
ovalbutton = tkinter.Button(toolgrid, image=ioval, command=modeoval)
ovalbutton.grid(row=1, column=1)
linebutton = tkinter.Button(toolgrid, image=iline, command=modeline)
linebutton.grid(row=1, column=2)
ngonbutton = tkinter.Button(toolgrid, image=ingon, command=modengon)
ngonbutton.grid(row=2, column=1)
textbutton = tkinter.Button(toolgrid, image=itext, command=modetext)
textbutton.grid(row=2, column=2)

colgrid = tkinter.Frame(toolwindow)
colgrid.pack()

collabel = tkinter.Label(colgrid, text="Colors and thickness", font="Roboto 14").grid(row=0,column=0,columnspan=3)
colpickbut = tkinter.Button(colgrid, text="Fill Color", command=opencolorpick, bg=fillcolor)
colpickbut.grid(row=1, column=0)

filltransparentbut = tkinter.Button(colgrid, text="Fill Transparent (T)", command=togglefilltransparent, bg=("#BDBDBD"))
filltransparentbut.grid(row=1, column=1)

colpickbut2 = tkinter.Button(colgrid, text="Line Color", command=opencolorpick2, bg=linecolor, fg="white")
colpickbut2.grid(row=1, column=2)

thicc = tkinter.Scale(colgrid, from_=1, to=75, orient=HORIZONTAL, tickinterval=10, length=200, label="Line Width", resolution=5)
thicc.grid(row=2,column=0,columnspan=3)

snapp = tkinter.Scale(colgrid, from_=0, to=200, orient=HORIZONTAL, length=200, label="Snapping (0 to turn off)", resolution=5)
snapp.grid(row=3,column=0,columnspan=3)
snapp.set(roundto)

toollabel = tkinter.Label(toolwindow, text="Animation", font="Roboto 14").pack()

animationguiframe = tkinter.Frame(toolwindow)
animationguiframe.pack()

isanimationmodelabel = tkinter.Label(animationguiframe, text="ANIMATION MODE DISABLED\nto work with animation enable via Menu>Animation")
isanimationmodelabel.grid(row=0,column=0, columnspan=3)
frameprevbut = tkinter.Button(animationguiframe, text="<", command=changeframeminus).grid(row=1, column=0)
framelabel = tkinter.Label(animationguiframe, text="Frame 0")
framelabel.grid(row=1,column=1)
framenextbut = tkinter.Button(animationguiframe, text=">", command=changeframeplus).grid(row=1, column=2)


#selobjframe = tkinter.Frame(toolwindow)
#selobjframe.pack()

#selobjname = tkinter.Label(selobjframe, text="Select object to edit it")
#selobjname.pack()

melabel = tkinter.Label(toolwindow, text="Made by TobaT3", font="Roboto 8").pack(anchor="s")

win.mainloop()
toolwindow.mainloop()