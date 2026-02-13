from utils import *
from time import sleep
from locations import locations
from recording import record_replay
import os

days = {
    1: (670,1301),
    2: (877,1294),
    3: (1083,1296),
    4: (1293,1296),
    5: (1495,1292),
    6: (1694,1294),
    7: (1908,1293),
}

def wait_for_cwl_menu_to_load():
    sleep(0.5) # make sure the clouds have actually came

    while not find_location_on_screen(r"resources\cwl_info.png"): pass

def scroll_to_top():
    move_mouse_to(*locations["center_of_screen"])
    while not check_color_of_pixel(0, 0, 0, 0, 0, 3):
        scroll(1)

def record_all_replays(clan_name: str, date: str, speed_factor: int):
    '''
    open cwl menu

    for day in 1 to 7
        click on day

        for attack in 1 to 15
            if file does not exist
                record attack
            go to next attack
    '''
    click_on_screen(*locations["cwl_menu"])
    wait_for_cwl_menu_to_load()
    click_on_screen(*locations["close_popup"])

    for day in range(1, 8):
        click_on_screen(*locations["center_of_screen"])
        click_on_screen(*days[day])
        wait_for_cwl_menu_to_load()
        scroll_to_top()
        click_on_screen(*locations["first_enemy_base"])

        for attack in range(1, 16):
            filepath = [clan_name, date, f"day_{day}"]
            filename = f"attack_{attack}"

            if not check_if_recording_exists(filepath, filename):
                click_on_screen(*locations["replay_button"], min_delay=0.05, max_delay=0.1, min_press_time=0.05, max_press_time=0.1)
                
                record_replay(filepath, filename, speed_factor)

                click_on_screen(*locations["return_home"])
                wait_for_cwl_menu_to_load()
                click_on_screen(*locations["close_popup"])
            
            click_on_screen(*locations["next_base"])

def check_if_recording_exists(subdirs, filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))

    videos_dir = os.path.join(base_dir, "videos")
    for subdir in subdirs:
        videos_dir = os.path.join(videos_dir, subdir)
    
    video_file = os.path.join(videos_dir, f"{filename}.mp4")

    if os.path.exists(video_file):
        return True
    
    print(f"file `{video_file}` does not exist")
    return False
