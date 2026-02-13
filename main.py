from utils import *
from navagate_menu import record_all_replays, RecordSettings
from locations import locations

if __name__ == "__main__":
    init_clash_window()

    pyautogui.PAUSE = 0.0

    CLAN_NAME = "Lethal_Turtles"
    DATE = "26_FEB"

    settings = RecordSettings(
        clan_name="Lethal_Turtles",
        date="26_FEB",
        speed_factor=1,
        resolution="1080p"
    )

    record_all_replays(settings)