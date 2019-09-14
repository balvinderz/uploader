import os
import subprocess
command="ffmpeg -i \"https://v.redd.it/5a4bzndycol31/HLSPlaylist.m3u8\"-codec copy file.mp4"
print(command)
process =subprocess.Popen(command,shell=True)
#process=subprocess.run(["ffmpeg","-i",command,"-codec","copy","file.mp4"],shell=True)
process.wait()
print('soja')
