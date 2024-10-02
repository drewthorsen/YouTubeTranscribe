import os
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import sys
import re

# Check if the video ID is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python transcript.py <video_id>")
    sys.exit(1)

# Extract the video ID from the URL or directly use the video ID
def get_video_id(url_or_id):
    # Check if input is just the video ID
    if len(url_or_id) == 11 and re.match(r"^-?[0-9A-Za-z_-]{11}$", url_or_id):  # Allow a dash at the start
        return url_or_id
    # If it's a full YouTube URL, extract the video ID using regex
    video_id_match = re.search(r"(?:v=|\/)(-?[0-9A-Za-z_-]{11}).*", url_or_id)  # Allow a dash at the start
    if video_id_match:
        return video_id_match.group(1)
    else:
        raise ValueError("Invalid YouTube URL or video ID")


# Get the video ID from the command-line arguments
video_id = get_video_id(sys.argv[1])

# Fetch the video title
youtube_url = f"https://www.youtube.com/watch?v={video_id}"
yt = YouTube(youtube_url)
video_title = yt.title.replace(" ", "_").replace("/", "_")  # Replace spaces and slashes for file naming

# Function to format text into paragraphs with a specified number of sentences
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

# Function to fetch and save the transcript
def fetch_and_save_transcript(video_id, video_title):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([entry['text'] for entry in transcript])
    formatted_text = format_text(full_text)

    # Replace colons with underscores in the video title
    safe_title = re.sub(r'[:\\/|*?"<>]', '_', video_title)

    # Specify the path to the Downloads folder
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    output_file = os.path.join(downloads_path, f"{safe_title}_transcript.txt")

    # Save the transcript to a file
    with open(output_file, 'w') as file:
        file.write(formatted_text)

    print(f"Transcript has been saved to {output_file}")

# Fetch and save the transcript
fetch_and_save_transcript(video_id, video_title)
