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
reps = 0
timer = ""
timer_running = False


def lift_window():
    window.attributes('-topmost', True)
    window.update_idletasks()  # get window on top
    window.attributes('-topmost', False)  # prevent permanent focus
    window.focus_force()  # focus to the window


def start_button_clicked():
    # This function prevents multiple timers to start when the start button is clicked multiple times
    global timer_running
    if not timer_running:
        timer_running = True
        start_timer()


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps, timer_running
    reps = 0
    timer_running = False


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep:
    if reps % 8 == 0:
        lift_window()
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    # If it's the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        lift_window()
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    # If it's the 1st/3rd/5th/7th rep:
    else:
        lift_window()
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_button_clicked, highlightbackground=YELLOW)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 44), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

check_marks = Label(bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)

window.mainloop()

