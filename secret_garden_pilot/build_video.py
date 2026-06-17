import os
import sys
import json
import subprocess
import argparse
import asyncio
import edge_tts

def get_audio_duration(audio_path):
    """Get the exact duration of the audio file in seconds using ffprobe."""
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", audio_path
    ]
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return float(result.stdout.strip())
    except Exception as e:
        print(f"Error reading audio duration with ffprobe for {audio_path}: {e}")
        sys.exit(1)

def format_timestamp(seconds):
    """Convert seconds float to SRT timestamp format (HH:MM:SS,mmm)."""
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    mils = int(round((seconds - int(seconds)) * 1000))
    if mils == 1000:
        mils = 999
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{mils:03d}"

async def get_exact_segment_durations(script, pilot_dir):
    """Generate temporary files for Edge-TTS and read exact durations for all segments."""
    durations = []
    temp_dir = os.path.join(pilot_dir, "temp_srt_durations")
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
        
    try:
        for idx, item in enumerate(script):
            segment_idx = item["id"]
            if item.get("type") == "custom_file":
                src_path = os.path.join(pilot_dir, item["file_path"])
                duration = get_audio_duration(src_path)
                durations.append(duration)
                print(f"  Segment {segment_idx} (Mary custom file): {duration:.2f}s")
            else:
                text = item["text"]
                voice_id = item["voice_id"]
                temp_file = os.path.join(temp_dir, f"temp_{segment_idx:03d}.mp3")
                
                # Generate edge-tts segment to measure exact length
                communicate = edge_tts.Communicate(text, voice_id)
                await communicate.save(temp_file)
                
                duration = get_audio_duration(temp_file)
                durations.append(duration)
                print(f"  Segment {segment_idx} ({item['speaker']}): {duration:.2f}s")
                
                # Cleanup immediately
                if os.path.exists(temp_file):
                    os.remove(temp_file)
    finally:
        # Cleanup temp directory
        if os.path.exists(temp_dir):
            for f in os.listdir(temp_dir):
                try:
                    os.remove(os.path.join(temp_dir, f))
                except:
                    pass
            try:
                os.rmdir(temp_dir)
            except:
                pass
                
    return durations

def generate_srt(script_path, srt_path, pilot_dir):
    """Generate a perfectly synced SRT file by measuring exact segment durations."""
    with open(script_path, "r", encoding="utf-8") as f:
        script = json.load(f)
        
    print("Measuring exact segment durations to sync subtitles...")
    durations = asyncio.run(get_exact_segment_durations(script, pilot_dir))
    
    srt_entries = []
    current_time = 0.0
    subtitle_index = 1
    
    for idx, item in enumerate(script):
        text = item["text"].strip()
        segment_duration = durations[idx]
        segment_end = current_time + segment_duration
        
        words = text.split()
        if not words:
            current_time = segment_end
            continue
            
        # Group words into chunks of 2-3 words (aiming for 3 words)
        chunks = []
        temp_chunk = []
        for word in words:
            temp_chunk.append(word)
            if len(temp_chunk) >= 3:
                chunks.append(" ".join(temp_chunk))
                temp_chunk = []
        if temp_chunk:
            chunks.append(" ".join(temp_chunk))
            
        # Distribute the segment's exact duration across the word chunks
        num_chunks = len(chunks)
        chunk_duration = segment_duration / num_chunks
        
        chunk_start = current_time
        for chunk in chunks:
            chunk_end = chunk_start + chunk_duration
            if chunk_end > segment_end:
                chunk_end = segment_end
                
            srt_entries.append(f"{subtitle_index}\n{format_timestamp(chunk_start)} --> {format_timestamp(chunk_end)}\n{chunk}\n")
            subtitle_index += 1
            chunk_start = chunk_end
            
        current_time = segment_end
        
    with open(srt_path, "w", encoding="utf-8") as f:
        f.writelines("\n".join(srt_entries))
    print(f"Subtitles successfully written to {srt_path}")

def render_video(image_path, audio_path, srt_path, output_path):
    """Run ffmpeg to stitch image and audio, embedding the SRT subtitles."""
    print("Starting video rendering using ffmpeg...")
    
    escaped_srt = srt_path.replace("\\", "/").replace(":", "\\:")
    
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", image_path,
        "-i", audio_path,
        "-vf", f"subtitles='{escaped_srt}':force_style='FontSize=24,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,BorderStyle=1,Outline=2'",
        "-c:v", "libx264", "-tune", "stillimage",
        "-c:a", "aac", "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        output_path
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"Success! Video rendered and saved to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error rendering video: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate audiobook video with friendly, short-phrase subtitles.")
    parser.add_argument("--audio", required=True, help="Path to input audio file (.mp3)")
    parser.add_argument("--script", required=True, help="Path to script JSON file")
    parser.add_argument("--image", required=True, help="Path to background image")
    parser.add_argument("--output", required=True, help="Path to output video file (.mp4)")
    
    args = parser.parse_args()
    
    # Generate path for temp SRT file
    srt_temp_path = args.output.replace(".mp4", ".srt")
    
    # Set pilot dir based on the script file location
    pilot_dir = os.path.dirname(args.script)
    
    # Step 1: Generate SRT File with exact durations
    generate_srt(args.script, srt_temp_path, pilot_dir)
    
    # Step 2: Render Final Video
    render_video(args.image, args.audio, srt_temp_path, args.output)
