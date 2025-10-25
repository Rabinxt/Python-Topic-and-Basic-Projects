from pytube import Playlist

p = Playlist("your link")

for video in p.videos:
    video.streams.first().download()
    
    
#Or use command prompt 
#   pip install yt-dlp

# yt-dlp -x --audio-format mp3 <playlist_URL>
