from tkinter import *
from math import sqrt
from random import shuffle
from random import randint
from time import sleep, time

window = Tk()
colors = ['blue', 'green', 'pink', 'purple', 'black',]
health = {'ammount': 3,'color':'green'}

window.title('Bubble Game')

c = Canvas(window, height = 768, width = 1366, bg = 'skyblue')
c.pack()
ship = c.create_polygon(5, 5, 5, 25, 30, 15, fill='green')
ship1 = c.create_oval(0, 0, 30, 30, outline = 'red')
SHIP_R = 15
c.move(ship, 683, 384)
c.move(ship1, 683, 384)
ship_spd = 20

score = 0

def ship_move(event):
    if event.keysym == 'Up': #вверх
        c.move(ship, 0, -ship_spd)
        c.move(ship1, 0, -ship_spd)
    elif event.keysym == 'Down':#вниз
        c.move(ship, 0, ship_spd)
        c.move(ship1, 0, ship_spd)
    elif event.keysym == 'Left':#влево
        c.move(ship, -ship_spd, 0)
        c.move(ship1, -ship_spd, 0)
    elif event.keysym == 'Right':#вправо
        c.move(ship, ship_spd, 0)
        c.move(ship1, ship_spd, 0)
    elif event.keysym == 'c':#чит
        score += 10000
c.bind_all('<Key>', ship_move)

bub_id = list()
bub_r = list()
bub_speed = list()
bub_id1 = list()
bub_r1 = list()
bub_speed1 = list()
min_bub_r = 13
max_bub_r = 32
max_bub_spd = 12

def new_bubble():
    x = 1366 + 100
    y = randint(0, 768)
    r = randint(min_bub_r, max_bub_r)
    id1 = c.create_oval(x-r, y-r, x+r, y+r, outline='white', fill = 'lightblue')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(6, max_bub_spd))
    
def new_bubble1():
    x = 1366 + 100
    y = randint(0, 768)
    r = randint(min_bub_r, max_bub_r)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline = 'black', fill = 'red')
    bub_id1.append(id1)
    bub_r1.append(r)
    bub_speed1.append(randint(7, max_bub_spd))
    
def new_bubble_r():
    x = 1366 + 100
    y = randint(0, 768)
    r = randint(min_bub_r, max_bub_r)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline = 'white', fill=colors[0])
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(7, max_bub_spd))
    
def moving():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[i], 0)
    for i in range(len(bub_id1)):
        c.move(bub_id1[i], -bub_speed1[i], 0)

bub_chance = 40

def coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y

def minusbubble(i):
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]

def clean():
    for i in range(len(bub_id) -1, -1, -1):
        x, y = coords(bub_id[i])
        if x < -100:
            minusbubble(i)

def distance(id1, id2):
    x1, y1 = coords(id1)
    x2, y2 = coords(id2)
              

    
    
    
    



    
        
    

