import os
print("\n\n --- CURRENT PATH:\n \t\t",os.getcwd())
from moviepy.editor import *
video = VideoFileClip("a.mp4")
video.audio.write_audiofile("ab.mp3")
