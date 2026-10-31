
import yt_dlp
from pathlib import Path

def download_playlist():
    url = input("Enter YouTube playlist URL: ").strip()

    if not url:
        print("Error: Please enter a playlist URL.")
        return

    output_dir = Path("YouTube_Downloads")
    output_dir.mkdir(parents=True, exist_ok=True)

    options = {
        # Download best available audio
        "format": "bestaudio/best",

        # Convert audio to MP3
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],

        # Save in playlist order
        "outtmpl": str(
            output_dir / "%(playlist_index)03d - %(title)s.%(ext)s"
        ),

        # Skip previously downloaded items
        "download_archive": str(output_dir / "archive.txt"),

        # Continue if an item is unavailable
        "ignoreerrors": True,

        "noplaylist": False,
    }

    try:
        with yt_dlp.YoutubeDL(options) as downloader:
            downloader.download([url])

        print(f"\nFinished! MP3 files are in: {output_dir.resolve()}")

    except Exception as error:
        print(f"Download error: {error}")


if __name__ == "__main__":
    download_playlist()
