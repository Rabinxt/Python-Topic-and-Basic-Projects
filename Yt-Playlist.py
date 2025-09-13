from pytube import Playlist

p = Playlist("your link goes here")

for video in p.videos:
    video.streams.first().download()
