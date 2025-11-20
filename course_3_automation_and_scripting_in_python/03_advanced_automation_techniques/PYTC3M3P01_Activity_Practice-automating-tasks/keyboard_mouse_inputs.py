import schedule
import pyautogui as py
import time

# simulate mouse click
py.click()

# simulate mouse click at location x=400, y=400
# note (0, 0) is top left corner, and (x, y) are in pixels
py.click(400, 400)

# simulate a right click, then wait 2 seconds, then left click
py.click(button='right')
time.sleep(2)
py.click(button='left')

# simulate a right click at middle point of your screen
screen_width, screen_height = py.size()
py.click(button='left', x=screen_width//2, y=screen_height//2)

# simulate keyboard entries
py.typewrite("Hello") # this types out the word 'Hello' as if you would type it on your keyboard

# simulate single keyboard presses
py.press('enter')
py.press('esc')
py.press('ctrl')

py.press('p')

# take 10 seconds for cursor to arrive in middle of your screen and then double left click when you get there
py.doubleClick(x=screen_width//2, y=screen_height//2, button='left', duration=10)