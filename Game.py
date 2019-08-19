import tkinter as tk
import random

class Player():

    def __init__(this, color):
        this.x = this.randompos(N_X)
        this.y = this.randompos(N_Y)
        this.color = color

    def draw(this):
        canvas.create_oval((this.x, this.y),(this.x+step, this.y+step), fill=this.color)
            
        
    def randompos (this, top):
        return random.randint(1, top-1)*step

master = tk.Tk()
step = 60
N_X = 10
N_Y = 10
canvas = tk.Canvas(master, bg = '#FF6347', height = step*N_X, width = step*N_Y)

player = Player('#FFDAB9')
player.draw();
exit_g = Player('#800000')
exit_g.draw()


canvas.pack()
master.mainloop()
