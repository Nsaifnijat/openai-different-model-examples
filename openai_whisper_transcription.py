
#installation, pip install openai-whisper
#colab address, https://colab.research.google.com/drive/1vJj6EW0nKi3olLb5nOccA4ypkKx-x4Hr#scrollTo=dsDvCjk1KNi0
import whisper
from pytube import YouTube

#the model we use for our case is base, there is -- tiny - base -small- medium - large
model = whisper.load_model('base')


youtube_video_url = "https://www.youtube.com/watch?v=c_LAIkkhKts&ab_channel=PartTimeLarry" #"https://www.youtube.com/watch?v=NT2H9iyd-ms"
youtube_video = YouTube(youtube_video_url)

video_title = youtube_video.title
print(video_title)

video_formats = youtube_video.streams
#we only need audio formats
audios = video_formats.filter(only_audio=True)
first_audio = audios.first()


#now lets download 
first_audio.download(filename='partimelarry.mp4')


import datetime

# save a timestamp before transcription
t1 = datetime.datetime.now()
print(f"started at {t1}")

# do the transcription
output = model.transcribe("partimelarry.mp4")

# show time elapsed after transcription is complete.
t2 = datetime.datetime.now()
print(f"ended at {t2}")
print(f"time elapsed: {t2 - t1}")


