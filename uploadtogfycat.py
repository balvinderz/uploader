from gfycat.client import GfycatClient

CLIENT_ID="2_ge5Nca"
secret="V7idgMVa-xTKKrBAFXGJzBANlFv9xXnIxQTQ7eegui-MUTHIlYmtd0WWU6M-eH1X"

client = GfycatClient(CLIENT_ID,secret)
info =client.upload_from_file('tenor.gif')
print(info)
