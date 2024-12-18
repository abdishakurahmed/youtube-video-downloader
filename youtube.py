import yt_dlp

# Video URL
video_url = "https://www.youtube.com/watch?v=OUM6XmhViN4"

# Download options
ydl_opts = {
    "format": "bestvideo[height=720]+bestaudio/best",  # Select 720p video and best audio
    "merge_output_format": "mp4",                     # Merge video and audio into MP4 format
    "outtmpl": "%(title)s.%(ext)s",                   # Save as video title
    "progress_hooks": [                               # Hook to show download progress
        lambda d: print(f"Status: {d['status']}, Downloaded: {d.get('downloaded_bytes', 0)} bytes")
    ],
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
except Exception as e:
    print(f"Error: {e}")
