# 🎵 YouTube Playlist Downloader (MP3)

A simple and efficient Python script to download entire YouTube playlists and convert them to high-quality MP3 files.

## ✨ Features

- **Batch Download**: Download complete YouTube playlists with one command
- **Auto-Convert**: Automatically converts videos to MP3 (192kbps) using FFmpeg
- **Smart Ordering**: Files are saved with playlist index numbers (001, 002, etc.)
- **Resume Support**: Skips previously downloaded items using an archive file
- **Error Handling**: Continues downloading even if some videos are unavailable/private
- **Organized Output**: All files saved in a dedicated `YouTube_Downloads` folder

## 📋 Requirements

- **Python**: 3.7 or higher
- **FFmpeg**: Required for audio conversion (must be installed and added to PATH)
- **yt-dlp**: Python library for downloading

## 🚀 Installation

1. **Clone or download** this repository
2. **Install dependencies**:
   ```bash
   pip install yt-dlp
   ```
3. **Install FFmpeg**:
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) or use `winget install ffmpeg`
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg` (Debian/Ubuntu) or `sudo dnf install ffmpeg` (Fedora)

## 💻 Usage

Run the script:

```bash
python playlist_downloader.py
```

When prompted, paste the YouTube playlist URL:

```
Enter YouTube playlist URL: https://www.youtube.com/playlist?list=PLxxxxxxxxxxxxx
```

The download will start automatically. Files will be saved in the `YouTube_Downloads` folder.

## 📁 Output Structure

```
YouTube_Downloads/
├── 001 - Song Title One.mp3
├── 002 - Song Title Two.mp3
├── 003 - Song Title Three.mp3
└── archive.txt (tracks downloaded history)
```

## ⚙️ Configuration

You can modify these options in the script:

| Option | Default | Description |
|--------|---------|-------------|
| `preferredquality` | `192` | MP3 bitrate (128, 192, 256, 320) |
| `outtmpl` | `%(playlist_index)03d - %(title)s.%(ext)s` | File naming pattern |
| `download_archive` | `archive.txt` | File to track downloaded items |

## 🛠️ Troubleshooting

**"FFmpeg not found" error:**
- Make sure FFmpeg is installed and added to your system PATH
- Restart your terminal/IDE after installing FFmpeg

**"Video unavailable" errors:**
- The script automatically skips unavailable/private videos and continues with the rest

**Slow downloads:**
- Check your internet connection
- YouTube may throttle downloads; try again later

## ⚠️ Disclaimer

This tool is for personal use only. Downloading copyrighted content may violate YouTube's Terms of Service and local laws. Only download content you own or that is freely available for download.

## 📄 License

This project is open source and available under the MIT License.
