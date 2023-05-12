from tkinter import*

window = Tk()
CANVAS_WIDTH = 100
CANVAS_HEIGHT = 100
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
w.create_line(0,0, 0,CANVAS_HEIGHT, fill=GREEN, width=1)
w.create_line(0,0,10,CANVAS_HEIGHT,fill=GREEN, width=1)
w.create_line(0,0,20,CANVAS_HEIGHT,fill=GREEN, width=1)
w.create_line(0,0,30,CANVAS_HEIGHT,fill=GREEN, width=1)
w.create_line(0,0,40,CANVAS_HEIGHT,fill=GREEN, width=1)
w.create_line(0,0,50,CANVAS_HEIGHT,fill=GREEN, width=1)
w.create_line(0,0,60,CANVAS_HEIGHT,fill=GREEN, width=1)
w.create_line(0,0,70,CANVAS_HEIGHT,fill=GREEN, width=1)
w.create_line(0,0,80,CANVAS_HEIGHT,fill=GREEN, width=1)
w.create_line(0,0,90,CANVAS_HEIGHT,fill=GREEN, width=1)
w.create_line(0,0,CANVAS_WIDTH,CANVAS_HEIGHT,fill=GREEN, width=1)

w.create_line(CANVAS_WIDTH,0,0,CANVAS_HEIGHT,fill=MAGENTA, width=1)
w.create_line(CANVAS_WIDTH,0, 10,CANVAS_HEIGHT, fill=MAGENTA, width=1)
w.create_line(CANVAS_WIDTH,0, 20,CANVAS_HEIGHT, fill=MAGENTA, width=1)
w.create_line(CANVAS_WIDTH,0, 30,CANVAS_HEIGHT, fill=MAGENTA, width=1)
w.create_line(CANVAS_WIDTH,0, 40,CANVAS_HEIGHT, fill=MAGENTA, width=1)
w.create_line(CANVAS_WIDTH,0, 50,CANVAS_HEIGHT, fill=MAGENTA, width=1)
w.create_line(CANVAS_WIDTH,0, 60,CANVAS_HEIGHT, fill=MAGENTA, width=1)
w.create_line(CANVAS_WIDTH,0, 70,CANVAS_HEIGHT, fill=MAGENTA, width=1)
w.create_line(CANVAS_WIDTH,0, 80,CANVAS_HEIGHT, fill=MAGENTA, width=1)
w.create_line(CANVAS_WIDTH,0, 90,CANVAS_HEIGHT, fill=MAGENTA, width=1)
w.create_line(CANVAS_WIDTH,0, 100,CANVAS_HEIGHT, fill=MAGENTA, width=1)
w.mainloop()