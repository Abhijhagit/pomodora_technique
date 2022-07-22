from cgitb import text
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timers=None

def nothing(count):
    count_min= math.floor(count/60)
    count_sec= count % 60
    hello.itemconfig(new_cnava,text=f"{count_min}:{count_sec}")
    label.config(text="Start")
    if count>0:
     global timers
     timers=window.after(1000,nothing,count-1)
   


def timecount():
   nothing(120)
     
def timeend():
    window.after_cancel(timers)
    hello.itemconfig(new_cnava,text="00:00")
    label.config(text="Rest")


window=Tk()
window.title("Tomato Timer")
window.config(background=GREEN ,padx=100,pady=50)

# print(nothing)
# nothing(5)

 

label = Label(text="Timer" ,font=(FONT_NAME,20))
# label.config(text="Result" ,font=("Arial", 25))
label.grid(column=1,row=0)



hello=Canvas(width=300,height=300,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
hello.create_image(150, 130,image=tomato)
new_cnava=hello.create_text(145,150,text="00:00", fill="white" ,font=('Helvetica 15 bold'))
hello.grid(column=1,row=1)


button1=Button(text="Start",font=(FONT_NAME,20),highlightthickness=0,command=timecount)
button1.grid(column=0,row=2)


button2=Button(text="Reset",font=(FONT_NAME,20),highlightthickness=0,command=timeend)
button2.grid(column=2,row=2)



# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window.mainloop()