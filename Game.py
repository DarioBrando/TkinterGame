import tkinter as tk
import random

class Player():

    def __init__(this, color):
        this.x = this.randompos(N_X)
        this.y = this.randompos(N_Y)
        this.color = color

    def draw(this):
        this.body = canvas.create_oval((this.x, this.y),(this.x+step, this.y+step), fill=this.color)
            
        
    def randompos (this, top):
        return random.randint(1, top-1)*step

    def repaint(this, x, y):
        canvas.move(this.body, x, y)

    def checkPos(this, other):
        return this.x == other.x and this.y == other.y
    

def keyPress(event):
    print(event)
    if event.keycode == 37:
        player.x -= step
        player.repaint(-step, 0)
    elif event.keycode == 38:
        player.y -= step
        player.repaint(0, -step) 
    elif event.keycode == 39:
        player.x += step
        player.repaint(step, 0)
    elif event.keycode == 40:
        player.y += step
        player.repaint(0, step)
    endGame() 

def endGame():
    if player.checkPos(exit_g):
        print('Game over')
        print('u won!!')
    
master = tk.Tk()
step = 60
N_X = 10
N_Y = 10
canvas = tk.Canvas(master, bg = '#FF6347', height = step*N_X, width = step*N_Y)

player = Player('#FFDAB9')
player.draw();
exit_g = Player('#810000')
exit_g.draw()


canvas.pack()
master.bind('<KeyPress>', keyPress)
master.mainloop()
