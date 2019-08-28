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
def ship_move(event):
    if event.keysym == 'Up': #вверх
        c.move(ship, 0, -ship_spd)
        c.move(ship1, 0, -ship_sdp)
    elif event.keysym == 'Down':#вниз
        c.move(ship, 0, ship_spd)
        c.move(ship1, 0, ship_spd)
    elif event.keysym == 'Left':#влево
        c.move(ship, -ship_spd, 0)
        c.move(ship1, -ship_spd, 0)
    elif event.keysym == 'c'+'h'+'e'+'a'+'t':#чит
        score += 10000
c.bind_all('<Key>', move_ship)
    
        
    

