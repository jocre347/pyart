# In part 1 we will lear what we can create 
from tkinter import*

window = Tk()
CANVAS_WIDTH = 385
CANVAS_HEIGHT = 500
w = Canvas(window,
           width=CANVAS_WIDTH,
           height=CANVAS_HEIGHT)
w.pack()
# the first thing is a rectangle 
w.create_rectangle(0,0,CANVAS_WIDTH, CANVAS_HEIGHT, fill="#ffffff")
# first we write w for the canvas. Then what we are going to create. The 0,0 is the point at the top left of the window 
# and the two variables are the point at the bottom right these two points must always be specified and fill is the color

#the next is the arc 
coord = 100, 50, 320, 370 
arc = w.create_arc(coord, start=0, extent=90, fill="black")
# so for an arc you need the same type of points as for an rectangle but here you can say how mucht of an circle you need
# and in all creations you can use names for the colors

#the next is the polygon
#because there aren't funktions to create triangles or other things you need to make them from scratch
points = 120, 450, 210, 450, 210, 370
w.create_polygon(points, outline=None, fill="yellow")
# here we have more than two points because this is a triangle and  ther is another parameter called outline this works
# also in the other funktions

#the next is the line
w.create_line(0, 0, 50, 20, fill="red", width=3)
#there we have again lots of points and a filling but we have also a widht of the line where you can chose how wide your line is

window.mainloop()