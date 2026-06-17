import os
import requests

API_KEY = "sk_20b0dea1abae29f3d31b36ecc757f706fcd9fd636bed7c54"

# Define proposed casting from active ElevenLabs voices
CASTING = {
    "Narrator": {
        "voice_id": "JBFqnCBsd6RMkjVDRZzb",  # George
        "text": "When Mary Lennox was sent to live with her uncle at Misselthwaite Manor, everyone described her as the most unpleasant-looking child they had ever seen."
    },
    "Mary": {
        "voice_id": "pFZP5JQG7iQjIQuC4Bku",  # Lily
        "text": "Why are you here? Get out! Send my nanny to me."
    },
    "Servant": {
        "voice_id": "hpp4J3VqNfWAUOO0d1Us",  # Bella
        "text": "The nanny could not come, Missie Sahib. It is not possible for her to come."
    },
    "Mother": {
        "voice_id": "FGY2WhTYpPnrIDTdsKH5",  # Laura
        "text": "Oh, I know I should have! I only stayed behind for that silly dinner party. What a fool I was!"
    },
    "Officer": {
        "voice_id": "onwK4e9ZLuTAKqWW03F9",  # Daniel
        "text": "It's terrible, Mrs. Lennox. You should have left for the cooler mountain regions weeks ago."
    }
}

def generate_preview(character, config):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{config['voice_id']}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": config["text"],
        "model_id": "eleven_multilingual_v2"
    }
    
    print(f"Generating preview for {character}...")
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        filename = f"preview_{character.lower()}.mp3"
        filepath = os.path.join("d:/git_repo/thefirstaicompany", filename)
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"  Saved to {filename}")
    else:
        print(f"  Failed for {character}: {response.status_code} - {response.text}")

if __name__ == "__main__":
    for character, config in CASTING.items():
        generate_preview(character, config)
