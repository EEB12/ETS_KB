import tkinter as tk
import os
import subprocess

root = tk.Tk()
root.geometry("640x480")
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

child_env = dict(os.environ)
child_env["SDL_WINDOWID"] = str(frame.winfo_id())
child_env["SDL_VIDEODRIVER"] = "windib"
p = subprocess.Popen(["cmd.exe"], env=child_env)

root.mainloop()