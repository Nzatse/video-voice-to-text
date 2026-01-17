#!/usr/bin/env python3
"""
YouTube Video to Text Transcriber

This script downloads a YouTube video, extracts the audio, 
and transcribes it to text using OpenAI's Whisper model.
"""

import argparse
import os
import sys
import whisper
import yt_dlp


def download_youtube_audio(url, output_dir="downloads"):
    """
    Download audio from a YouTube video.
    
    Args:
        url (str): YouTube video URL
        output_dir (str): Directory to save the audio file
        
    Returns:
        str: Path to the downloaded audio file
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'quiet': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading audio from: {url}")
            info = ydl.extract_info(url, download=True)
            # Get the output filename
            audio_file = os.path.join(output_dir, f"{info['title']}.mp3")
            print(f"Audio downloaded to: {audio_file}")
            return audio_file
    except Exception as e:
        print(f"Error downloading video: {e}")
        sys.exit(1)


def transcribe_audio(audio_file, model_name="base", language=None):
    """
    Transcribe audio file to text using Whisper.
    
    Args:
        audio_file (str): Path to the audio file
        model_name (str): Whisper model to use (tiny, base, small, medium, large)
        language (str): Language code (e.g., 'en', 'es', 'fr') or None for auto-detect
        
    Returns:
        dict: Transcription result containing text and metadata
    """
    print(f"Loading Whisper model: {model_name}")
    model = whisper.load_model(model_name)
    
    print(f"Transcribing audio file: {audio_file}")
    
    # Set transcription options
    transcribe_options = {}
    if language:
        transcribe_options['language'] = language
    
    result = model.transcribe(audio_file, **transcribe_options)
    
    print("Transcription complete!")
    return result


def save_transcription(result, output_file):
    """
    Save transcription result to a text file.
    
    Args:
        result (dict): Transcription result from Whisper
        output_file (str): Path to save the transcription
    """
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_file)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result['text'])
    
    print(f"Transcription saved to: {output_file}")


def main():
    """Main function to orchestrate the transcription process."""
    parser = argparse.ArgumentParser(
        description='Transcribe YouTube videos to text using Whisper AI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s https://www.youtube.com/watch?v=VIDEO_ID
  %(prog)s https://www.youtube.com/watch?v=VIDEO_ID -o output.txt
  %(prog)s https://www.youtube.com/watch?v=VIDEO_ID -m small -l en
        """
    )
    
    parser.add_argument('url', help='YouTube video URL')
    parser.add_argument('-o', '--output', 
                        default='transcription.txt',
                        help='Output file for transcription (default: transcription.txt)')
    parser.add_argument('-m', '--model', 
                        default='base',
                        choices=['tiny', 'base', 'small', 'medium', 'large'],
                        help='Whisper model to use (default: base). Larger models are more accurate but slower.')
    parser.add_argument('-l', '--language',
                        help='Language code (e.g., en, es, fr). Leave empty for auto-detection.')
    parser.add_argument('-d', '--download-dir',
                        default='downloads',
                        help='Directory to save downloaded audio (default: downloads)')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("YouTube Video to Text Transcriber")
    print("=" * 60)
    
    # Step 1: Download audio from YouTube
    audio_file = download_youtube_audio(args.url, args.download_dir)
    
    # Step 2: Transcribe the audio
    result = transcribe_audio(audio_file, args.model, args.language)
    
    # Step 3: Save the transcription
    save_transcription(result, args.output)
    
    # Display the transcription
    print("\n" + "=" * 60)
    print("TRANSCRIPTION:")
    print("=" * 60)
    print(result['text'])
    print("=" * 60)
    
    print(f"\nDone! Transcription saved to: {args.output}")


if __name__ == "__main__":
    main()
