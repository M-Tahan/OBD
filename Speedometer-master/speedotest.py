import random
from turtle import position
from urllib import response
import speedometer
from tkinter import *

import testoop
import OBD
root=Tk()
canvas=Canvas(root,height=600,width=600)
canvas.pack()
canvas.create_oval(0,0,600,600,tag="oval")
speedText = canvas.create_text(330,350,text="Km/h",font=("Courier",20))
speed = canvas.create_text(270,350,font=("Courier",20))
rpmText = canvas.create_text(325,400,text="RPM x1000",font=("Courier",20))
rpm = canvas.create_text(275,400,font=("Courier",20))
A=speedometer.Speedometer(canvas,"oval",Range=(0,200))
obdVar = OBD.OBDvar()

def updateS():
        
    f= obdVar.speedResults()
    x= obdVar.rpmResults()
    canvas.itemconfig(speed, text = str(f))
    canvas.itemconfig(rpm, text = str(x))
    A.moveto(f, "oval")
    
    root.after(200, updateS)

#A.moveto(5,"oval")
A.changerange(Range=(0,220),rfont=("Verdana",10))

updateS()

root.mainloop()
