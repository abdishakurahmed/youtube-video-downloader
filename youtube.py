from tqdm import tqdm
import yt_dlp

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
                print("Download complete!")

url = "https://www.youtube.com/watch?v=g8p7rYscp04.com/watch?v=-hlwlML6pEg"

progress = ProgressBar()
ydl_opts = {
    "format": "bestvideo[height<=720]+bestaudio/best",
    "progress_hooks": [progress.hook],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
