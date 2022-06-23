#!/usr/bin/env python
import os
import html
import requests
from sys import exit
import sys
import subprocess
from time import sleep
# CONFIGURATION
# API_URL - Saavn Unofficial API (@sumitkolhe)
API_URL = "https://saavn.me"
# Search_EP - Endpoint for searching the API
Search_EP = "/search/songs?query="

Bitrate = 320 # Default Bitrate

allowed_Bitrate = [12,48,96,160,320]
# Bitrate Squence is important

version = "0.0.1" # Client Version
versionCode = 1
Nullifier = " >/dev/null 2>&1 " # Nullifier to hide messy ffmpeg output
debug="false" # Show additional output or not
Bitrate_index = 4 #Default Bitrate Index of allowed_Bitrate
# Initialization Text
init_text = """
 ___________________________________________
 | Saavn-cli Command-Line Music Downloader |
 | ==========    By Wiz64     ============ |
 |  https://github.com/wiz64/saavn-cli     |
 |                                         |
 |     For Help, run `saavn-cli help`      |
 -------------------------------------------
"""
#Help Text
help_text = """
saavn-cli <action> <terms/links>

Supported Actions :
# s / search <terms>
     Searching Tracks from the terminal
     Example -
    `saavn-cli s english 2022`

# d / download <link1> <link2> ...
   NOT AVAIABLE IN THIS VERSION
     Downloading Saavn Songs from links or IDs
     Example -
    `saavn-cli d IEBQ7- DFEHNB- SJADKEi`

To force bitrate, specify it after action like <action:160>
`saavn-cli s:160 english songs`

# h / help 
     Shows this message

# update
     Checks for updates

---- END ----
"""

SearchTerm = ""
DownloadItems = []
action = ""
FetchedItems = []
work_dir = "/tmp/saavn-cli/"

FFMPEG_ERROR = "use your package manager - eg- sudo apt install ffmpeg"
print("System Platform : "+sys.platform)
if sys.platform == "win32":
        Nullifier = " >nul 2>&1"
        FFMPEG_ERROR = r"Download ffmpeg.exe and copy to C:\Windows\System32"
if debug=="true":
        Nullifier = ""

