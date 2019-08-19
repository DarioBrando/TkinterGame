import tkinter as tk
import random

def randompos (top):
    return random.randint(1, top-1)*step

master = tk.Tk()
step = 60
N_X = 10
N_Y = 10
canvas = tk.Canvas(master, bg = 'blue', height = step*N_X, width = step*N_Y)

player_pos = (randompos(N_X), randompos(N_Y))
exit_pos =(randompos(N_X), randompos(N_Y)) 

player = canvas.create_oval(player_pos, (player_pos[0]+step, player_pos[1]+step,), fill = 'green')

exit_g = canvas.create_oval(exit_pos, (exit_pos[0]+step, exit_pos[1]+step,), fill = 'yellow')

canvas.pack()
master.mainloop()
