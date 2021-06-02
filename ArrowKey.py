from tkinter import *

root = Tk()

text = ''
def key(event):
    global text
    text+= event.char
    print("pressed", text)

def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()