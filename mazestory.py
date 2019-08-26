import tkinter as tk
import random

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange','White', 'Purple', 'Brown']

score = 0

timeleft = 30

def newgame(event):
    if timeleft == 30:
        countdown()
    nextColour()

def nxtclr():
    global score
    global timeleft
    if timeleft>0:
        sys.exit
        print('Серьезно? -_-') or ('Нормально же шли :(') or ('Все с тобой ясно')


    



