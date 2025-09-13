from pytube import Playlist

p = Playlist("https://www.youtube.com/watch?v=Sc1OI1i-Kgs&list=RDSc1OI1i-Kgs&start_radio=1")

for video in p.videos:
    video.streams.first().download()
