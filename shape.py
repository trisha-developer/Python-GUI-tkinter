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
#moving objects with the mouse(drag and drop)
"""
import tkinter as tk
root= tk.Tk()
root.title("Drag a circle")

canvas = tk.Canvas(root,width=500,height=350,bg="#fff")
canvas.pack()

ball= canvas.create_oval(200,130,260,190,fill="tomato",outline="")
drag={"x":0,"y":0}

def start_drag(event):
    drag["x"],drag["y"]=event.x,event.y

def do_drag(event):
    dx=event.x -drag["x"]
    dy=event.y -drag["y"]
    canvas.move(ball,dx,dy)
    drag["x"],drag["y"]=event.x,event.y

canvas.tag_bind(ball,"<ButtonPress-1>",start_drag)
canvas.tag_bind(ball,"<B1-Motion>",do_drag)

root.mainloop()"""
