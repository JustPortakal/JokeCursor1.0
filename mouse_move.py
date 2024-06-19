import pyautogui
import time
import random

# Get the screen size
screen_width, screen_height = pyautogui.size()

# Move the mouse randomly for 100 seconds
timeout = time.time() + 100
while time.time() < timeout:
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    pyautogui.moveTo(x, y, duration=0.2)
