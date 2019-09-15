from moviepy.editor import *
gifclip = VideoFileClip("giftest.gif")
logo = (ImageClip("watermark.png")
    .set_duration(gifclip.duration)
    .set_opacity(0.5)
    .set_position( ("right", "bottom") ))
final_clip = CompositeVideoClip([gifclip, logo])
final_clip.write_gif("newgif.gif")
