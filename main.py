import wakeup_word
import sr
import generate_code
import pyautogui
import time
from playsound import playsound


while True:
    if wakeup_word.check():
        try:
            text = sr.start()
            print("You : ", text)
            code = generate_code.get(text)
            print(code)
            for c in code.split("\n"):
                try:
                    exec(c)
                except:
                    continue
        except:
            playsound("error.mp3")
