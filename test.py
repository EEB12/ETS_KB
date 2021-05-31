from tkinter import *
import subprocess

def run():
    subprocess.run(["python3", "-l"])

root = Tk()
Button(root, text="Click to run 'ls -l'", command=run).pack()
root.mainloop()