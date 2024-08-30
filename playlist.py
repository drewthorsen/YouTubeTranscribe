import os
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube, Playlist
import sys
import re

# Check if the playlist URL is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python playlist.py <playlist_url>")
    sys.exit(1)

# Get the playlist URL from the command-line arguments
playlist_url = sys.argv[1]

# Fetch the playlist
playlist = Playlist(playlist_url)

# Define a function to format text


def format_text(text, sentences_per_paragraph=3):
    sentences = text.split('. ')
    formatted_text = ""
    sentence_count = 0

    for sentence in sentences:
        formatted_text += sentence.strip() + '. '
        sentence_count += 1

        if sentence_count >= sentences_per_paragraph:
            formatted_text += "\n\n"
            sentence_count = 0

    return formatted_text.strip()

# Define a function to fetch and save transcripts


def fetch_and_save_transcript(video_id, video_title):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([entry['text'] for entry in transcript])
    formatted_text = format_text(full_text)

    # Replace colons with underscores in the video title
    safe_title = re.sub(r':', '_', video_title)

    # Specify the path to the Downloads folder
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    output_file = os.path.join(downloads_path, f"{safe_title}_transcript.txt")

    # Save the transcript to a file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(formatted_text)

    print(f"Transcript has been saved to {output_file}")


# Iterate through each video in the playlist
for video in playlist.videos:
    try:
        video_id = video.video_id
        video_title = video.title.replace(" ", "_").replace("/", "_")
        print(f"Transcribing: {video.title}")
        fetch_and_save_transcript(video_id, video_title)
    except Exception as e:
        print(f"Could not transcribe video {video.title}: {e}")
