import subprocess
import os

BASE_DIR = "/mnt/d/git_repo/thefirstaicompany/reels"
INPUT_VIDEO = os.path.join(BASE_DIR, "no_man_company_journey_v2.mp4")
OUTPUT_VIDEO = os.path.join(BASE_DIR, "no_man_company_journey_v3_captions.mp4")

# Basic caption mapping (start_time, end_time, text)
captions = [
    (0, 5, "In the new AI world,"),
    (5, 8, "the No Man Company will be everywhere,"),
    (8, 10, "and I wanted to learn."),
    (10, 13, "I found Hermes is the perfect tool for that,"),
    (13, 18, "but I had limited resources: only one PC"),
    (18, 22, "and a PlayStation 5, which is not recommended."),
    (22, 27, "So, I ended up setting up Hermes Agent in my WSL on Windows."),
    (27, 32, "This is the note of that journey.")
]

# Construct complex filter for FFmpeg
# Using drawtext to overlay white text with black outline
filter_string = ""
for i, (start, end, text) in enumerate(captions):
    filter_string += f"drawtext=text='{text}':x=(w-text_w)/2:y=h-200:fontsize=48:fontcolor=white:shadowcolor=black:shadowx=2:shadowy=2:enable='between(t,{start},{end})',"

# Remove trailing comma
filter_string = filter_string.rstrip(',')

cmd = [
    "ffmpeg", "-y",
    "-i", INPUT_VIDEO,
    "-vf", filter_string,
    "-c:a", "copy",
    OUTPUT_VIDEO
]

subprocess.run(cmd)
