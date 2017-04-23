from gmusicapi import Musicmanager


def uploadSong(song):
    songPath = song + ".m4a"
    api = Musicmanager()
    
    api.login()
    x = api.upload(songPath)  

def main():
    uploadSong("Never Gonna Give You Up")
    
if __name__ == "__main__": main()