# Calling ffmpeg command to test if it is installed and working
try:
    subprocess.run(['ffmpeg','-version'],check = True,
    stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
except:
    print("\033[31;1;4m ERROR : ffmpeg command not found. Install ffmpeg..")
    print("\033[1;32m "+FFMPEG_ERROR+" \033[0m")

def DoUpdate(version):
    #URL of Update service
    URL = ("https://raw.githubusercontent.com/wiz64/saavn-cli/main/latest-version")
    print(" GET "+URL)
    r = requests.get(URL)
    if r.status_code == 200:
      print("OK 200")
      Fetched = r.json()
      print(Fetched)
      ServerVersion = Fetched['version']
      ServerVersionCode = Fetched['versionCode']
      if(ServerVersionCode>versionCode):
        print("\n\n [OK] An Update is available, Download Here : "+Fetched['download'])
        exit()
      elif(ServerVersion<=versionCode):
        print("\n\n Tool is currently at latest version. check back later")
    else:
      print(r.status_code)
      print("ERROR : Unable to reach Update API. Check Github")
      exit()

######## SEARCH FUNCTION
def FetchSearch(search_term):
    URL = ( API_URL + Search_EP + str(search_term) + "&limit=60")
    print(" GET "+URL)
    r = requests.get(URL)
    if(r.status_code == 200):
      print("OK 200")
      FetchedItems = r.json()
      
      i=0 #number counter
      for item in FetchedItems["results"][:20]:
        i=i+1
        song_id = str(item['id'])
        song_album = str(item['album']['name'])[:32]
        song_name = str(item['name'])[:32]
        if song_name == song_album:song_album=" "
        else: song_album = " @ "+song_album
        song_artist = str(item['artist'])[:32]
        print(f"({i}) ID: {song_id} | {song_name}{song_album} by {song_artist}")

      is_next_page=0
      NextPage_text =""
      if(FetchedItems["results"][20:]):
        is_next_page = 1
        NextPage_text = " `n` for next page |"
      print(f" {NextPage_text} Enter Comma Sperated Numbers eg-(6,11,23) To Download | 0 or Enter to Cancel")
      #
      # # ASK FOR USER INPUT
      #
      song_indexes = input("Track No.s - ")
      if (is_next_page==1 and str(song_indexes).lower() == 'n'):
            i=20 #number counter
            for item in FetchedItems["results"][20:]:
              i=i+1
              song_id = str(item['id'])
              song_album = html.unescape(str(item['album']['name'])[:32])
              song_name = html.unescape(str(item['name'])[:32])
              if song_name == song_album:song_album=" "
              else: song_album = " @ "+song_album
              song_artist = html.unescape(str(item['artist'])[:32])
              print(f"({i}) ID: {song_id} | {song_name}{song_album} by {song_artist}")
            print(f"Enter Comma Sperated Numbers eg-(6,11,23) To Download | 0 or Enter to Cancel")
            song_indexes = input("Track No.s - ")

      
            
      if (song_indexes=="" or song_indexes == 0 or song_indexes=="0"):
        print("User Cancelled Download. Exiting")
        exit(0)
      song_indexes = song_indexes.split(",")
      print("Selected Download(s):")
      for song_index in song_indexes:
        i = int(song_index)
        item = FetchedItems['results'][i-1]
        song_id = str(item['id'])
        song_album = str(item['album']['name'])
        song_name = str(item['name'])
        print(f"{i}th -> {song_name} - {song_album}")

      sleep(3)
      for song_index in song_indexes:
        i = int(song_index)
        item = FetchedItems['results'][i-1]
        song_id = str(item['id'])
        song_album = html.unescape(str(item['album']['name']))
        song_name = html.unescape(str(item['name']))
        song_year = html.unescape(str(item['year']))
        song_artist = html.unescape(str(item['artist']))
        song_img_url = str(item['image'][2]['link'])
        song_copyright = html.unescape(str(item['copyright']))
        song_publisher = "Saavn-cli" #str(item['publisher'])
        song_comment = "https://github.com/wiz64/saavn-cli"
        song_download_url = str(item['downloadUrl'][Bitrate_index]['link'])
      
      
        print(f"Downloading ({i}) {song_name[:36] } @ { song_album[:36]} by {song_artist[:36]} with song_id {song_id} at {Bitrate}kbps at {work_dir}")
        if not os.path.isdir(work_dir):
            os.makedirs(work_dir)

        song_data = requests.get(song_download_url)
        open(f'{work_dir}{song_id}_raw.mp3', 'wb').write(song_data.content)
        song_data = requests.get(song_img_url)
        open(f'{work_dir}{song_id}_raw.jpg', 'wb').write(song_data.content)
        output = os.getcwd()+f"/{song_name}-{song_year}.mp3"
        print("Compiling Metadata")
        compile_command = f'cd "{work_dir}" && ls && ffmpeg -i "{song_id}_raw.mp3" -i "{song_id}_raw.jpg" -map 0:0 -map 1:0 -c copy -id3v2_version 3 -metadata title="{song_name}" -metadata album="{song_album}" -metadata artist="{song_artist[:72]}" -metadata date="{song_year}" -metadata album_artist="{song_artist[:72]}" -metadata copyright="{song_copyright}" -metadata publisher="{song_publisher}" -metadata comment="{song_comment}" -codec:a libmp3lame -b:a {Bitrate}k -hide_banner -y "{output}"{Nullifier} && rm "{song_id}_raw.mp3" "{song_id}_raw.jpg"'

        print("========= STARTING COMPILATION ============")
        download_data =f"""
       TRACK ID : {song_id}
       NAME : {song_name[:32]}
       ARTIST : {song_artist[:42]}
       ALBUM : {song_album[:32]}
       PUBLISHING : {song_copyright}
       YEAR : {song_year}
       BITRATE : {Bitrate}kbps
       Output : `{output}`
      """
        print(download_data)
        print("Executing FFMPEG... \n Compiling")
        try:
            os.system(compile_command)
        except:
            print(" ERROR EXECUTING COMMANDS")
        print('========  COMPILATION FINISHED  ========')
    else:
      print("ERROR : UNABLE TO FETCH FROM API")

def ParseAction(argv):
    action="help"
    options = argv[1].split(":",1)
    if (options[0] == "s" or options[0] =="search"):
      action="search"
      print("Action : search")
    elif (options[0] =="exit"):
      action="exit"
      print("Action : exit")
      print("     Exiting....")
      exit()

    elif (options[0] == "d" or options[0] =="download"):
      action="download"
      print("Action : download | This action is currently under development. Check for Updates")
    elif(options[0]=="h" or options[0] =="help"):
      print(help_text)
    elif(options[0]=="update"):
      print("Checking for Updates")
      action="update"
    else:
      print("Unknown action : Check `saavn-cli help`")
    
    if(len(options)>1):
        if int(options[1]) in allowed_Bitrate:
          Bitrate = int(options[1])
          Bitrate_index = allowed_Bitrate.index(Bitrate)
          print("Bitrate Selected : "+ str(Bitrate))
          
    return action
## END CLI OPTIONS PARSING
#####################
# START TERMS PARSING
def ParseTerms(action,argv):
  terms = argv[2:]
  if(action=="search"):
    searchTerm = " ".join(terms)
    print("Search Terms : "+ searchTerm)
    return searchTerm
  if(action=="download"):
    terms = sys.argv[2:]
    DownloadItems = " ".join(terms).split(" ")
    for item in DownloadItems:
      print(item)
    return DownloadItems
####### END TERMS PARSING
####### DIRECT MODE FUNTCION
def DirectMode():
  while(1):
    Command = input(" Command : ")
    Command = Command.split(" ")
    if not Command[0] == "saavn-cli":
      Command.insert(0,"saavn-cli")
    if len(Command) > 1:
      action = ParseAction(Command)
    if len(Command) > 2:
      searchTerms = ParseTerms(action,Command)
    DoAction(action,searchTerms)

## 
def DoAction(action,Terms):
  if(action=="search"):
    try:
      FetchSearch(Terms)
    except:
      print("\n ERROR : Action Failed")
      exit()
  if(action=="update"):
    DoUpdate(version)


print(init_text)

# ARGUMENTS PARSING
if(len(sys.argv) == 1):
      print("Running directly. Enter Command. eg- saavn-cli search new english songs")
      DirectMode()
      
if (len(sys.argv) > 1):
      action = ParseAction(sys.argv)
if (len(sys.argv) > 2):
      SearchTerm = ParseTerms(action,sys.argv)

DoAction(action,SearchTerm)
