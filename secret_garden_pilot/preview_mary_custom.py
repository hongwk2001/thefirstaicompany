import os
import requests

API_KEY = "sk_20b0dea1abae29f3d31b36ecc757f706fcd9fd636bed7c54"
VOICE_ID = "Nggzl2QAXh3OijoXD116"
TEXT = "Why are you here? Get out! Send my nanny to me."

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}
data = {
    "text": TEXT,
    "model_id": "eleven_multilingual_v2"
}

print("Generating custom preview for Mary...")
response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
    filename = "preview_mary_custom.mp3"
    filepath = os.path.join("d:/git_repo/thefirstaicompany", filename)
    with open(filepath, "wb") as f:
        f.write(response.content)
    print(f"  Saved to {filename}")
else:
    print(f"  Failed: {response.status_code} - {response.text}")
