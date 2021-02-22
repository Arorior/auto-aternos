import pyautogui

language = open('Languages', 'r').readlines()
button = None
lang_inside = None
start = input("ru/eng?\n")

def main():
    if input() == "start":
        if lang_inside == "ru":
            print(language[2].strip())
        elif lang_inside == "eng":
            print(language[7].strip())
        while True:
            cords = pyautogui.locateCenterOnScreen(button)
            pyautogui.click(cords)
            if cords != None:
                if lang_inside == "ru":
                    print(language[3].strip())
                elif lang_inside == "eng":
                    print(language[9].strip())
                break
    else:
        print(language[11].strip())

if start == "ru":
    print(language[1].strip())
    button = "RuButton.png"
    lang_inside = "ru"
    main()
elif start == "eng":
    print(language[6].strip())
    button = "EngButton.png"
    lang_inside = "eng"
    main()
else:
    print(language[11].strip())