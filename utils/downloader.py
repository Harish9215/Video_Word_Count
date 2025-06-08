import os
import yt_dlp
from config import FFMPEG_PATH, TEMP_AUDIO_PATH

def download_audio(video_url):
    output_path = TEMP_AUDIO_PATH  # no .wav yet
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'ffmpeg_location': FFMPEG_PATH,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # Final path will be output_path + ".wav"
    final_audio = output_path + ".wav"
    return final_audio if os.path.exists(final_audio) else None

