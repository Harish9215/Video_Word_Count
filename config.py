import os

# Path to ffmpeg directory (must contain both ffmpeg and ffprobe)
FFMPEG_PATH = "/opt/homebrew/bin"  # Change this path as per your OS

# Output paths
# TEMP_AUDIO_PATH = os.path.join("temp", "audio.wav")
TRANSCRIPT_DIR = os.path.join("data", "transcripts")
TEMP_AUDIO_PATH = os.path.join("temp", "audio")


# Ensure directories exist
os.makedirs("temp", exist_ok=True)
os.makedirs(TRANSCRIPT_DIR, exist_ok=True)
