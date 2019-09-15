import moviepy.video.fx.all as vfx
from moviepy.editor import *
clip= VideoFileClip("test.mp4")
watermark= VideoFileClip("watermark.gif",has_mask=True).loop().set_duration(clip.duration).resize(height=50).margin(right=8,bottom=8,opacity=0).set_pos(("right","bottom"))
watermark_video =CompositeVideoClip([clip,watermark])
watermark_video.write_videofile('output4.mp4',threads=200)
