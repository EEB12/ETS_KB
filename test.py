# from tkinter import *
# import tkinter as tk

# import subprocess

# def run():
#     result["text"]=subprocess.check_output(["python3","ai.py","03","BEST"])
    

# window = tk.Tk()
# window.title("Temperature Converter")
# window.resizable(width=False, height=False)
# # root = Tk()
# result = tk.Label(master=window)
# result.grid(row=0, column=2, padx=10)
# Button(window, text="Click to run 'ls -l'", command=run).pack()




import tkinter as tk
import subprocess
def run():
    
    
    result["text"]=subprocess.check_output(["python3","ai.py","03","BEST"])

# Set-up the window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)


# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Create the conversion Button and result display Label
btn_convert = tk.Button(
    window, text="execute ai.py'", command=run
)
result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Set-up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()

