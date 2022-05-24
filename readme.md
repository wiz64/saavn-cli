## Saavn-cli - Command-Line Music Downloader

Search, Download and Play your favorite songs right away from the command-line. High-Quality MP3 Files upto 320kbps bitrate with Metadata.

# Details

[Download Here](https://github.com/wiz64/saavn-cli/releases)
> Developer : [@wiz64](https://github.com/wiz64) <br>
> Status : `In Development`<br>
> Version : `v 0.0.1`<br>
> Last Updated : `May 2022`<br>
> Based on : [Saavn Unofficial API](https://github.com/sumitkolhe/jiosaavn-api) By [@sumitkolhe](https://github.com/sumitkolhe)
---
Written in - Python <br>
Compatible with Linux, Windows & MacOS

# Features -
- A large library of songs
- Search and Download songs directly from the command Line
- Upto 320kbps MP3 files with Metadata

# Usage
Quickstart
```
saavn-cli search Arijit Singh
```
This will query the API for "Arijit Singh" and then display the results as a list. You can select from the list for the song to download.

Windows users run `python saavn-cli`. Due to a VSCode bug, you may need to add `python ` prefix before commands, if VSCode is installed.

# How it works ?

>When a user runs the script to search or download songs,<br> The script requests download links, album art, album details, etc from the unofficial API. It downloads the raw files and then compiles them using ffmpeg.

# Installation
### Requirements

- ffmpeg
- Python
  #### Py Modules
  `requests`
  


1) Install FFMPEG & Python
<br>To check if ffmpeg is properly installed, run<br>
`ffmpeg -version`<br>
[Download ffmpeg](https://ffmpeg.org/download.html)<br>
Windows users can copy `ffmpeg.exe` to `C:\Windows\System32`
2) Python<br>
   Download from [Python.org](https://www.python.org/)<br>
   run command<br>
   (you can use cmd/git-bash on windows)<br>
   `pip install requests`

3) Download `saavn-cli` file<br>
   `chmod +x saavn-cli` make it executable<br>
   test by running `./saavn-cli`<br>
   (optional) save to any $PATH directory for direct global access<br>
LINUX : `/usr/bin/`<br>
Windows : `C:\Windows\System32\`<br>
Check [RELEASES](https://github.com/wiz64/saavn-cli/releases/) or clone this repository
<hr>

## Argument Parsing
Example Command :
```
saavn-cli search:160 Imagine Dragons
```
- Here `saavn-cli` is argv[0], the script entry point
- `search:160` is argv[1], action and bitrate option, seperated by `: colon` as `ACTION:BITRATE`.<br>
- Action is Necessary but Bitrate is optional, 320 by default.
- `Imagine Dragons` - Rest Arguments are "terms" used to query the API in search action or Links/IDs seperated by spacing in download mode
# Actions
## Search
To search for songs available on Saavn and download MP3 to current directory.<br>
Syntax : `saavn-cli <s/search> <query>`<br>
Argument : `s or search`<br>
Bitrate can be added optionally.
Example:
```
saavn-cli s:160 DJ Snake
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
saavn-cli download https://jiosaavn.com/song/LINK1 https://jiosaavn.com/song/LINK2 ID1 ID2
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
<br>

### Todo -
 - fixing 'htmlspecialchars' bug
 - adding multi-download support

# Footnotes 
I dedicate this project to a special one. Any guess who are they ?

Anyone is free to contribute to this project, fixing bugs, optimising code, improving documentation, testing, feedback, etc.
PLEASE NOTE - `saavn-cli` file is just a duplicate of `main.py`. Please change code of `main.py` file instead.
# License
Copyright &copy; 2022 wiz64

The source code of this tool has been licensed under `MIT License` Read the LICENSE File for more info.

# Copyright Disclaimer
I am not responsible for anything related to Third-Party copyright holders, This script comes with absolutely no warranties and works similar to `youtube-dl`. Kindly use at your own risk. <br>We do not host the Music files on our servers or accounts.
