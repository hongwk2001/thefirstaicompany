import subprocess
import os

BASE_DIR = "/mnt/d/git_repo/thefirstaicompany/reels"
INPUT_VIDEO = os.path.join(BASE_DIR, "no_man_company_journey_v2.mp4")
OUTPUT_VIDEO = os.path.join(BASE_DIR, "no_man_company_journey_v3_captions.mp4")

# Captions with escaped colons for FFmpeg
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

# Build filter
filters = []
for start, end, text in captions:
    # Escape colon and other special characters in the text for drawtext
    escaped_text = text.replace(':', '\\:').replace(',', '\,')
    f = f"drawtext=text='{escaped_text}':x=(w-text_w)/2:y=h-200:fontsize=48:fontcolor=white:shadowcolor=black:shadowx=2:shadowy=2:enable='between(t,{start},{end})'"
    filters.append(f)

filter_string = ",".join(filters)

cmd = [
    "ffmpeg", "-y",
    "-i", INPUT_VIDEO,
    "-vf", filter_string,
    "-c:a", "copy",
    OUTPUT_VIDEO
]

subprocess.run(cmd)
