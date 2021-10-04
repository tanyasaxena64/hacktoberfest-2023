from tkinter import *
import random

top = Tk()
top.geometry("300x300")

l_wc = Label(top,text = "Welcome to Pairs Game")
l_wc.pack()


f_game = Frame(top)
f_game.pack()

flag = 0
temp = (0,0)
def playGame(b):
    global flag
    global temp
    if flag == 0:
        buttons[b]['bg'] = 'yellow'
        temp = b
        flag = 1
    else:
        buttons[b]['bg'] = 'yellow'
        if buttons[b]["text"] != buttons[temp]["text"]:
            buttons[b]["bg"]= "green"
            buttons[temp]["bg"]= "green"
        flag = 0
            

def createButtons():
    (x1,y1) = (random.randint(1,4),random.randint(1,4))
    b1 = (x1,y1)
    (x2,y2) = (random.randint(1,4),random.randint(1,4))
    b2 = (x2,y2)
    if b1 in buttons.keys() or b2 in buttons.keys() or b1 == b2:
        createButtons()
    else:
        buttons[b1] = Button(f_game,text = txt,bg='green',fg='green',command = lambda :playGame(b1))
        buttons[b1].grid(row=x1,column = y1)
        buttons[b2] = Button(f_game,text = txt,bg='green',fg='green',command = lambda:playGame(b2))
        buttons[b2].grid(row=x2,column = y2)
        
        
    

buttons ={}
txt = 0
for i in range(1,9):
    txt = i
    createButtons()

top.mainloop()