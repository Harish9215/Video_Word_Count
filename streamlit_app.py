import streamlit as st
import os
import re

from utils.downloader import download_audio
from utils.transcriber import transcribe_audio
from utils.text_analysis import count_words, search_word
from config import TEMP_AUDIO_PATH, TRANSCRIPT_DIR

# --------------- Helper ----------------
def is_valid_youtube_url(url):
    pattern = r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+'
    return re.match(pattern, url)

# --------------- App Layout ---------------
st.set_page_config(page_title="YouTube Transcript Generator", page_icon="🎙️", layout="centered")

st.markdown("<h1 style='text-align: center;'>🎙️ YouTube Transcript Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Extract transcripts from any YouTube video — even if it has no subtitles!</p>", unsafe_allow_html=True)

st.divider()

youtube_url = st.text_input("📎 Paste a YouTube Video URL below:")

if youtube_url:
    if not is_valid_youtube_url(youtube_url):
        st.error("❌ Please enter a valid YouTube URL (youtube.com or youtu.be)")
        st.stop()

    with st.spinner("📥 Downloading audio..."):
        audio_path = download_audio(youtube_url)

    if audio_path and os.path.exists(audio_path):
        with st.spinner("🧠 Transcribing audio..."):
            transcript_text = transcribe_audio(audio_path)

        if transcript_text:
            st.success("✅ Transcription complete!")

            video_id = youtube_url.split("v=")[-1].split("&")[0]
            transcript_file = os.path.join(TRANSCRIPT_DIR, f"{video_id}.txt")
            with open(transcript_file, "w") as f:
                f.write(transcript_text)

            word_counts = count_words(transcript_text)
            total_words = sum(word_counts.values())

            st.info(f"📝 **Transcript Stats:** `{total_words}` total words")

            # Layout: search on left, download on right
            col1, col2 = st.columns(2)
            with col1:
                search_term = st.text_input("🔍 Search for a word:")
                if search_term:
                    count = search_word(word_counts, search_term)
                    st.write(f"'{search_term}' appears **{count}** times.")

            with col2:
                st.download_button("⬇️ Download Transcript", transcript_text, file_name="transcript.txt")

            with st.expander("📖 Click to expand full transcript"):
                st.write(transcript_text)
        else:
            st.error("❌ Transcription failed.")
    else:
        st.error("❌ Audio file not found. Try a different video.")

st.markdown(
    """
    <hr style="margin-top: 2em;" />
    <div style='text-align: center; color: gray; font-size: 0.9em;'>
        Made with ❤️ by <strong>Harish</strong>
    </div>
    """,
    unsafe_allow_html=True
)      