import os
import sys
import json
import asyncio
import edge_tts

# Reconfigure stdout to prevent encoding errors on Windows console when printing Korean text
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

PILOT_DIR = "d:/git_repo/thefirstaicompany/secret_garden_pilot"

# We will use Edge-TTS neural voices as a fallback to avoid paid ElevenLabs account limits
ENGLISH_MARY_VOICE = "en-US-AnaNeural" # Friendly child female voice
KOREAN_MARY_VOICE = "ko-KR-SunHiNeural"  # Friendly standard Korean female voice

async def generate_edge_voice(text, voice_id, output_path):
    print(f"Generating Edge-TTS voice: \"{text[:30]}...\" -> {os.path.basename(output_path)}")
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        communicate = edge_tts.Communicate(text, voice_id)
        await communicate.save(output_path)
        if os.path.exists(output_path):
            print("  Successfully saved.")
            return True
    except Exception as e:
        print(f"  Error generating voice via Edge-TTS: {e}")
    return False

def process_script(script_path, voice_id):
    print(f"\nProcessing script: {os.path.basename(script_path)}")
    with open(script_path, "r", encoding="utf-8") as f:
        script = json.load(f)
        
    for item in script:
        if item.get("type") == "custom_file":
            text = item["text"]
            file_path = item["file_path"]
            full_output_path = os.path.join(PILOT_DIR, file_path)
            
            # Force generation
            success = asyncio.run(generate_edge_voice(text, voice_id, full_output_path))
            if not success:
                print("Stopping generation due to error.")
                return False
    return True

if __name__ == "__main__":
    print("=== Starting Mary Custom Voice Generation (Edge-TTS Fallback) ===")
    
    # 1. English Script (using en-US-AnaNeural child voice)
    en_script = os.path.join(PILOT_DIR, "secret_garden_chapter_1_script.json")
    process_script(en_script, ENGLISH_MARY_VOICE)
    
    # 2. Korean Script (using ko-KR-SunHiNeural voice)
    kr_script = os.path.join(PILOT_DIR, "secret_garden_chapter_1_script_kr.json")
    process_script(kr_script, KOREAN_MARY_VOICE)
    
    print("\n=== Generation Complete ===")
