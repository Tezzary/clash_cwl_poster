# python main.py -c "Lethal_Turtles" -d "26_FEB" -t 2

from utils import *
from navagate_menu import record_all_replays
from RecordSettings import get_settings
from locations import locations
import argparse

def check_args_valid():
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--clan_name", type=str, help="The name of the clan were recording", required=True)
    parser.add_argument("-d", "--date", type=str, help="The date of the cwl (YY_MMM)", required=True)
    parser.add_argument("-da", "--day", type=int, help="Only record a speficic day")

    # TODO: Offload this part to a different service and pass in speed factor and res directly as cli arguments
    parser.add_argument("-t", "--tier", type=int, help="Tier of the clan", required=True)

    args = parser.parse_args()

    init_clash_window()

    pyautogui.PAUSE = 0.0

    settings = get_settings(args.clan_name, args.date, args.tier, args.day)
    print(settings)

    record_all_replays(settings)