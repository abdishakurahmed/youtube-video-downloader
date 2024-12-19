from tqdm import tqdm
import yt_dlp
import os

class ProgressBar:
    def __init__(self):
        self.pbar = None

    def hook(self, d):
        if d["status"] == "downloading":
            if not self.pbar:
                total_size = float(d.get("total_bytes", 0))
                self.pbar = tqdm(total=total_size, unit="B", unit_scale=True)
            downloaded = float(d.get("downloaded_bytes", 0))
            self.pbar.n = downloaded
            self.pbar.refresh()
        elif d["status"] == "finished":
            if self.pbar:
                self.pbar.close()
                print(f"Download complete! Saved to {d['filename']}")

# Prompt for custom download folder
download_folder = input("Enter the path to the download folder (leave blank for current directory): ").strip()

# Use the current directory if no folder is specified
if not download_folder:
    download_folder = os.getcwd()

# Ensure the folder exists
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Video URL
url = "Enter youtube video url here"

progress = ProgressBar()
ydl_opts = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
    "merge_output_format": "mp4",
    "progress_hooks": [progress.hook],
    "outtmpl": os.path.join(download_folder, "%(title)s.%(ext)s"),  # Save file to the specified folder
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
