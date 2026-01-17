#!/usr/bin/env python3
"""
Example usage of the YouTube Video to Text Transcriber

This script demonstrates how to use the main.py script programmatically.
"""

import subprocess
import sys


def run_transcription(youtube_url, output_file="transcription.txt", model="base"):
    """
    Run the transcription script with given parameters.
    
    Args:
        youtube_url (str): YouTube video URL
        output_file (str): Output file path
        model (str): Whisper model to use
    """
    cmd = [
        sys.executable,
        "main.py",
        youtube_url,
        "-o", output_file,
        "-m", model
    ]
    
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    
    return result.returncode == 0


if __name__ == "__main__":
    # Example: Transcribe a sample YouTube video
    # Replace with an actual YouTube URL to test
    
    example_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    
    print("=" * 60)
    print("Example: YouTube Video Transcription")
    print("=" * 60)
    print(f"\nThis will transcribe the video at: {example_url}")
    print("\nNote: Replace the URL with a real video you want to transcribe.")
    print("\nUsage from command line:")
    print(f"  python main.py {example_url}")
    print(f"  python main.py {example_url} -o my_output.txt -m small")
    print("\n" + "=" * 60)
    
    # Uncomment the line below to actually run the transcription
    # success = run_transcription(example_url, "example_output.txt", "tiny")
