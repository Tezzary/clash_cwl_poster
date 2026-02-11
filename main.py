import pyautogui
from utils import *
from time import sleep
from recording import record_replay

locations = {
    "cwl_menu": (105, 877),
    "close_popup": (2270, 82),
    "center_of_screen": (1282, 651),
    "return_home": (155, 1282),
    "first_enemy_base": (1486, 899),
    "replay_button": (931, 1265),
    "next_base": (1896, 1142),
    "3rd_star": (1018, 1182, 255, 221, 77)
}

days = {
    1: (670,1301),
    2: (877,1294),
    3: (1083,1296),
    4: (1293,1296),
    5: (1495,1292),
    6: (1694,1294),
    7: (1908,1293),
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
    sleep(5) # sleep extra long in case it needs to load
    
    # try to close the popup
    click_on_screen(*locations["close_popup"])

    # scroll to the top of the page
    move_mouse_to(*locations["center_of_screen"])
    scroll(15)

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
    sleep(2)

    # close the popup
    click_on_screen(*locations["close_popup"])

    # return home
    click_on_screen(*locations["return_home"])

if __name__ == "__main__":
    init_clash_window()

    CLAN_NAME = "Lethal_Turtles"
    DATE = "26_FEB"

    for day in range(1, 8):
        for attack in range (1, 16):

            file_path = [CLAN_NAME, DATE, f"day_{day}"]
            file_name = f"attack_{attack}"

            print(f"recording {"".join([f"{x}/" for x in file_path])}{file_name}")

            start_replay(day, attack)
            record_replay(file_path, file_name, speed_factor=4)
            reset()