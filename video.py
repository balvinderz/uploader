import ffmpy
ff=ffmpy.FFmpeg(
    inputs ={'https://v.redd.it/5a4bzndycol31/HLSPlaylist.m3u8' : None},
    outputs ={'./out.mp4' :None})
ff.run()
