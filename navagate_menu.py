from utils import *
from time import sleep
from recording import record_replay
import os
from locations import *

'''
day = cwl day the replay is on
replay = the number of the enemy base to rec
on_cwl_page = if we just finished recording another replay (makes navigating faster)
'''
def start_replay(day: int, replay: int, on_cwl_page: bool = False) -> bool:
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
    
    if on_cwl_page:
        # wait till we can see the info in the top corner
        while not find_location_on_screen("resources/cwl_info.png"):
            continue

        if find_location_on_screen("resources/red_x.png"):
            click_on_screen(*locations["close_popup"])
        
        click_on_screen(*locations["next_base"])

        # check if its a 3 star
        if not check_color_of_pixel(*locations["3rd_star"], threshold=40):
            print("exiting because star col is wrong")
            return False

        click_on_screen(*locations["replay_button"])

        return True

    # open cwl page
    click_on_screen(*locations["cwl_menu"])

    # wait till we can see the info in the top corner
    while not find_location_on_screen("resources/cwl_info.png"):
        continue
    
    # close the popup
    sleep(0.5) # leave time for popup animation to play
    if find_location_on_screen("resources/red_x.png"):
        click_on_screen(*locations["close_popup"])

    # scroll to the top of the page (we know were at the top when the top is black)
    move_mouse_to(*locations["center_of_screen"])
    while not check_color_of_pixel(x=0, y=0, r=0, g=0, b=0, threshold=3):
        scroll(1)

    # go the the right day
    click_on_screen(*days[day])
        
    # wait till we can see the info in the top corner
    sleep(0.5) # leave time for the clouds to come
    while not find_location_on_screen("resources/cwl_info.png"):
        continue

    # click on the first enemy base
    click_on_screen(*locations["first_enemy_base"])

    # go to the correct replay
    for i in range(replay - 1):
        click_on_screen(*locations["next_base"], min_delay=0.1, max_delay=0.3, max_press_time=.15)

    # check if its a 3 star
    if not check_color_of_pixel(*locations["3rd_star"], threshold=40):
        print("exiting because star col is wrong")
        return False

    # start the replay
    click_on_screen(*locations["replay_button"])

    return True

def reset():
    # exit out of the replay
    click_on_screen(*locations["return_home"])

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
