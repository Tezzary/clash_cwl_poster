import os
import subprocess
import imageio_ffmpeg

CLAN = "Lethal_Turtles"
CWL_DATE = "26_FEB"

directory = os.path.dirname(os.path.abspath(__file__))
videos_dir = os.path.join(directory, "videos", CLAN, CWL_DATE)

ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

file_list_path = os.path.join(videos_dir, "files.txt")

# Create concat list file
with open(file_list_path, "w", encoding="utf-8") as f:
    for day in range(1, 8):
        for attack in range(1, 16):
            file_name = f"attack_{attack}.mp4"
            file_path = os.path.join(videos_dir, f"day_{day}", file_name)

            if os.path.exists(file_path):
                print(f"{file_path} found, adding to list...")
                # IMPORTANT: use forward slashes for ffmpeg on Windows
                safe_path = file_path.replace("\\", "/")
                f.write(f"file '{safe_path}'\n")
            else:
                print(f"{file_path} not found, skipping...")

output_path = os.path.join(videos_dir, "archive.mp4")

# Run ffmpeg concat (NO re-encode)
subprocess.run([
    ffmpeg_path,
    "-f", "concat",
    "-safe", "0",
    "-i", file_list_path,
    "-c", "copy",
    output_path
], check=True)

#remove the concat list file
os.remove(file_list_path)
print("Archive created successfully.")
