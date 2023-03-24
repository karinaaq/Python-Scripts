from subprocess_maximize import Popen
import pyautogui

# Colocar las resoluciones de las pantallas
screen_size_1 = (1440, 900) 
screen_size_2 = (1920, 1080) 
path_1 = "C:\Program Files (x86)\Internet Explorer\iexplore.exe"
path_2 = "C:\Program Files\Google\Chrome\Application\chrome.exe"
Popen(path_1,show='maximized', priority=0)
pyautogui.moveTo(screen_size_1[0], screen_size_1[1])  # mueve la flechita a la primera pantalla

Popen(path_2,show='maximized', priority=0)
pyautogui.moveTo(screen_size_2[0], screen_size_2[1])  # mueve la flechita a la segunda pantalla
