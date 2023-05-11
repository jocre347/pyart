from tkinter import*
# Make a window with Canvas and Tkinter
window = Tk() #first you need to make a space where you can 'paint'
CANVAS_WIDTH = 385 #With these two variables you can change the height and width of the window.
CANVAS_HEIGHT = 500
w = Canvas(window,
           width=CANVAS_WIDTH,
           height=CANVAS_HEIGHT) #here the canvas is created you always need your window, the height and the width

#here comes the code

w.pack() #here you put your canvas on your window
#here comes the code
window.mainloop()# You need mainloop because otherwise you will only see your image for a very short time.
# This is the main build of your python code for canvas