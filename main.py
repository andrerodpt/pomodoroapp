from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 20
CHECK_MARK = '✔'
check_mark_text = ''
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps, check_mark_text
    window.after_cancel(timer)
    status_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    reps = 0
    check_mark_text = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)
    if reps % 8 == 0:
        reps = 0
        status_label.config(text='Break', fg=RED)
        countdown(long_break_sec)
    elif reps % 2 != 0:
        status_label.config(text='Work', fg=GREEN)
        countdown(work_sec)
    else:
        status_label.config(text='Break', fg=PINK)
        countdown(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global check_mark_text
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    formated_timer = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=formated_timer)
    if count >= 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start()
        if reps % 2 == 0:
            check_mark_text = check_mark_text + CHECK_MARK
            checkmarks_label.config(text=check_mark_text)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

status_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'normal'))
status_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, 'bold'))
canvas.grid(row=1, column=1)

button = Button(text="Start", command=start, highlightthickness=0)
button.grid(row=2, column=0)

button = Button(text="Reset", command=reset, highlightthickness=0)
button.grid(row=2, column=2)

checkmarks_label = Label(fg=GREEN, bg=YELLOW)
checkmarks_label.grid(row=3, column=1)

window.mainloop()

