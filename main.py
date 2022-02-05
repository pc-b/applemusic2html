import requests
from bs4 import BeautifulSoup
from youtubesearchpython import VideosSearch


#get page and parse (set your own playlist url)
URL = "_your_apple_music_playlist_url_here"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

#get songs and artists
songs = soup.find_all("div", class_="songs-list-row__song-container")
artists = soup.find_all("div", class_="songs-list__col songs-list__col--artist typography-body")


#open file
f = open("songs.txt", "w")

#print every song in results
num = 0
while num < len(songs):
    title = songs[num].find("div", class_="songs-list-row__song-name")
    artist = artists[num].text.strip()
    #set printed to {title} + {artist} 
    printed = title.text.strip() + " - " + artist
   
    video = VideosSearch(printed, limit=1)
    result = video.result()
    
    #get link of video
    link = result["result"][0]["link"]

    #format string for html output (my formatting change as you like)
    printed = '<a href="' + link + '"style="text-decoration: none;">>' + title.text.lower() + "</a><br>"

    #write to file
    f.write(printed)
    f.write("\n")
    num += 1
#close file
f.close()