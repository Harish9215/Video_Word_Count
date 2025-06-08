
# 🎙️ YouTube Transcript Generator (No Subtitles Needed)

A Streamlit-based web app that generates a full transcript from **any YouTube video**, even if it doesn't have built-in subtitles. This tool uses OpenAI's Whisper for state-of-the-art speech recognition and `yt-dlp` for efficient audio extraction.

-----

## ✨ Features

  - **🔗 Universal URL Support**: Works with any public YouTube video URL.
  - **🎧 Smart Audio Extraction**: Downloads only the audio stream using `yt-dlp` for speed and efficiency.
  - **🧠 High-Accuracy Transcription**: Leverages OpenAI's `whisper` model to transcribe speech with remarkable precision.
  - **🔍 Text Analysis Tools**: Instantly search the transcript for keywords and view a word frequency counter.
  - **📄 Easy Export**: Preview the full transcript in the app and download it as a `.txt` file with a single click.
  - **✅ No Subtitles Required**: Generates transcripts from the audio itself, making it invaluable for videos without captions.

-----

## ⚙️ How It Works

The application follows a simple, powerful pipeline:

1.  **Audio Download**: You provide a YouTube URL. `yt-dlp` downloads the audio stream and saves it as a temporary `.wav` file.
2.  **Transcription**: The audio data is fed into the `whisper` model, which processes it and generates the transcript.
3.  **Analysis & Display**: The generated text is displayed in the Streamlit interface, where you can search, analyze, and download it.

-----

## 📁 Project Structure

The repository is organized to separate concerns, making it easy to maintain and extend.

```
youtube-transcript-app/
├── .gitignore
├── README.md
├── requirements.txt
├── streamlit_app.py      # Main Streamlit application
├── config.py             # Handles paths and ffmpeg configuration
├── utils/
│   ├── __init__.py
│   ├── downloader.py       # Manages YouTube audio downloads
│   ├── transcriber.py      # Handles Whisper transcription logic
│   └── text_analysis.py    # Powers word search and frequency counting
├── data/
│   └── transcripts/      # Default directory for saved .txt transcripts
└── temp/
    └── audio.wav         # Temporary storage for the downloaded audio file
```

-----

## 📦 Installation

To run this application locally, you'll need Python, Pip, and `ffmpeg`.

### 1\. Prerequisites

  - **Python 3.8+** and **Pip**
  - **Git** for cloning the repository.
  - **FFmpeg**: A crucial dependency for audio processing.
      - **macOS (via Homebrew)**:
        ```bash
        brew install ffmpeg
        ```
      - **Ubuntu (via APT)**:
        ```bash
        sudo apt update && sudo apt install ffmpeg
        ```
      - **Windows (via Chocolatey or direct download)**:
        ```bash
        choco install ffmpeg
        ```
        Alternatively, [download the binaries](https://ffmpeg.org/download.html), extract them (e.g., to `C:\ffmpeg`), and add the `bin` directory (e.g., `C:\ffmpeg\bin`) to your system's `PATH`.

### 2\. Setup Steps

Clone the repository, set up a virtual environment, and install the required Python packages.

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/youtube-transcript-app.git
cd youtube-transcript-app

# 2. Create and activate a virtual environment
# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
.\venv\Scripts\activate

# 3. Install the dependencies
pip install -r requirements.txt
```

-----

## 🚀 Usage

With all dependencies installed, running the app is as simple as:

```bash
streamlit run streamlit_app.py
```

Your web browser should automatically open a new tab with the running Streamlit application. Just paste a YouTube video URL into the input box and click the "Generate Transcript" button to start.

-----

## 🧠 Powered By

This project is built with several incredible open-source tools:

  - [**Streamlit**](https://streamlit.io/): For building the interactive web interface.
  - [**OpenAI Whisper**](https://github.com/openai/whisper): For accurate speech-to-text transcription.
  - [**yt-dlp**](https://github.com/yt-dlp/yt-dlp): For downloading video audio efficiently.
  - [**PyTorch**](https://pytorch.org/): As a backend for running the Whisper model.

-----

## 📃 License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it as you see fit. See the `LICENSE` file for more details.
