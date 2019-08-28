from tkinter import *
from math import sqrt
from random import shuffle
window = Tk()
colors = ['blue', 'green', 'pink', 'purple', 'black', 'blue',]
health = {'ammount': 3,'color':'green'}
window.title('Bubble Game')
c = Canvas(window, height = 768, width = 1366, bg = 'skyblue')
c.pack()
ship = c.create_polygon(5, 5, 5, 25, 30, 15, fill='green')
ship1 = c.create_oval(0, 0, 30, 30, outline = 'red')
SHIP_R = 15
c.move(ship, 683, 384)
c.move(ship1, 683, 384)
ship_spd = 10
score = 0
def ship_move()


