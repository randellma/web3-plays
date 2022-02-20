#pip install pynput
import time
import random
from pynput.keyboard import Key, Controller
keyboard = Controller()

inputs = [Key.up, Key.left, Key.down, Key.right, 'x', 'z']

for i in range(10000):
    key = inputs[random.randrange(0, 5)]
    keyboard.press(key)
    time.sleep(0.2)
    keyboard.release(key)