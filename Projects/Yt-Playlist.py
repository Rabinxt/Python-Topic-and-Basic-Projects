from pytube import Playlist

p = Playlist("your link")

for video in p.videos:
    video.streams.first().download()
