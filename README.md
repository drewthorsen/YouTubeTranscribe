# YouTubeTranscribe
This repository contains two command-line tools to help you easily extract and save transcripts from YouTube videos and playlists. Both tools are implemented in Python and can be executed via simple batch commands.
README

## Command-Line Tools for YouTube Transcript Extraction

This repository contains two command-line tools to help you easily extract and save transcripts from YouTube videos and playlists. Both tools are implemented in Python and can be executed via simple batch commands.

### 1. `transcript`: Extract Transcript from a Single YouTube Video

#### **Description**:
The `transcript` command fetches the transcript from a single YouTube video and saves it as a text file in your Downloads folder. The transcript is formatted for readability, with paragraph breaks every few sentences.

`https://www.youtube.com/watch?v= **HgL_REJe4LU**`
#### **Usage**:
```bash
transcript <YouTube_Video_ID>
```

#### **Example**:
```bash
transcript fiIaqAYPzFk
```

#### **Output**:
- The transcript will be saved in the Downloads folder as a text file named after the video title.
- Example output file: `C:\Users\<YourUsername>\Downloads\<Video_Title>_transcript.txt`

### 2. `playlist`: Extract Transcripts from All Videos in a YouTube Playlist

#### **Description**:
The `playlist` command fetches transcripts for all videos in a specified YouTube playlist. Each transcript is saved individually in your Downloads folder, named after the corresponding video title.

#### **Usage**:
```bash
playlist "<YouTube_Playlist_URL>"
```

#### **Example**:
```bash
playlist "https://www.youtube.com/playlist?list=PLIFyRwBY_4bRLmKfP1KnZA6rZbRHtxmXi"
```

#### **Output**:
- Each transcript is saved in the Downloads folder as a text file, named after the video title.
- Example output files:
  - `C:\Users\<YourUsername>\Downloads\<Video_Title_1>_transcript.txt`
  - `C:\Users\<YourUsername>\Downloads\<Video_Title_2>_transcript.txt`

### **System Requirements**:
- **Python 3.x** installed on your system.
- Required Python libraries: `pytube`, `youtube-transcript-api`.

### **Installation Instructions**:
1. **Install Python Libraries**:
   - Run the following commands to install the necessary libraries:
     ```bash
     pip install pytube
     pip install youtube-transcript-api
     ```

2. **Batch Files Setup**:
   - Ensure that `transcript.bat` and `playlist.bat` are correctly set up in your `C:\Scripts\` directory.

3. **Environment Variables**:
   - Add `C:\Scripts` to your system's PATH environment variable to allow the use of these commands globally from any directory in the Command Prompt.



### **Troubleshooting**:
- **URL or Video ID Issues**: Make sure that the video ID or playlist URL is correctly formatted and enclosed in quotes if it contains special characters.
- **PATH Configuration**: Ensure that `C:\Scripts` is correctly added to the PATH environment variable, and that the batch files are located in their respective directory.
'`C:\Scripts\playlist`
'`C:\Scripts\transcript`'
### **Contributors**:
Drew Thorsen: Original script and command setup.
