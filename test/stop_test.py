import keyboard
from threading import Thread
import time

runNum = int(input("[system] 장풍을 몇 번 날릴까요? : "))

detect = False

def detector() : 
    global detect
    while True : 
        if keyboard.is_pressed("ESC") : 
            print("[감지의 정령 케인인] 얘! ESC를 눌렀으니 죽어버리렴!")
            detect = True
            break


def main() : 
    global detect
    for i in range(runNum) : 
        print("\"나는! 장풍을 했다!\"")
        if detect == True : 
            break

mainThread = Thread(target = main)
detectThread = Thread(target = detector)

mainThread.start()
detectThread.start()