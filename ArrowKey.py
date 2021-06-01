# KeyLogger_tk2.py
# show a character key when pressed without using Enter key
# hide the Tkinter GUI window, only console shows

import tkinter as tk

a = 1

def key(event, arg):
    """shows key or tk code for the key"""
    if event.keysym == 'Escape':
        root.destroy()
    if event.char == event.keysym:
        # normal number and letter characterxads
        print( arg, 'Normal Key %r' % event.char )
    elif len(event.char) == 1:
        # charcters like []/.,><#$ also Return and ctrl/key
        print( arg, 'Punctuation Key %r (%r)' % (event.keysym, event.char) )
    else:
        # f1 to f12, shift keys, caps lock, Home, End, Delete ...
        print( arg, 'Special Key %r' % event.keysym )

root = tk.Tk()
print( "Press a key (Escape key to exit):" )
root.bind_all('<Key>', lambda event, arg=2: key(event, arg))
# don't show the tk window
root.withdraw()
root.mainloop()