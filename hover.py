import pyautogui
import time

try:
    print("Mouse hover started. Press Ctrl+C to stop.")
    while True:
        pyautogui.moveRel(20, 0, duration=0.2)
        pyautogui.moveRel(0, 20, duration=0.2)
        pyautogui.moveRel(-20, 0, duration=0.2)
        pyautogui.moveRel(0, -20, duration=0.2)
        time.sleep(5)
except KeyboardInterrupt:
    print("Mouse hover stopped.")
