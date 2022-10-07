from email.mime import image
from tkinter import *
import math
from urllib import response

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30

# ------- countdown mechanism ----- #
reps = 0
timer = None

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    lb_timer="Timer"
    global reps
    reps=0
    lb_done.config(text="")

def start_timer():
    global reps
    reps += 1
    print(reps)
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        lb_timer.config(text="Long Break", fg=GREEN)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        lb_timer.config(text="Short Break", fg=PINK)
    else:
        count_down(WORK_MIN*60)
        lb_timer.config(text="WORK Time", fg=RED)



def count_down(count):
    global reps
    count_min = math.floor( count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec=f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(10, count_down, count -1)
    else:
        start_timer()
        work_sessions = math.floor(reps / 2)
        print(work_sessions)
        
        marks = ""
        for _ in range(work_sessions):
            marks+= "✔"
        lb_done.config(text=marks)
        print(marks)


# -----  UI SETUP -------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

def say_something(thing):
    print(thing)



lb_timer = Label(fg=GREEN,text="Timer",font=(FONT_NAME,45,"bold"), bg=YELLOW)
lb_timer.grid(column=1,row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1,row=1)
tomoto_img = PhotoImage(file="pomodoro_app/tomato.png")
canvas.create_image(100,112, image= tomoto_img)
timer_text = canvas.create_text(100,130, text="00:00", font=(FONT_NAME,35,"bold"))

start = Button(text="Start",command=start_timer,highlightthickness=0 )
start.grid(column=0,row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2,row=2)

lb_done = Label(fg=GREEN, bg=YELLOW,text="")
lb_done.grid(column=1,row=3)

window.mainloop()