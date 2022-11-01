# DrawTk
Make pngs and .py files with drawings made in a visual editor

(I might have changed the repo name a bunch of times upon discovering how many repos were called TkPaint...)

**Please note, this is a project made mostly for fun, most of the versions contain some bugs, i will try my best to fix them if you open an issue, but this isnt some amazingly polished application.**

**If you have any ideas, problems or just a question, please open an Issue**

# Usage
## Download

1. Either download the latest release .exe or .py file, or clone this repo
2. Run the file!

If you cloned the repo and it doesn't work, make sure you are running the code with Python 3.10 (ideally 3.10.4) and have installed pillow and tkfontchooser:

    pip install pillow, tkfontchooser

## Drawing

![test](https://user-images.githubusercontent.com/67913859/199307071-de06ceae-b8e3-4af8-9050-013948a1453f.png)

Select one of the tools from the toolbox. Then just click on the canvas, pretty self explanatory. Adjust fill color and line color with the fill color and line color buttons (make sure you toggle fill transparent off if you want to use a fill color). You can also adjust line width and snapping. If you screw anything up, use the undo button.

## Exporting

### .py

**Keep in mind that exporting will overwrite the previously generated file. If you dont want to lose a previously generated file, before you run another export operation move or rename the existing tkinter_drawing.py file (same goes for the .png files)**

In the top menu in the toolbox, click on File > Save/Export to .py. Select where you want the file to be saved and what it should be called. Then run the .py file and you should see your image; you can modify it too.

Example tkinter_drawing.py file:

    #If you want to load this file make sure lines 1-6 are not modified

    import tkinter
    c = tkinter.Canvas(height=500, width=700)
    c.pack()

    c.create_rectangle(50,50,450,450, width=1,fill='#617dfe', outline='#000000')
    c.create_polygon([60, 60, 60, 440, 440, 440], fill='#617dfe', outline='#000000', width=11)
    c.create_rectangle(440,60,280,220, width=11,fill='#617dfe', outline='#ffffff')
    tkinter.mainloop()
    #Made in DrawTk by TobaT3
    
### Image

**Keep in mind that exporting will overwrite the previously generated file. If you dont want to lose a previously generated file, before you run another export operation move or rename the existing tkinter_drawing.png file (same goes for the .py files)**

In the top menu in the toolbox, click on File > Export image. Select where you want the file to be saved and what it should be called. Open it in whatever program you want!

Supported image types are .png, .jpeg, .tiff and .bmp

## Thanks to:

My stupid friend who made (and as i write this is still making) a program that is essentially the same thing (contrary to his belief, my program is actually better).

B.Jenkins on stack overflow for https://stackoverflow.com/a/38645917/15888488 (yes its like 6 years old but it still works) plus some other people on stack overflow

And of course all the creators of python and pillow
