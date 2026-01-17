# video-voice-to-text

A Python application that downloads YouTube videos and transcribes the audio to text using OpenAI's Whisper AI model.

## Features

- Download audio from any YouTube video
- Transcribe speech to text using state-of-the-art Whisper AI
- Support for multiple languages with auto-detection
- Multiple model sizes for different accuracy/speed trade-offs
- Simple command-line interface

## Requirements

- Python 3.8 or higher
- ffmpeg (required for audio processing)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Nzatse/video-voice-to-text.git
cd video-voice-to-text
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install ffmpeg:
   - **Ubuntu/Debian**: `sudo apt-get install ffmpeg`
   - **MacOS**: `brew install ffmpeg`
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html)

## Usage

Basic usage:
```bash
python main.py https://www.youtube.com/watch?v=VIDEO_ID
```

Specify output file:
```bash
python main.py https://www.youtube.com/watch?v=VIDEO_ID -o my_transcription.txt
```

Use a larger model for better accuracy:
```bash
python main.py https://www.youtube.com/watch?v=VIDEO_ID -m small
```

Specify language (faster than auto-detection):
```bash
python main.py https://www.youtube.com/watch?v=VIDEO_ID -l en
```

### Command-Line Options

- `url` (required): YouTube video URL
- `-o, --output`: Output file for transcription (default: transcription.txt)
- `-m, --model`: Whisper model to use: tiny, base, small, medium, large (default: base)
- `-l, --language`: Language code (e.g., en, es, fr) for faster transcription
- `-d, --download-dir`: Directory to save downloaded audio (default: downloads)

### Model Sizes

The application supports different Whisper model sizes. Larger models are more accurate but slower:

| Model  | Parameters | Relative Speed | Description |
|--------|------------|----------------|-------------|
| tiny   | 39 M       | ~32x           | Fastest, least accurate |
| base   | 74 M       | ~16x           | Good balance (default) |
| small  | 244 M      | ~6x            | Better accuracy |
| medium | 769 M      | ~2x            | High accuracy |
| large  | 1550 M     | 1x             | Best accuracy, slowest |

## Examples

Transcribe an English video with high accuracy:
```bash
python main.py https://www.youtube.com/watch?v=dQw4w9WgXcQ -m medium -l en -o rick_astley.txt
```

Quick transcription with the tiny model:
```bash
python main.py https://www.youtube.com/watch?v=VIDEO_ID -m tiny
```

## How It Works

1. **Download**: Uses yt-dlp to download the audio stream from YouTube
2. **Extract**: Converts the audio to MP3 format using ffmpeg
3. **Transcribe**: Uses OpenAI's Whisper model to transcribe the audio to text
4. **Save**: Outputs the transcription to a text file

## Troubleshooting

**Error: ffmpeg not found**
- Make sure ffmpeg is installed and available in your PATH

**Error downloading video**
- Check that the YouTube URL is valid and accessible
- Some videos may be restricted or unavailable in your region

**Out of memory error**
- Try using a smaller model (e.g., tiny or base)
- For very long videos, consider splitting them first

## License

This project is open source and available under the MIT License.