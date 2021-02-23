import pyautogui
import platform
import plyer
import os


def main():
    if input() == "start":
        
        if lang_inside == "ru":
            print(language[2].strip())
            
        elif lang_inside == "eng":
            print(language[9].strip())
            
        while True:
            cords = pyautogui.locateCenterOnScreen(button)
            pyautogui.click(cords)
            
            if cords is not None:
                
                if lang_inside == "ru":
                    print(language[3].strip())
                    push(title=language[4].strip(), message=language[5].strip())
                    
                elif lang_inside == "eng":
                    print(language[10].strip())
                    push(title=language[11].strip(), message=language[12].strip())
                break
                
    else:
        print(language[15].strip())


def push(title, message):
    plt = platform.system()
    
    if plt == "Darwin":
        command = f'''
        osascript -e 'display notification "{message}"  \
        with title "{title}"'
        '''
        
    elif plt == "Linux":
        command = f'''
        notify-send "{title}" "{message}"
        '''
        
    elif plt == "Windows":
        plyer.notification.notify(message=message,
                                  app_name="auto-aternos",
                                  title=title)
        return
    
    else:
        return
    os.system(command)

    
if __name__ == '__main__':
    language = open('Languages', 'r').readlines()
    button = None
    lang_inside = None
    start = input("[ru/en] ").lower()
    
    if start not in ('ru', 'en'):
        exit(0)
        
    is_ru = True if start == 'ru' else False
    print(language[1].strip() if is_ru else language[8].strip())
    button = "RuButton.png" if is_ru else "EngButton.png"
    lang_inside = start
    main()
