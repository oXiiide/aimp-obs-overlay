# aimp-browser-overlay
AIMP Now playing with UI for OBS

## What is this

This project shows the currently playing track from AIMP in a browser overlay for OBS.

The overlay updates automatically every 30 seconds.

## Preview

![Now Playing Preview](image.png)

## Requirements

- AIMP player installed and running
- OBS Studio
- Windows (start.bat is used to run the overlay server/script)

## Setup

### 1. Configure path
Open start.bat and change the path to your project or script location.

This is required for the overlay to work correctly.

### 2. Start AIMP
Launch AIMP and start playing music.

### 3. Run start script
Open start.bat

A local URL will be generated after startup.

### 4. Add to OBS
- Open OBS Studio
- Add new source: Browser
- Paste the generated URL into the Browser Source

## How it works

The script reads current track information from AIMP and exposes it through a local web page.

OBS displays this page as a browser overlay.

Data refresh interval: 30 seconds

## Notes

- Make sure AIMP is running before starting the script
- If nothing shows up, check the path in start.bat
- Adjust OBS Browser Source resolution if needed

## Known Issues

- The server may occasionally stop responding and require a restart.
