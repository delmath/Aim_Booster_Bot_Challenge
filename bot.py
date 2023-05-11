import time
import pyautogui
import keyboard

print('Cliquer sur q pour arrêter le bot')
print('Veuillez cliquer dans le coin supérieur de la région de capture... (a pour valider)')

while True:
    if keyboard.is_pressed('q'):
        quit()
    if keyboard.is_pressed('a'):
        x1, y1 = pyautogui.position()
        break

print('Angle supérieur OK !')
time.sleep(1)
print('Veuillez cliquer dans le coin inférieur de la région de capture... (a pour valider)')

while True:
    if keyboard.is_pressed('q'):
        quit()
    if keyboard.is_pressed('a'):
        x2, y2 = pyautogui.position()
        break

print('Angle inférieur OK!')
print('Bot en cours d\'exécution dans 2s')
time.sleep(2)

while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    for x in range(0, pic.width, 5):
        for y in range(0, pic.height, 5):
            if pic.getpixel((x, y)) == (255, 219, 195):
                pyautogui.click(x + x1, y + y1)
                time.sleep(0.05)
                break
        else:
            continue
        break