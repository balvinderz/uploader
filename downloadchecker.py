import requests
f = open('00000001.mp4','wb')
f.write(requests.get('https://v.redd.it/5a4bzndycol31/DASH_480?source=fallback').content)
f.close()
