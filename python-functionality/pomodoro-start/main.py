from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARKS = ""
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def resettimer():
    global REPS
    window.after_cancel(timer)
    timer_label.config(text= "Timer")
    canvas.itemconfig(timer_text, text=f'00:00')
    CHECKMARKS = ""
    check_label.config(text=CHECKMARKS)
    REPS = 0


    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def starttimer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        length = LONG_BREAK_MIN
        timer_label.config(text="Break", fg= RED)
    elif REPS % 2 == 0:
        length = SHORT_BREAK_MIN
        timer_label.config(text="Break", fg= PINK)
    else:
        length = WORK_MIN
        timer_label.config(text="Work", fg= GREEN)
    count = length *60
    count_down(count)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global CHECKMARKS
    minutes  = math.floor(count/60)
    seconds = count%60
    if seconds<10:
        seconds = f'0{seconds}'

    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count > 0:
        global timer
        timer = window.after(10,count_down, count-1)
    else:
        if REPS % 2 == 0:
            CHECKMARKS = CHECKMARKS+ "✔"
            check_label.config(text=CHECKMARKS)
        starttimer()
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas= Canvas(width=200, height= 224, bg= YELLOW, highlightthickness=0)
tomato_img =PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column = 2)



reset_button = Button(text="Reset", highlightthickness=0, borderwidth=0, bg=YELLOW, command=resettimer)
reset_button.grid(row=3, column=3)

start_button = Button(text="Start", highlightthickness=0, borderwidth=0, bg=YELLOW, command=starttimer)
start_button.grid(row=3, column=1)

timer_label = Label(text="Timer", fg=GREEN,bg= YELLOW, font=(FONT_NAME, 50))
timer_label.grid(row=1, column=2)

check_label = Label(text= CHECKMARKS, fg=GREEN, bg=YELLOW )
check_label.grid(row=4, column=2)

window.mainloop()