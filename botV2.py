from tkinter import *
from pyautogui import *
import pyautogui
import time
import keyboard

def click_a():
    global x1, y1
    while True:
        if keyboard.is_pressed('a'):
            x1, y1 = position()
            coord1.config(text=f"x ; y : ({x1}) ; ({y1})")
            break
    angle1.config(relief=SUNKEN)
    angle2.config(relief=RAISED)

def click_b():
    global x2, y2
    while True:
        if keyboard.is_pressed('z'):
            x2, y2 = position()
            coord2.config(text=f"x ; y : ({x2}) ; ({y2})")
            break
    angle1.config(relief=RAISED)
    angle2.config(relief=SUNKEN)

def run_bot():
    while keyboard.is_pressed('p') == False:
        pic = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
        for x in range(0, pic.width, 5):
            for y in range(0, pic.height, 5):
                if pic.getpixel((x, y)) == (255, 219, 195):
                    click(x+x1, y+y1)
                    time.sleep(0.05)
                    break
            else:
                continue
            break

window = Tk()
window.resizable(0, 0)
window.wm_attributes("-topmost", 1)
window.geometry("500x150")
window.title("Bot AimBooster")

frame1 = Frame(window)
frame1.pack(side=TOP, pady=10)

angle1 = Button(frame1, text="Coin supérieur", command=click_a, relief=RAISED, width=15)
angle1.pack(side=LEFT, padx=10)

coord1 = Label(frame1, text="x ; y : (0) ; (0)")
coord1.pack(side=LEFT)

angle2 = Button(frame1, text="Coin inférieur", command=click_b, relief=RAISED, width=15)
angle2.pack(side=LEFT, padx=10)

coord2 = Label(frame1, text="x ; y : (0) ; (0)")
coord2.pack(side=LEFT)

run = Button(window, text="Lancer le bot", command=run_bot, bg='green', fg='white', width=20)
run.pack(pady=20)

quit_btn = Button(window, text="Quitter", command=quit, bg='red', fg='white', width=10)
quit_btn.pack(side=BOTTOM, pady=5)

window.mainloop()