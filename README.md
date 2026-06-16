# aimp-browser-overlay
AIMP Now playing with UI for OBS

## What is this

This project shows the currently playing track from AIMP in a browser overlay for OBS.

The overlay updates automatically every 30 seconds.

Tested on Windows, using
- Python 3.10 - 3.14
- AIMP v5.40

## Preview

![Now Playing Preview](image.png)

## Setup

1. Put everything into one folder, open console there
2. Create venv using `python -m venv venv`
3. Activate venv using `venv\Scripts\Activate`
4. Install requirements using `pip install -r requirements.txt`

Open AIMP player and then start through bat

A local URL will be generated after startup, running on `http://127.0.0.1:5000`

### Add to OBS
- Open OBS Studio
- Add new source: Browser
- Paste the generated URL into the Browser Source

## How it works

The script reads current track information from AIMP and exposes it through a local web page.

OBS displays this page as a browser overlay.

Data refresh interval: 30 seconds (you can change it if needed, but on my opinion 30 seconds is enought for such program)

## Notes

- Make sure AIMP is running before starting the script
- If nothing shows up, check the path in start.bat
- Adjust OBS Browser Source resolution if needed

## Known Issues

- The server may occasionally stop responding and require a restart.
