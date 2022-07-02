## saavn-cli - Command-Line Music Downloader

Search, Download and Play your favorite songs right away from the command-line. High-Quality MP3 Files upto 320kbps bitrate with Metadata.
# Details

## [Download](https://github.com/wiz64/saavn-cli/releases)
<br>

> Developer : [@wiz64](https://github.com/wiz64) <br>
> Status : `In Development`<br>
> Version : `v 1.0.0`<br>
> Last Updated : `June 2022`<br>
> Based on : [Saavn Unofficial API](https://github.com/sumitkolhe/jiosaavn-api) By [@sumitkolhe](https://github.com/sumitkolhe)
---
Written in - Python <br>
Compatible with Linux, Windows, Android(Termux) & MacOS

# Features -
- ❤️ Free and Open Source
- 📙 A large library of tracks
- 🚀 Search and Download tracks directly from the command Line
- 🎶 Upto 320kbps MP3 files with Metadata
- 🎧 Download Multiple tracks at once

# Usage
Quickstart
- Compiled Executable

Download the executable binary file, and run it directly or from the terminal 

```
./saavn-cli search english songs
```
This will query the API for "english songs" and then display the results as a list. Enter comma-seperated numbers of tracks to download (eg. 4,6,12,15)

- Python Script (Lighter)

Universal :
```
python saavn-cli.py search english songs
```

# How it works ?

>When a user runs the script to search or download songs,<br> The script requests download links, album art, album details, etc from the unofficial API. It downloads the raw files and then compiles them using ffmpeg.

# Installation
### Requirements

- ffmpeg
- Python (v3)

1) Install FFMPEG
<br>To check if ffmpeg is properly installed, run<br>
`ffmpeg -version`<br>
Termius/Linux : `sudo apt install ffmpeg`<br>
[Download ffmpeg](https://ffmpeg.org/download.html)<br>
Windows users can copy `ffmpeg.exe` to `C:\Windows\System32` or any other $PATH Directory

2) Download Executable from [RELEASES PAGE](https://github.com/wiz64/saavn-cli/releases/)
Directly run commands relatively to the executables.

---
### Using Python Script:

 Python<br>
   Download and install Python v3+. Run

   `pip install -r requirements.txt`

execute script :

`python saavn-cli.py search:160 english songs`

### Compiling Binary :
With `pyinstaller`

`pip install -U pyinstaller`

`pyinstaller --onefile saavn-cli.py`

The Executable file will be saved to `dist` folder
<hr>

## Argument Parsing
Example Command :
```
./saavn-cli search:160 English Songs
```
- Here `saavn-cli` is argv[0], the script entry point
- `search:160` is argv[1], action and bitrate option, seperated by `: colon` as `ACTION:BITRATE`.<br>
- Action is Necessary but Bitrate is optional, 320 by default.
- `English Songs` - Rest Arguments are "terms" used to query the API in search action or Links/IDs seperated by spacing in download mode
# Actions
## Search
To search for songs available on Saavn and download MP3 to current directory.<br>
Syntax : `saavn-cli <s/search> <query>`<br>
Argument : `s or search`<br>
Bitrate can be added optionally.
Example:
```
./saavn-cli s:160 DJ Snake
```
---

## Multi Link Downloading (upcoming)

### From saavn song links or IDs : <br>


  Syntax : `saavn-cli download LINK1 LINK2 ID1 ID2`<br>
  Argument : `d or download`<br>
  Bitrate can be added optionally.<br>
  Supports Multiple Links/IDs<br>
  Example :

```
saavn-cli download IEBQ7- DFEHNB- SJADKEi
```
---

## Bitrate Settings
(Optional) To specify bitrate, pass the desired bitrate to right of `:` after action. <br>
Supported Values : `320 (default), 160, 96, 48, 12`<br>
Example:
```
saavn-cli search:96 Magneta Riddim
```
---
## Check for Updates
To check for updates, run command
```
saavn-cli update
```

---


### Todo -
 - adding link-download support
 - fix some bugs
 - album, artist search
  
# Footnotes 
I dedicate this project to a special one. Any guess who are they ?

Anyone is free to contribute to this project, fixing bugs, optimising code, improving documentation, testing, feedback, etc.

# License
Copyright &copy; 2022 wiz64

The source code of this tool has been licensed under `MIT License` Read the LICENSE File for more info.

# Copyright Disclaimer
I am not responsible for anything related to Third-Party copyright holders, This script comes with absolutely no warranties. Kindly use at your own risk. <br>We do not host or serve the Music files on our servers or accounts.<br> 
