from moviepy.editor import *
def addwatermarktogif(path)
    gifclip = VideoFileClip(path)
    logo = (ImageClip("watermark.png")
        .set_duration(gifclip.duration)
        .set_opacity(0.5)
        .set_position( ("right", "bottom") ))
    final_clip = CompositeVideoClip([gifclip, logo])
    watermarkpath = "watermark.gif")
        final_clip.write_gif(watermarkpath)

    return watermarkpath
