import os
import requests

API_KEY = "sk_20b0dea1abae29f3d31b36ecc757f706fcd9fd636bed7c54"

ALTERNATIVES = {
    "Jessica": "cgSgspJ2msm6clMCkdW9",
    "Alice": "Xb7hH8MSUJpSbSDYk0k2",
    "River": "SAz9YHcvj6GT2YYXdXww"
}

TEXT = "Why are you here? Get out! Send my nanny to me."

def generate_alternative(name, voice_id):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": TEXT,
        "model_id": "eleven_multilingual_v2"
    }
    
    print(f"Generating alternative for Mary using {name}...")
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        filename = f"preview_mary_{name.lower()}.mp3"
        filepath = os.path.join("d:/git_repo/thefirstaicompany", filename)
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"  Saved to {filename}")
    else:
        print(f"  Failed for {name}: {response.status_code} - {response.text}")

if __name__ == "__main__":
    for name, voice_id in ALTERNATIVES.items():
        generate_alternative(name, voice_id)
