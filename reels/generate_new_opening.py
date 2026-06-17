import os
from gtts import gTTS

# Define new opening script
script = "In the new AI world, the No Man Company will be everywhere, and I wanted to learn. I found Hermes is the perfect tool for that, but I had limited resources: only one PC and a PlayStation 5, which is not recommended. So, I ended up setting up Hermes Agent in my WSL on Windows. This is the note of that journey."

# Save to temporary audio file
tts = gTTS(text=script, lang='en')
tts.save("/mnt/d/git_repo/thefirstaicompany/reels/audio/scene1_new.mp3")

print("Generated new scene 1 audio.")
