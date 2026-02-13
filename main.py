# python main.py -s 4 -r 1440p -p "C:\Users\xavie\OneDrive\Documents\Mother Folder\coding stuff\PROJECTS\ACTIVE\clash_cwl_poster\videos\Lethal_Turtles\26_FEB"

from utils import *
from navagate_menu import record_all_replays, RecordSettings
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--speed", type=int, help="Speed of the replays", required=True)
    parser.add_argument("-r", "--resolution", type=str, help="Recording Resolution", required=True)
    parser.add_argument("-p", "--path", type=str, help="Path to record the cwl into", required=True)
    parser.add_argument("-d", "--day", type=int, help="Only record a speficic day")

    args = parser.parse_args()

    init_clash_window()

    pyautogui.PAUSE = 0.0

    settings = RecordSettings(
        speed_factor = args.speed,
        resolution = args.resolution,
        path = args.path,
        day = args.day
    )
    print(settings)

    record_all_replays(settings)