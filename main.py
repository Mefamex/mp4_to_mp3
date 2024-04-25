import os
from moviepy.editor import *
video = VideoFileClip("aaa.mp4")
video.audio.write_audiofile("ab.mp3")
