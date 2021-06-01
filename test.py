from tkinter import *
import subprocess

def run():
    subprocess.run(["python3", "ai.py", "03", "BEST"])

root = Tk()
Button(root, text="Click to run 'ls'", command=run).pack()
root.mainloop()

