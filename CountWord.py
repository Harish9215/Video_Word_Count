import streamlit as st  # For creating the web app
from youtube_transcript_api import YouTubeTranscriptApi  # To get video subtitles
from collections import Counter  # For counting words
import re  # For cleaning text

# Function to extract video ID from a YouTube link
def extract_video_id(url):
    if "youtu.be/" in url:  # Shortened YouTube links
        return url.split("youtu.be/")[-1].split("?")[0]
    elif "youtube.com/watch?v=" in url:  # Normal YouTube links
        return url.split("v=")[-1].split("&")[0]
    return None  # If the link is invalid

# Function to get the transcript of a video
def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)  # Fetch subtitles
        text = " ".join([entry['text'] for entry in transcript])  # Combine all lines into one
        return text
    except Exception as e:
        return None  # If subtitles are missing or the video is restricted

# Function to count words in the transcript
def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())  # Convert text to lowercase & split words
    return Counter(words)  # Count each word's occurrence

# Streamlit app UI
st.title("🔍 YouTube Video Word Search")  # App title

# Input field for YouTube link
youtube_url = st.text_input("🔗 Paste a YouTube Video URL:")

if youtube_url:  # If user enters a link
    video_id = extract_video_id(youtube_url)  # Extract video ID
    
    if video_id:
        st.write(f"✅ Video ID Found: `{video_id}`")  # Show extracted video ID

        transcript_text = get_transcript(video_id)  # Fetch subtitles
        
        if transcript_text:
            word_counts = count_words(transcript_text)  # Count words

            total_words = sum(word_counts.values())  # Get total words
            st.write(f"📖 **Total Words in Transcript:** {total_words}")  # Show total words

            # Input field to search for a word
            search_term = st.text_input("🔍 Type a word to search:")

            if search_term:
                search_count = word_counts.get(search_term.lower(), 0)  # Get word count
                st.write(f"**The word '{search_term}' appears {search_count} times in the video.**")  # Show result

        else:
            st.error("❌ Could not get transcript. The video may not have subtitles.")
    
    else:
        st.error("❌ Invalid YouTube URL. Please check and try again.")