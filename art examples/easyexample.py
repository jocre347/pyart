from tkinter import*

window = Tk()
CANVAS_WIDTH = 385
CANVAS_HEIGHT = 500
w = Canvas(window,
           width=CANVAS_WIDTH,
           height=CANVAS_HEIGHT)
w.pack()

RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"
YELLOW = "#FFFF00"
MAGENTA = "#FF00FF"
CYAN = "#00FFFF"
BLACK = "#000000"
WHITE = "#FFFFFF"

w.create_rectangle(0,0,CANVAS_WIDTH, CANVAS_HEIGHT, fill=WHITE)
w.create_rectangle(200,0,CANVAS_WIDTH, 185, fill=RED)
w.create_rectangle(195,0,200,CANVAS_HEIGHT,fill=BLACK)
w.create_rectangle(0,92,200,102,fill=BLACK)
w.create_rectangle(0,185,CANVAS_WIDTH,189,fill=BLACK)
w.create_rectangle(CANVAS_WIDTH-20,189,CANVAS_WIDTH-15,CANVAS_HEIGHT,fill=BLACK)

window.mainloop()
#this is a little example