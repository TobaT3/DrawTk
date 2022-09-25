# DrawTk
Make pngs and .py files with drawings made in a visual editor

(I might have changed the repo name a bunch of times upon discovering how many repos were called TkPaint...)


**If you have any ideas or experience any problems, please open an Issue**

# Usage
## Download
1. Clone the repository (or just download main.py) somewhere on your computer.
2. Run the file!

Make sure you have installed python 3.10, tkinter (should come installed with python) and pillow.
If running it doesnt work, try opening it in IDLE and running it that way.

## Drawing

![image](https://user-images.githubusercontent.com/67913859/192092488-399e35cd-6f98-4153-8930-e97a2d4231b4.png)

Select one of the tools from the toolbox. Then just click on the canvas, pretty self explanatory. Adjust fill color and line color with the fill color and line color buttons (make sure you toggle fill transparent off if you want to use a fill color). You can also adjust line width and snapping. If you screw anything up, use the undo button.

## Exporting

### .py

**Keep in mind that exporting will overwrite the previously generated file. If you dont want to lose a previously generated file, before you run another export operation move or rename the existing tkinter_drawing.py file (same goes for the .png files)**

Click on the export to .py button. export to .py generates a python file like the one below in the directory where the main python file is located (named tkinter_drawing.py). Simply run it and you should see your image.

Example tkinter_drawing.py file:

    #Made in TkPaint by TobaT3

    import tkinter
    c = tkinter.Canvas(height=500, width=700)
    c.pack()

    c.create_rectangle(100,100,350,300,fill='', outline='#000000')
    c.create_oval(350,350,550,150,fill='', outline='#000000')
    c.create_oval(200,400,550,100,fill='#ffffff', outline='#000000')
    c.create_rectangle(250,300,500,500,fill='#ffffff', outline='#000000')
    c.create_polygon(210,300,375,210,525,300, fill='#ffffff',outline='#000000')
    c.create_rectangle(350,500,400,425,fill='', outline='#000000')
    c.create_rectangle(275,425,325,475,fill='', outline='#000000')
    c.create_rectangle(425,425,475,475,fill='', outline='#000000')
    c.create_rectangle(275,325,325,375,fill='', outline='#000000')
    c.create_rectangle(425,325,475,375,fill='', outline='#000000')
    c.create_rectangle(350,325,400,375,fill='', outline='#000000')
    c.create_rectangle(275,325,325,375,fill='#80ffff', outline='#000000')
    c.create_rectangle(350,325,400,375,fill='#80ffff', outline='#000000')
    c.create_rectangle(425,325,475,375,fill='#80ffff', outline='#000000')
    c.create_rectangle(425,425,475,475,fill='#80ffff', outline='#000000')
    c.create_rectangle(275,425,325,475,fill='#80ffff', outline='#000000')
    c.create_rectangle(350,425,400,500,fill='#804040', outline='#000000')
    c.create_oval(398,461,389,468,fill='#000000', outline='#000000')
    c.create_line(350,350,400,350, fill='#000000')
    c.create_line(375,325,375,375, fill='#000000')
    c.create_line(450,325,450,375, fill='#000000')
    c.create_line(425,350,475,350, fill='#000000')
    c.create_line(450,425,450,475, fill='#000000')
    c.create_line(425,450,475,450, fill='#000000')
    c.create_line(275,450,325,450, fill='#000000')
    c.create_line(300,425,300,475, fill='#000000')
    c.create_line(300,375,300,325, fill='#000000')
    c.create_line(325,350,275,350, fill='#000000')
    
### .png

**Keep in mind that exporting will overwrite the previously generated file. If you dont want to lose a previously generated file, before you run another export operation move or rename the existing tkinter_drawing.png file (same goes for the .py files)**

Click on the export to .png button. A file named tkinter_drawing.png should pop up in the directory where the main.py file is located. Open it in whatever program you want!

## Thanks to:

My stupid friend who made (and as i write this is still making) a program that is essentially the same thing (contrary to his belief, my program is actually better).

B.Jenkins on stack overflow for https://stackoverflow.com/a/38645917/15888488 (yes its like 6 years old but it still works)

And of course all the creators of python and pillow
