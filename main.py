#!/usr/bin/env python
import os
import requests
import sys


# CONFIGURATION
# API_URL - Saavn Unofficial API (@sumitkolhe)
API_URL = "https://saavn.me"
# Search_EP - Endpoint for searching the API
Search_EP = "/search/songs?query="

Bitrate = 320 # Default Bitrate

allowed_Bitrate = [12,48,96,160,320]
# Bitrate Squence is important

version = "0.0.1" # Client Version
NULL = " >/dev/null 2>&1 " # Nullifier to hide messy ffmpeg output
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
     Searching Songs from the terminal
     Example -
    `saavn-cli s Darshan Raval`

# d / download <link1> <link2> ...
   NOT AVAIABLE IN THIS VERSION
     Downloading Saavn Songs from links or IDs
     Example -
    `saavn-cli d IEBQ7- DFEHNB- SJADKEi`

To force bitrate, specify it after action like <action:160>
`saavn-cli s:160 New songs`

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

print("System Platform : "+sys.platform)
if sys.platform == "win32":
        NULL = " >nul 2>&1"
if debug=="true":
        NULL = ""


def DoUpdate(version):
    #URL of Update service
    URL = ("https://raw.githubusercontent.com/wiz64/saavn-cli/main/latest-version")
    print(" GET "+URL)
    r = requests.get(URL)
    if(r.status_code == 200):
      print("OK 200")
      Fetched = r.json()
      print(Fetched)
      ServerVersion = Fetched['version']
      if(ServerVersion>version):
        print("\n\n [OK] An Update is available, Download Here : "+Fetched['download'])
        exit()
      elif(ServerVersion<=version):
        print("\n\n Tool is currently at latest version. check back later")
    else:
      print(r.status_code)
      print("ERROR : Unable to reach Update API. Check Github")
      exit()


######## SEARCH FUNCTION
def FetchSearch(search_term):
    URL = ( API_URL + Search_EP + search_term + "&limit=40")
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
      if(FetchedItems["results"][20:]):
        is_next_page = 1
        NextPage_text = "| `n` for next page |"
      print(f" {NextPage_text} Enter Song No. To Download | 0 or Enter to Cancel")
      #
      # # ASK FOR USER INPUT
      #
      song_index = input()
      if (is_next_page==1 and str(song_index).lower() == 'n'):
            i=20 #number counter
            for item in FetchedItems["results"][20:]:
              i=i+1
              song_id = str(item['id'])
              song_album = str(item['album']['name'])[:32]
              song_name = str(item['name'])[:32]
              if song_name == song_album:song_album=" "
              else: song_album = " @ "+song_album
              song_artist = str(item['artist'])[:32]
              print(f"({i}) ID: {song_id} | {song_name}{song_album} by {song_artist}")
            print(f" Enter Song No. To Download | 0 or Enter to Cancel")
            song_index = input()

      
            
      if (int(song_index) == 0 or song_index==""):
        print("User Cancelled Download. Exiting")
        exit(0)
      i = int(song_index)
      item = FetchedItems['results'][i-1]
      song_id = str(item['id'])
      song_album = str(item['album']['name'])
      song_name = str(item['name'])
      song_year = str(item['year'])
      song_artist = str(item['artist'])
      song_img_url = str(item['image'][2]['link'])
      song_copyright = str(item['copyright'])
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
      print(NULL)
      compile_command = f'cd "{work_dir}" && ls && ffmpeg -i "{song_id}_raw.mp3" -i "{song_id}_raw.jpg" -map 0:0 -map 1:0 -c copy -id3v2_version 3 -metadata title="{song_name}" -metadata album="{song_album}" -metadata artist="{song_artist[:72]}" -metadata date="{song_year}" -metadata album_artist="{song_artist[:72]}" -metadata copyright="{song_copyright}" -metadata publisher="{song_publisher}" -metadata comment="{song_comment}" -codec:a libmp3lame -b:a {Bitrate}k -hide_banner -y "{output}"{NULL} && rm "{song_id}_raw.mp3" "{song_id}_raw.jpg"'

      print("========= STARTING COMPILATION ============")
      download_data =f"""
       SONG ID : {song_id}
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
      exit()



print(init_text)

# ARGUMENTS PARSING
if (len(sys.argv) > 1):
  options = sys.argv[1].split(":",1)
  if (options[0] == "s" or options[0] =="search"):
    action="search"
    print("Action : search")
  elif (options[0] == "d" or options[0] =="download"):
    action="download"
    print("Action : download | This action is currently under development. Check for Updates")
    exit()
  elif(options[0]=="h" or options[0] =="help"):
    print(help_text)
    exit()
  elif(options[0]=="update"):
    print("Checking for Updates")
    action="update"
  else:
    print("Unknown action : Check `saavn-cli help`")
    exit()
  if(len(options)>1):
    if int(options[1]) in allowed_Bitrate:
        Bitrate = int(options[1])
        Bitrate_index = allowed_Bitrate.index(Bitrate)
  print("Bitrate Selected : "+ str(Bitrate))
## END CLI OPTIONS PARSING
#####################
# START TERMS PARSING
if (len(sys.argv) >= 3):
  terms = sys.argv[2:]
  if(action=="search"):
    searchTerm = " ".join(terms)
    print("Search Terms : "+ searchTerm)
  if(action=="download"):
    terms = sys.argv[2:]
    DownloadItems = " ".join(terms).split(" ")
    for item in DownloadItems:
      print(item)
####### END TERMS PARSING


if(action=="search"):
  try:
   FetchSearch(searchTerm)
  except:
    print("\n ERROR : Action Failed")
    exit()
if(action=="update"):
  DoUpdate(version)
