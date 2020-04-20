from tkinter import *
from Segment import *

LENGTH = 30
NUMBER = 20

pen = Tk()

canvas = Canvas(pen, width=700, height=500, bg='black')
canvas.pack(expand=1, fill='both')

mouse = Vector(300, 300)
canvas.bind("<Motion>", lambda event: mouse.set(event.x, event.y))

current  = Segment((250, 250), LENGTH)
current.follow(320, 200)
current.show(canvas)

for i in range(NUMBER):
    parent = Segment(current, LENGTH)
    parent.show(canvas)
    current = parent


try:
    while True:
        canvas.delete('all')
        head = current
        current.follow(mouse.x, mouse.y)
        current.show(canvas)

        while current.child:
            next = current.child
            next.follow(current)
            next.show(canvas)
            current = next

        current = head
        pen.update()

except:
    print("exit")

pen.mainloop()