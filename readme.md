## saavn-cli - Command-Line Music Downloader

Search, Download and Play your favorite songs right away from the command-line. High-Quality MP3 Files upto 320kbps bitrate with Metadata. <br>
<img src="https://user-images.githubusercontent.com/67432394/205225612-f6fb25ac-92f9-4926-863b-e5e2518851ff.png" width="100px" height="100px">
# Details

## [Download](https://github.com/wiz64/saavn-cli/releases)
<br>

> Developer : [@wiz64](https://github.com/wiz64) <br>
> Status : `In Development`<br>
> Version : `v 1.2.0`<br>
> Last Updated : `November 2022`<br>

---
Written in - Python <br>
Compatible with Linux, Windows, Android(Termux) & MacOS

# Features -
- ❤️ Free and Open Source
- 📙 A large library of tracks
- 🚀 Search and Download tracks directly
- ⚙️ Cross Platform - Linux, Windows, MacOS, Android(termux)
- 🎶 Upto 320kbps MP3 files with Metadata
- 🎧 Download Multiple tracks at once

# Usage
Quickstart / Compiled
- [Install ffmpeg](#install-ffmpeg)
- Download, Extract zip and run
```
chmod +x saavn-cli
./saavn-cli search english songs
```
Enter comma-seperated numbers for the tracks you want to download - `1,4,12,15`
..There you go !

<img src="https://user-images.githubusercontent.com/67432394/203235138-02f43690-1eb6-4660-9e7e-d3a12904e3c2.png" width="275px">

---
- Python Script 

Universal :
```
pip install -r requirements.txt
python saavn-cli.py search english songs
```

# How it works ?

>When a user runs the script to search or download songs,<br> The script requests download links, album art, album details, etc from the unofficial API. It downloads the raw files and then compiles them using ffmpeg.

### Requirements

- ffmpeg
- Python (v3)


#### Install FFMPEG
<br>To check if ffmpeg is properly installed, run<br>
`ffmpeg -version`<br>
[Download ffmpeg](https://ffmpeg.org/download.html)<br>
- Termius/Linux : `sudo apt install ffmpeg`<br>
- MacOS (Homebrew) : `brew install ffmpeg` <br> check [brew.sh](https://brew.sh) <br>
- Windows users can copy `ffmpeg.exe` to `C:\Windows\System32` or any other `$PATH` Directory


---

### Compiling Binary :
With `pyinstaller`

`pip install -U pyinstaller`
`python3 -m PyInstaller --icon=icon.ico --onefile saavn-cli.py -n saavn-cli`

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
 - album, artist search
  
# Footnotes 
I dedicate this project to a special one. Any guess who are they ?

Anyone is free to contribute to this project, fixing bugs, optimising code, improving documentation, testing, feedback, etc.

# License
Copyright &copy; 2022 wiz64

The source code of this tool has been licensed under `MIT License` Read the LICENSE File for more info.

# Copyright Disclaimer
I am not responsible for anything related to Third-Party copyright holders, This script comes with absolutely no warranties. Kindly use at your own risk. <br>We do not host or serve the Music files on our servers or accounts.<br> 
