from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import time

changeme = 10 # CAN BE CHANGED TO FIT THE TIMMINGS


# Create mouse and keyboard controller objects
mouse = MouseController()
keyboard = KeyboardController()

def perform_actions():

    keyboard.press(Key.alt_l)
    print('Left Alt key pressed')

    mouse.press(Button.right)
    time.sleep(1)
    mouse.release(Button.right)
    print('Right click')

    mouse.move(75, 0)
    print('Mouse moved by 50 pixels')

    mouse.press(Button.left)
    time.sleep(1)
    mouse.release(Button.left)    
    print('Left click')

    keyboard.release(Key.alt_l)
    print('Left Alt key released')

def main():
    time.sleep(5)
    print('GO!')

    try:
        while True:
            perform_actions()
            time.sleep(changeme)
    except KeyboardInterrupt:
        print("Script stopped by user")

if __name__ == "__main__":
    main()