from utils import *
from time import sleep
from recording import record_replay
from navagate_menu import check_if_recording_exists, start_replay, reset
from locations import locations

if __name__ == "__main__":
    init_clash_window()

    pyautogui.PAUSE = 0.0

    CLAN_NAME = "Lethal_Turtles"
    DATE = "26_FEB"

    on_cwl_page = False

    for day in range(1, 8):
        for attack in range (1, 16):
            file_path = [CLAN_NAME, DATE, f"day_{day}"]
            file_name = f"attack_{attack}"

            print(f"recording {"".join([f"{x}/" for x in file_path])}{file_name}")

            if check_if_recording_exists(file_path, file_name):
                if on_cwl_page:
                    # if we are navigating the cwl menu already then we must go to the next base in the gui
                    click_on_screen(*locations["next_base"])
                    continue
                else:
                    # otherwise we can just do noting (since we will click on the next button x times anyway in record_replay)
                    continue

            start_recording = start_replay(day, attack, on_cwl_page)
            on_cwl_page = True

            if start_recording:
                record_replay(file_path, file_name, speed_factor=1)
                reset()
        
        # bring us home
        reset()
        on_cwl_page = False
        
