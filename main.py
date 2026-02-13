from utils import *
from navagate_menu import record_all_replays
from locations import locations

if __name__ == "__main__":
    init_clash_window()

    pyautogui.PAUSE = 0.0

    CLAN_NAME = "Lethal_Turtles"
    DATE = "26_FEB"

    record_all_replays(CLAN_NAME, DATE, 4)