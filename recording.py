from pyfastscreencap import pyfastscreencap as screencap
from time import sleep
from utils import find_location_on_screen, click_on_screen, move_mouse_to
import math
import pyautogui

FRAME_RATE = 60

locations = {
    "speed_button": (2460, 1340),
    "pause_button": (2325, 1340)
}

def toggle_pause():
    click_on_screen(*locations["pause_button"], max_delay=.3)

def speed_up_game():
    click_on_screen(*locations["speed_button"], max_delay=.3)

# returns replay length in seconds
def record_replay(filepath, speed_factor=1):
    if not speed_factor in (1, 2, 4):
        raise ValueError("Speed factor must be 1 of: 1, 2, 4")
    
    while not find_location_on_screen("resources/pause_button.png", 0.99):
        sleep(0.1)
    
    #initially pause while doing setup
    toggle_pause()

    #zoom out
    move_mouse_to(1000, 1000)
    for _ in range(10):
        pyautogui.scroll(-500)
        sleep(0.1)

    #unpause to begin recording
    toggle_pause()

    #handling game speed
    speed_button_clicks = round(math.log2(speed_factor))
    for _ in range(speed_button_clicks):
        speed_up_game()

    #recording
    recorder = screencap.Recorder(filepath, 0, FRAME_RATE, 100, True)

    recorder.start_recording()
    
    #check if play again button is on screen to end replay
    while not find_location_on_screen("resources/play_again.png", 0.99):
        sleep(1)

    frame_count = recorder.stop_recording()

    replay_time = frame_count / FRAME_RATE * speed_factor

    print(f"Recorded {frame_count} frames")
    print(f"Recorded {replay_time} second replay")

    return 

if __name__ == "__main__":
    record_replay("replay.mp4", 2)