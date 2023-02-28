from time import *
from tkinter import *
window= Tk()
window.title("clock")
window.config(bg="green")
clock=Frame(bg="green")
clock.pack(side=TOP)
def update():
    time=strftime("%I:%M:%S %p")
    timelabel.config(text=time)
    timelabel.after(1000,update) 
timelabel=Label(clock,font=("digital-7",50),bg="green")
update()
date=strftime("%x")
Label(clock,text=date,font=("digital-7",20),bg="green").pack(side=BOTTOM)
timelabel.pack()
window.mainloop()