import tkinter as tk
import random

def randompos (top):
    return random.randint(1, top-1)*step

master = tk.Tk()
step = 60
N_X = 10
N_Y = 10
canvas = tk.Canvas(master, bg = 'green', height = step*N_X, width = step*N_Y)

player_pos = (randompos(N_X), randompos(N_Y))
exit_pos =(randompos(N_X), randompos(N_Y)) 
