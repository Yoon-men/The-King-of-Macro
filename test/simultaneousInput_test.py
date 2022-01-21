import keyboard
import time
import pyautogui

key = keyboard.read_hotkey(suppress=False)

simultaneousInputDetector = "+" in key

if simultaneousInputDetector == True : 
    key = key.split("+")
    print(key)
    print(len(key))

else : 
    print(key)
    print(len(key))

print("[system] 방금 입력한 키를 또 입력하고 싶다면 3초 이내로 Enter를 입력.")

timeOut = time.time() + 3
while time.time() <= timeOut : 
    if keyboard.is_pressed('Enter') : 
        pyautogui.press(key)
