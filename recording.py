from pyfastscreencap import pyfastscreencap as screencap
from time import sleep
from utils import find_location_on_screen, click_on_screen, init_clash_window, move_mouse_to
import math
import time
import pyautogui
import os
import obsws_python as obs

FRAME_RATE = 60

HOST = 'localhost'
PORT = 4455
PASSWORD = 'password' # Replace with your actual password

recording_start = 0

def start_recording(video_file):
    global recording_start

    cl = obs.ReqClient(host=HOST, port=PORT, password=PASSWORD, timeout=3)
    
    # os.path.pardir is basically just .. so im basically just adding .. to it and then taking the path
    # stack overflow reckons that using os.path.dirname is unreliable lmao
    parent_dir = os.path.abspath(os.path.join(video_file, os.path.pardir))
    filename = os.path.basename(video_file)

    os.makedirs(parent_dir, exist_ok=True)

    cl.set_record_directory(parent_dir)
    cl.set_profile_parameter("Output", "FilenameFormatting", filename)

    resp = cl.start_record()
    recording_start = time.time()
    

def stop_recording():
    cl = obs.ReqClient(host=HOST, port=PORT, password=PASSWORD, timeout=3)
    resp = cl.stop_record()
    return time.time() - recording_start

locations = {
    "speed_button": (2450, 1300),
    "pause_button": (2280, 1300)
}

def toggle_pause():
    click_on_screen(*locations["pause_button"], max_offset=20, min_delay=0.0, max_delay=0.0, min_press_time=0.0, max_press_time=0.0)

def speed_up_game():
    click_on_screen(*locations["speed_button"], max_offset=20, min_delay=0.0, max_delay=0.0, min_press_time=0.0, max_press_time=0.0)

def zoom_out():
    move_mouse_to(1280, 720)
    pyautogui.keyDown('ctrl')
    sleep(0.1)
    for _ in range(10):
        pyautogui.scroll(-500)
        sleep(0.3)
    pyautogui.keyUp('ctrl')

# returns replay length in seconds
def record_replay(video_file, speed_factor=1):
    if not speed_factor in (1, 2, 4):
        raise ValueError("Speed factor must be 1 of: 1, 2, 4")
    
    while not find_location_on_screen("resources/pause_button.png", 0.99):
        sleep(0.1)
    
    #handling game speed
    speed_button_clicks = round(math.log2(speed_factor))
    for _ in range(speed_button_clicks):
        speed_up_game()

    #initially pause while doing setup
    toggle_pause()

    #zoom out
    zoom_out()

    #unpause to begin recording
    toggle_pause()

    #recording
    start_recording(video_file)
    
    #check if play again button is on screen to end replay
    while not find_location_on_screen("resources/play_again.png", 0.99):
        sleep(1)

    recording_time = stop_recording()
    replay_time = recording_time * speed_factor

    print(f"Recorded {replay_time} second replay in {recording_time} seconds at speed factor {speed_factor}x")

    return replay_time

if __name__ == "__main__":
    pass