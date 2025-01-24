from pytubefix import YouTube
from pytubefix.cli import on_progress
 
url = "https://www.youtube.com/watch?v=s5yoH4yhtyo"
 
yt = YouTube(url, on_progress_callback=on_progress, client="web")
ys = yt.streams.get_highest_resolution()
ys.download()

##не работает, нужно будет переписать