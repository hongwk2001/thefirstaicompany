import os
import subprocess

BASE_DIR = "/mnt/d/git_repo/thefirstaicompany/reels"
AUDIO_DIR = os.path.join(BASE_DIR, "audio")
IMAGE_DIR = os.path.join(BASE_DIR, "images")
OUTPUT_PATH = os.path.join(BASE_DIR, "output.mp4")

def get_duration(audio_path):
    cmd = ["ffprobe", "-i", audio_path, "-show_entries", "format=duration", "-v", "quiet", "-of", "csv=p=0"]
    return float(subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout.strip())

def main():
    scenes = [1, 2, 3, 4]
    slices = []
    scene_data = {
        1: {"img": "scene1.png", "aud": "scene1_new_narrative.mp3", "cap": "No Man Company Journey"},
        2: {"img": "scene_dashboard.png", "aud": "scene2.mp3", "cap": "Hermes Local Dashboard"},
        3: {"img": "scene_devqa.png", "aud": "scene3.mp3", "cap": "Dev-QA Swarm Loop"},
        4: {"img": "scene_evidence.png", "aud": "scene4.mp3", "cap": "Local LLM Integration"}
    }

    for s in scenes:
        data = scene_data[s]
        aud_path = os.path.join(AUDIO_DIR, data["aud"])
        dur = get_duration(aud_path)
        img_path = os.path.join(IMAGE_DIR, data["img"])
        slice_path = os.path.join(BASE_DIR, f"temp_{s}.mp4")
        
        filter_str = f"scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black,drawtext=text='{data['cap']}':fontsize=60:fontcolor=white:x=(w-text_w)/2:y=h-250:box=1:boxcolor=black@0.5:boxborderw=10"
        
        # Check if slice exists first, if not render
        if not os.path.exists(slice_path):
            cmd = ["ffmpeg", "-y", "-loop", "1", "-i", img_path, "-i", aud_path, "-c:v", "libx264", "-tune", "stillimage", "-t", str(dur), "-pix_fmt", "yuv420p", "-vf", filter_str, "-c:a", "aac", "-b:a", "192k", "-shortest", slice_path]
            subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        slices.append(slice_path)

    list_file = os.path.join(BASE_DIR, "slices.txt")
    with open(list_file, "w") as f:
        for slice_file in slices: f.write(f"file '{slice_file}'\n")
    
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file, "-c", "copy", OUTPUT_PATH])
    
    # Robust cleanup
    for f in slices:
        if os.path.exists(f): os.remove(f)
    if os.path.exists(list_file): os.remove(list_file)
    print(f"SUCCESS: {OUTPUT_PATH}")

if __name__ == "__main__": main()
