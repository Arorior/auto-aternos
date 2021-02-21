import pyautogui

lang = open('Languages', 'r')
button = None
start = input("ru/eng?\n")

if start == "ru":
    for line in lang.readlines():
        print(line)
    button = "RuButton.png"
elif start == "eng":
    print("eng")
    button = "EngButton.png"
else:
    print("else")

def main():
    while True:
        cords = pyautogui.locateCenterOnScreen(button)
        pyautogui.click(cords)


