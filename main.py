from pyfastscreencap import pyfastscreencap as screencap
from time import sleep

recorder = screencap.Recorder("video.mp4", 0, 60, 100, True)

recorder.start_recording()

sleep(3)

frame_count = recorder.stop_recording()

print(f"Recorded {frame_count} frames")