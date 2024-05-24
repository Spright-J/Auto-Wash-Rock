from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import time

# Create mouse and keyboard controller objects
mouse = MouseController()
keyboard = KeyboardController()

# Function to perform the desired sequence of actions
def perform_actions():
    # Hold down the left alt key
    keyboard.press(Key.alt_l)
    print('Left Alt key pressed')

    # Right-click
    mouse.press(Button.right)
    time.sleep(1)
    mouse.release(Button.right)
    print('Right click')

    # Move the mouse by 50 pixels
    mouse.move(75, 0)
    print('Mouse moved by 50 pixels')

    # Left-click
    mouse.press(Button.left)
    time.sleep(1)
    mouse.release(Button.left)    
    print('Left click')

    # Release the left alt key
    keyboard.release(Key.alt_l)
    print('Left Alt key released')

# Run the actions every 10 seconds
time.sleep(5)
print('GO!')

try:
    while True:
        perform_actions()
        time.sleep(10)
except KeyboardInterrupt:
    print("Script stopped by user")
