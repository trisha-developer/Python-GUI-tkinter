'''import tkinter as tk
m=tk.Tk()
m.title("Calculator")
m.geometry("500x300")
m.
m.mainloop()
'''

'''import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Labels")
lbl= tk.Label(root,
              text="Welcome to  Tkinter",
              font=("Arial",16,"bold"),
              fg="white",
              bg="#1F4E79",
              padx=20,pady=10)
lbl.pack(fill="x",padx=10,pady=10)
info = tk.Label(root,text="This is a long line of the text that wrape automatically inside label.",
                wraplength=300,justify="left")
info.pack(padx=10)
root.mainloop()

def on_close():
    if messagebox.askokcancel("Quit","Do you really want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW",on_close)
root.mainloop()'''

