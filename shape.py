import tkinter as tk

root = tk.Tk()
root.geometry("500x500")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

canvas.create_rectangle(50, 50, 200, 200, fill="blue", outline="black")
canvas.create_line(0, 0, 400, 400, fill="red", width=5)
canvas.create_oval(220, 220, 350, 350, fill="yellow", outline="black")

print("Rectangle ID:", canvas.find_all())

root.mainloop()
