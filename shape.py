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

"""
import tkinter as tk

root = tk.Tk()
root.title("Bouncing Ball")

W, H, R = 400, 300, 15
canvas = tk.Canvas(root, width=W, height=H, bg="black")
canvas.pack()

ball = canvas.create_oval(50, 50, 50 + 2 * R, 50 + 2 * R, fill="yellow", outline="")
dx, dy = 4, 3

def animate():
    global dx, dy
    canvas.move(ball, dx, dy)
    x1, y1, x2, y2 = canvas.coords(ball)
    if x1 <= 0 or x2 >= W:
        dx = -dx
    if y1 <= 0 or y2 >= H:
        dy = -dy
    root.after(20, animate)

animate()

"""
