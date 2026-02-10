import pyautogui
from utils import init_clash_window
from time import sleep

#set a 0.5 second delay after every pyautogui call to allow ui updates and prevent misclicks
pyautogui.PAUSE = 0.5

init_clash_window()

locations = {
    "cwl_menu": (80, 975),
    "close_popup": (2256, 40)
}
#open cwl menu
pyautogui.click(*locations["cwl_menu"])

#click red x to close popup if cwl is over and summary is up
pyautogui.click(*locations["close_popup"])