"Text Widget"

import tkinter as tk

root=tk.Tk()
root.title("Text widget")

txt= tk.Text(root,width=50,height=12,wrap="word")
txt.pack(padx=10,pady=10)
txt.insert("1.0","Line one\nLine two\n")

def show_text():
    content=txt.get("1.0",tk.END)
    print(repr(content.strip()))

tk.Button(root,text="Get Text",command=show_text).pack()
root.mainloop()
