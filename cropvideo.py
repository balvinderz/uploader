import cv2
import moviepy.video.fx.all as vfx
from moviepy.editor import *

cv2video = cv2.VideoCapture("test.mp4")
height = cv2video.get(cv2.CAP_PROP_FRAME_HEIGHT)
width  = cv2video.get(cv2.CAP_PROP_FRAME_WIDTH)
print(height)
print(width)
height=int(height)
width=int(width)
border=30
clip= VideoFileClip("test.mp4")
new_clip= vfx.crop(clip,x1=border,y1=border,x2=width-border,y2=height-border)
new_clip.write_videofile("cropped.mp4",audio=True,threads=100)
