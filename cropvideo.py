import cv2
import moviepy.video.fx.all as vfx
from moviepy.editor import *
def watermarkandcrop(path):
    cv2video = cv2.VideoCapture(path)
    height = cv2video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width  = cv2video.get(cv2.CAP_PROP_FRAME_WIDTH)
    print(height)
    print(width)
    height=int(height)
    width=int(width)
    border=30
    clip= VideoFileClip("test.mp4")
    new_clip= vfx.crop(clip,x1=border,y1=border,x2=width-border,y2=height-border)
    watermark= VideoFileClip("watermark.gif",has_mask=True).loop().set_duration(clip.duration).resize(height=50).margin(right=8,bottom=8,opacity=0).set_pos(("right","bottom"))
    watermark_video =CompositeVideoClip([new_clip,watermark])
    watermark_video.write_videofile('watermarkvideo.mp4',threads=200)

#new_clip.write_videofile("cropped.mp4",audio=True,threads=100,codec = 'libx264')
