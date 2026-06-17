import os
import sys
import json
import asyncio
import edge_tts

PILOT_DIR = "d:/git_repo/thefirstaicompany/secret_garden_pilot"

LANG_CONFIGS = {
    "en": {
        "script": os.path.join(PILOT_DIR, "secret_garden_chapter_1_script.json"),
        "output": os.path.join(PILOT_DIR, "secret_garden_chapter_1.mp3"),
        "temp_dir": os.path.join(PILOT_DIR, "temp_audio_en"),
        "mary_dir": "mary_voice",
        "mary_files": ["mary_1.mp3", "mary_2.mp3", "mary_3.mp3", "mary_4.mp3", "mary_5.mp3"],
        "name": "English"
    },
    "kr": {
        "script": os.path.join(PILOT_DIR, "secret_garden_chapter_1_script_kr.json"),
        "output": os.path.join(PILOT_DIR, "secret_garden_chapter_1_kr.mp3"),
        "temp_dir": os.path.join(PILOT_DIR, "temp_audio_kr"),
        "mary_dir": "mary_voice_kr",
        "mary_files": ["mary_1_kr.mp3", "mary_2_kr.mp3", "mary_3_kr.mp3", "mary_4_kr.mp3", "mary_5_kr.mp3"],
        "name": "Korean"
    }
}

def check_mary_files(lang_cfg):
    missing = []
    for f in lang_cfg["mary_files"]:
        path = os.path.join(PILOT_DIR, lang_cfg["mary_dir"], f)
        if not os.path.exists(path):
            missing.append(f)
    return missing

def fetch_edge_audio(text, voice_id, index, temp_dir):
    temp_file = os.path.join(temp_dir, f"segment_{index:03d}.mp3")
    try:
        # Programmatic call to edge_tts Communicate object
        communicate = edge_tts.Communicate(text, voice_id)
        asyncio.run(communicate.save(temp_file))
        if os.path.exists(temp_file):
            return temp_file
    except Exception as e:
        print(f"  Error generating segment {index} via Edge-TTS API: {e}")
    return None

def stitch_audio_binary(files, output_path):
    try:
        with open(output_path, "wb") as outfile:
            for fpath in files:
                with open(fpath, "rb") as infile:
                    outfile.write(infile.read())
        return True
    except Exception as e:
        print(f"  Error stitching files: {e}")
        return False

def generate_language(lang_code):
    cfg = LANG_CONFIGS[lang_code]
    print(f"\n=== Processing {cfg['name']} Version ===")
    
    missing_mary = check_mary_files(cfg)
    if missing_mary:
        print(f"ERROR: Missing custom files for Mary's voice ({cfg['name']}):")
        for m in missing_mary:
            print(f"  - {os.path.join(cfg['mary_dir'], m)}")
        print(f"Please generate these lines on ElevenLabs using your custom voice and place them in the directory.")
        return False

    if not os.path.exists(cfg["temp_dir"]):
        os.makedirs(cfg["temp_dir"])

    with open(cfg["script"], "r", encoding="utf-8") as f:
        script = json.load(f)

    segment_files = []
    success = True

    try:
        for item in script:
            idx = item["id"]
            if item.get("type") == "custom_file":
                src_path = os.path.join(PILOT_DIR, item["file_path"])
                dest_path = os.path.join(cfg["temp_dir"], f"segment_{idx:03d}.mp3")
                with open(src_path, "rb") as fsrc:
                    with open(dest_path, "wb") as fdest:
                        fdest.write(fsrc.read())
                segment_files.append(dest_path)
                print(f"  Segment {idx} (Mary): copied {item['file_path']}")
            else:
                text = item["text"]
                voice_id = item["voice_id"]
                print(f"  Segment {idx} ({item['speaker']}): calling Edge-TTS ({voice_id})...")
                temp_file = fetch_edge_audio(text, voice_id, idx, cfg["temp_dir"])
                if temp_file:
                    segment_files.append(temp_file)
                else:
                    success = False
                    break

        if success:
            print(f"  Stitching all {len(segment_files)} segments...")
            stitch_success = stitch_audio_binary(segment_files, cfg["output"])
            if stitch_success:
                print(f"SUCCESS: Generated {cfg['output']}")
                return True
        return False

    finally:
        # Clean up temp files
        print("  Cleaning up temporary segment files...")
        for f in segment_files:
            try:
                if os.path.exists(f):
                    os.remove(f)
            except Exception as e:
                pass
        try:
            if os.path.exists(cfg["temp_dir"]):
                os.rmdir(cfg["temp_dir"])
        except Exception as e:
            pass

def main():
    if len(sys.argv) > 1:
        lang = sys.argv[1].lower()
        if lang in LANG_CONFIGS:
            generate_language(lang)
        else:
            print(f"Unknown language: {lang}. Use 'en' or 'kr'.")
    else:
        # Try both
        en_success = generate_language("en")
        kr_success = generate_language("kr")
        
if __name__ == "__main__":
    main()
