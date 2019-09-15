from gfycat.client import GfycatClient
import requests
import os
import json
#client = GfycatClient(CLIENT_ID,secret)
#info =client.upload_from_file('tenor.gif')
#print(info)
url="https://api.gfycat.com/v1/gfycats"
data={"noMd5" : "true"}
r=requests.post(url=url,json={"noMd5" : "true"})
#print(r.text)

jsondata =json.loads(r.text)
print(jsondata['gfyname'])
uploadurl ="https://filedrop.gfycat.com"
os.rename("tenor.gif",jsondata['gfyname'])
#f={gfyname : open(jsondata['gfyname'],'rb')}
file= open(jsondata['gfyname'],'rb')
res=requests.put("https://filedrop.gfycat.com/{}".format(jsondata['gfyname']), file)
print(res.text)

