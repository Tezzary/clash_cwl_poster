import pyautogui
from utils import *
from time import sleep
from recording import record_replay

init_clash_window()

locations = {
    "cwl_menu": (80, 975),
    "center_of_screen": (1283, 565),
    "return_home": (135,1302),

    "close_popup": (2256, 40),
    "first_enemy_base": (1488, 910),
    "replay_button": (984, 1293),
    "next_base": (1789, 1191),
    "3rd_star": (1063, 1225, 255,221,77)
}

three_star_color = (255,221,77)

days = {
    1:  (772,1324),
    2:  (941,1324),
    3:  (1112,1324),
    4:  (1287,1324),
    5:  (1456,1324),
    6:  (1626,1324),
    7:  (1795,1324)
}

def start_replay(day: int, replay: int) -> bool:
    '''
    click on cwl menu
    scroll up
    close popup
    select right day
    click top replay
    click right arrow till we get to the replay
    check if its 3 stars, exit if its not
    press replay
    '''
    if day > 7 or day < 1:
        raise ValueError("day is out of range")
    
    if replay < 1:
        raise ValueError("replay is one indexed, and the value given is less than 1")
    
    # open cwl page
    click_on_screen(*locations["cwl_menu"])
    # sleep(5) # sleep extra long in case it needs to load
    
    # try to close the popup
    click_on_screen(*locations["close_popup"])

    # scroll to the top of the page
    move_mouse_to(*locations["center_of_screen"])
    for i in range(15):
        pyautogui.scroll(500)

    # go the the right day
    click_on_screen(*days[day])
    sleep(5)

    # click on the first enemy base
    click_on_screen(*locations["first_enemy_base"])

    # go to the correct replay
    for i in range(replay - 1):
        click_on_screen(*locations["next_base"], min_delay=0.1, max_delay=0.3, max_press_time=.15)

    # check if its a 3 star
    if not check_color_of_pixel(*locations["3rd_star"]):
        return False

    # start the replay
    click_on_screen(*locations["replay_button"])

    return True

def reset():
    # exit out of the replay
    click_on_screen(*locations["return_home"])

    # close the popup
    click_on_screen(*locations["close_popup"])

    # return home
    click_on_screen(*locations["return_home"])

if __name__ == "__main__":
    start_replay(4, 11)
    record_replay("replay.mp4", speed_factor=4)
    reset()