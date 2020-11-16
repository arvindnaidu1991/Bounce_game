from tkinter import *
import random
import time
from datetime import datetime

class Paddle:
    def __init__ (self,canvas):
        self.canvas = canvas
        canvas.bind_all('<KeyPress-Left>', self.movepaddle)
        canvas.bind_all('<KeyPress-Right>', self.movepaddle)
        self.id= canvas.create_rectangle(31,364,291,391,fill="Black")
        print(self.id)

    def movepaddle(self,event):
        if event.keysym == 'Left':
            canvas.move(1, -5, 0)
        else:
            canvas.move(1, 5, 0)






class Ball:
    def __init__(self, canvas, color,paddle):
        self.paddle=paddle
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 50, 50, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        #print(pos)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            return False
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        if self.hit_paddle(pos) == True:
            self.y= -3








tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
paddle=Paddle(canvas)
ball = Ball(canvas, 'red',paddle)
ball2=Ball(canvas,"Blue",paddle)


start_time = datetime.now()
ID=canvas.create_text(220, 300, text="Time",font=("Courier", 30))

def restart():
    canvas.coords(ball.id,10,10,50,50)
    canvas.coords(ball2.id,10,10,50,50)




btn = Button(tk, text="Restart", command=restart)
btn.pack()
while 1:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.02)
    if ball.draw()!= False and ball2.draw()!= False:

        end_time = datetime.now()
        a = "time: " + str((end_time.second - start_time.second))
        canvas.itemconfig(ID, text=a)

    else:
        canvas.itemconfig(ID, text=a)






    



