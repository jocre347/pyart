# In part 2 we will look for simplification in part 1
from tkinter import*

window = Tk()
CANVAS_WIDTH = 385
CANVAS_HEIGHT = 500
w = Canvas(window,
           width=CANVAS_WIDTH,
           height=CANVAS_HEIGHT)
w.pack()

#first we are going to make some color constans that we will never ever need to write those color codes
RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"
YELLOW = "#FFFF00"
MAGENTA = "#FF00FF"
CYAN = "#00FFFF"
BLACK = "#000000"
WHITE = "#FFFFFF"

# this are some color when you want to make other color you can google them or something else