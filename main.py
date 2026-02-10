import pyautogui
from utils import init_clash_window
from time import sleep

init_clash_window()

#open cwl menu
pyautogui.click(80, 975)
sleep(1)

#click red x to close popup if cwl is over and summary is up
pyautogui.click(2256, 40)
sleep(1)