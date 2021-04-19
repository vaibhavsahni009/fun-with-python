import random
import time
from tkinter import Tk,Button,DISABLED

def show_symbol(x,y):
    global first,prex,prey
    buttons[x,y]['text']=button_symbols[x,y]
    buttons[x,y].update_idletasks()
    if first:
        prex = x
        prey = y
        first = False
    elif prex != x or prey != y:
        if buttons[prex,prey]['text'] != buttons[x,y]['text']:
            time.sleep(0.5)
            buttons[prex,prey]['text'] = ' '
            buttons[x,y]['text'] = ' '
        else:
            buttons[prex,prey]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
        first = True

win=Tk()
win.title('matchmaker')
win.resizable(width=False,height=False)
first=True
prex=0
prey=0

buttons = { }
button_symbols = { }
symbols = ['A','B','C','A','B','C',
            '1','2','3','1','2','3'
            ]

random.shuffle(symbols)

for x in range(6):
    for y in range(2):
        button = Button(command = lambda x=x , y=y: show_symbol(x,y) , width = 10, height = 8)
        button.grid(column = x , row = y)
        buttons[x,y] = button
        button_symbols[x,y] = symbols.pop()





win.mainloop()
