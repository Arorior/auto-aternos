import PySimpleGUI
start = input("ru/eng ?")
def ru():
    if input("Введи start для запуска бота") == "start":
        main()

def eng():
    if input("Enter start to start the bot") == "start":
        main()

def main():
   print("doingg")
if start == "ru":
   ru()
elif start == "eng":
    eng()

