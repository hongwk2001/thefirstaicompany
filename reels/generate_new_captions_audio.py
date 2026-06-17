from gtts import gTTS
import os

# New narration script
narration = """
In the new AI world, the No Man Company will be everywhere. I wanted to learn how, and Hermes is the perfect tool for that. But with limited resources—just one PC and a PlayStation 5—I had to get creative. I set up Hermes Agent in my Windows WSL. This is the story of my journey, including the Dev-QA loops, the Hermes dashboard, and the local models like Qwen and Gemma. I'm building my No Man Company, one step at a time.
"""

# Generate Audio
tts = gTTS(text=narration, lang='en')
tts.save("/mnt/d/git_repo/thefirstaicompany/reels/audio/scene1_new_narrative.mp3")
print("Generated narrative audio.")
