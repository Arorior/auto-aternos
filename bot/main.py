import os
import platform
import plyer
import pyautogui

language = open('Languages', 'r').readlines()
button = None
lang_inside = None
title = None
message = None
start = input("ru/eng?\n").lower()

def main():
    if input() == "start":
        if lang_inside == "ru":
            print(language[2].strip())
        elif lang_inside == "eng":
            print(language[9].strip())
        while True:
            cords = pyautogui.locateCenterOnScreen(button)
            pyautogui.click(cords)
            if cords != None:
                if lang_inside == "ru":
                    print(language[3].strip())
                    push(title=language[4].strip(), \
                         message=language[5].strip())
                elif lang_inside == "eng":
                    print(language[10].strip())
                    push(title = language[11].strip(),\
                         message = language[12].strip())
                break
    else:
        print(language[15].strip())

def push(title, message):
    plt = platform.system()
    if plt == "Darwin":
        command = f'''
        osascript -e 'display notification "{message}" with title "{title}"'
        '''
    elif plt == "Linux":
        command = f'''
        notify-send "{title}" "{message}"
        '''
    elif plt == "Windows":
        plyer.notification.notify\
            (message= message,
             app_name= "auto-aternos",
             title= title)
        return
    else:
        return
    os.system(command)

if start == "ru":
    print(language[1].strip())
    button = "RuButton.png"
    lang_inside = "ru"
    main()
elif start == "eng":
    print(language[8].strip())
    button = "EngButton.png"
    lang_inside = "eng"
    main()
else:
    print(language[15].strip())