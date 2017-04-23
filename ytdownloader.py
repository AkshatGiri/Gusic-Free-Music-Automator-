#YTD - Youtube Downloader
#I used Paffy instead of Youtube-dl because it is easier to download a .m4a audio file(.m4a is compatible with google Music) with paffy. Especially on PythonAnywhere server. 
#If you think you can get youtube-dl to download .mp3 file from youtube please make a pull request. 

import pafy
import urllib.request
import os
from bs4 import BeautifulSoup

query = "say you won't let go" #Search content for the url
title = ''

def DownloadSong(songName):
    query = songName.replace(" ", "+")
    #Searching on youtube and gettiing the video url
    search = urllib.request.urlopen('http://youtube.com/results?search_query='+query)
    html = search.read()
    
    #reading the html document
    soup = BeautifulSoup(html, 'html.parser')
    #Takes the first video link
    link = soup.find('a', "yt-uix-tile-link")
    global title
    title = link.get('title')
    #Creating the download link
    downloadLink = "https://www.youtube.com" + link.get('href')
        
    #Downloading the song
    video = pafy.new(downloadLink)
    audiostreams = video.audiostreams
    
    for a in audiostreams:
        print(a.bitrate, a.extension, a.get_filesize())
        if a.extension == "m4a":
            a.download()
            break
           
#This function will delete the song as long as the song is in the same direcotry.
def deleteSong():
    os.remove(title + ".m4a")
    print("Delelted")
            
def main():
    song = input('Enter the song and the artist:')
    DownloadSong(song)  
    #deleteSong()
    
if __name__ == "__main__": main()