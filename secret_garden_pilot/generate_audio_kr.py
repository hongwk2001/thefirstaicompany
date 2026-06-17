import os
import sys
import json
import requests

API_KEY = "sk_20b0dea1abae29f3d31b36ecc757f706fcd9fd636bed7c54"
SCRIPT_FILE = "d:/git_repo/thefirstaicompany/secret_garden_pilot/secret_garden_pilot_script_kr.json"
OUTPUT_FILE = "d:/git_repo/thefirstaicompany/secret_garden_pilot/secret_garden_pilot_kr.mp3"
TEMP_DIR = "d:/git_repo/thefirstaicompany/secret_garden_pilot/temp_audio_kr"
PILOT_DIR = "d:/git_repo/thefirstaicompany/secret_garden_pilot"

def check_mary_files():
    required_files = [
        "mary_voice_kr/mary_1_kr.mp3",
        "mary_voice_kr/mary_2_kr.mp3"
    ]
    missing = []
    for rf in required_files:
        path = os.path.join(PILOT_DIR, rf)
        if not os.path.exists(path):
            missing.append(rf)
    return missing

def fetch_elevenlabs_audio(text, voice_id, index):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
    
    print(f"Generating Korean audio segment {index} ({voice_id})...")
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        temp_file = os.path.join(TEMP_DIR, f"segment_{index:03d}.mp3")
        with open(temp_file, "wb") as f:
            f.write(response.content)
        return temp_file
    else:
        print(f"Error generating Korean segment {index}: {response.status_code} - {response.text}")
        return None

def stitch_audio_binary(files, output_path):
    print("Stitching Korean audio files together using binary concatenation...")
    try:
        with open(output_path, "wb") as outfile:
            for fpath in files:
                with open(fpath, "rb") as infile:
                    outfile.write(infile.read())
        print(f"Success! Stitched file saved to {output_path}")
        return True
    except Exception as e:
        print(f"Error stitching files: {e}")
        return False

def main():
    missing_mary = check_mary_files()
    if missing_mary:
        print("ERROR: Missing custom Korean audio files for Mary's voice:")
        for m in missing_mary:
            print(f"  - {m}")
        print("\nPlease generate Mary's Korean lines on ElevenLabs using your custom voice, download them, and place them in the 'mary_voice_kr' directory.")
        sys.exit(1)

    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

    with open(SCRIPT_FILE, "r", encoding="utf-8") as f:
        script = json.load(f)

    segment_files = []
    success = True

    try:
        for idx, item in enumerate(script):
            segment_idx = item["id"]
            if item.get("type") == "custom_file":
                src_path = os.path.join(PILOT_DIR, item["file_path"])
                dest_path = os.path.join(TEMP_DIR, f"segment_{segment_idx:03d}.mp3")
                with open(src_path, "rb") as fsrc:
                    with open(dest_path, "wb") as fdest:
                        fdest.write(fsrc.read())
                segment_files.append(dest_path)
                print(f"Segment {segment_idx} (Mary): copied custom file {item['file_path']}")
            else:
                text = item["text"]
                voice_id = item["voice_id"]
                temp_file = fetch_elevenlabs_audio(text, voice_id, segment_idx)
                if temp_file:
                    segment_files.append(temp_file)
                else:
                    success = False
                    break

        if success:
            stitch_success = stitch_audio_binary(segment_files, OUTPUT_FILE)
            if stitch_success:
                print("Korean audio generation completed successfully.")

    finally:
        # Clean up temp files
        print("Cleaning up temporary segment files...")
        for f in segment_files:
            try:
                if os.path.exists(f):
                    os.remove(f)
            except Exception as e:
                print(f"Could not remove temp file {f}: {e}")
        try:
            if os.path.exists(TEMP_DIR):
                os.rmdir(TEMP_DIR)
        except Exception as e:
            pass

if __name__ == "__main__":
    main()
