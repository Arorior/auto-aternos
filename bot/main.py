import pyautogui

button = None
start = input("ru/eng ?")

if start == "ru":
    print("ru")
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


