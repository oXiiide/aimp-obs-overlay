import os
import time
from threading import Thread
from flask import Flask, send_from_directory
import psutil
from mutagen import File
from mutagen.id3 import APIC

app = Flask(__name__)

COVER_FILE = "cover.jpg"
TRACK_FILE = "track_info.txt"

def find_aimp_file():
    for proc in psutil.process_iter(["name", "open_files"]):
        if proc.info["name"] and proc.info["name"].lower() == "aimp.exe":
            files = proc.info["open_files"]
            if files:
                for f in files:
                    if f.path.lower().endswith((".mp3", ".flac", ".m4a")):
                        return f.path
    return None

def update_nowplaying():
    while True:
        try:
            time.sleep(5)
            track_path = find_aimp_file()
            if track_path and os.path.exists(track_path):
                audio = File(track_path)
                artist = str(audio.tags.get("TPE1")) if audio.tags.get("TPE1") else "Unknown Artist"
                title = str(audio.tags.get("TIT2")) if audio.tags.get("TIT2") else "Unknown Title"

                # Обложка
                for tag in audio.tags.values():
                    if isinstance(tag, APIC):
                        with open(COVER_FILE, "wb") as f:
                            f.write(tag.data)
                        break

                # Пишем artist/title
                with open(TRACK_FILE, "w", encoding="utf-8") as f:
                    f.write(f"{artist}\n{title}")

        except Exception as e:
            print("Ошибка:", e)
        time.sleep(10)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/cover.jpg")
def cover():
    if os.path.exists(COVER_FILE):
        return send_from_directory(".", COVER_FILE)
    return "", 404

@app.route("/track_info.txt")
def track_info():
    if os.path.exists(TRACK_FILE):
        return send_from_directory(".", TRACK_FILE)
    return "", 404

if __name__ == "__main__":
    Thread(target=update_nowplaying, daemon=True).start()
    app.run(port=5000)
