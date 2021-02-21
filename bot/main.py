import logging
from maia import AutoInstaller, printr
try:
    import pyautogui
    import keyboard
except ImportError:
    AutoInstaller()



