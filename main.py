from urllib.request import urlopen
import json
import time
import requests
from PIL import Image
from PIL import ImageOps
import pyimgur
from imgpy import Img
from moviepy.editor import *
import moviepy.video.fx.all as vfx
import cv2
import re
import os
CLIENT_ID = "82f73b28d4f67da"  # imgur
secret = "4a08aed2e3d2886bc98d25357ba49e057dbc0b28"
gyfcatid = "2_ge5Nca"
gyfcatsecret = "V7idgMVa-xTKKrBAFXGJzBANlFv9xXnIxQTQ7eegui-MUTHIlYmtd0WWU6M-eH1X"
refresh_token = ""


def get_token():
    payload = {
        'grant_type': 'password',
        'client_id': gyfcatid,
        'client_secret': gyfcatsecret,
        'username': 'balvinderz',
        'password': 'mani1234'
    }

    url = "https://api.gfycat.com/v1/oauth/token"
    r = requests.post(url, json=payload, headers={
                      'User-Agent': "abc down bot"})

    response = r.json()
    print(response)
    access_token = response["access_token"]
    print(access_token)
    return access_token


def upload(path):
    print("idhar pahucha")
    url = "https://api.gfycat.com/v1/gfycats"
    data = {"noMd5": "true"}
   # access_token = get_token()
    #headers = { 'Authorization': 'Bearer {}'.format(access_token) }

    r = requests.post(url=url, json={"noMd5": "true"})
    # print(r.text)
    print(r.text)
    jsondata = json.loads(r.text)
    print(jsondata['gfyname'])
    uploadurl = "https://filedrop.gfycat.com"
    os.rename(path, jsondata['gfyname'])
    #f={gfyname : open(jsondata['gfyname'],'rb')}
    gfyid = jsondata['gfyname']
    print("gif will be @ https://gfycat.com/{}".format(gfyid))
    file = open(jsondata['gfyname'], 'rb')
    res = requests.put(
        "https://filedrop.gfycat.com/{}".format(jsondata['gfyname']), file)
    # print(res.text)
    linkpath = "https://gfycat.com/"+gfyid
    # os.remove(jsondata['gfyname'])
    return linkpath


def watermarkandcrop(path):
    #cv2video = cv2.VideoCapture(path)
    #height = cv2video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    #width = cv2video.get(cv2.CAP_PROP_FRAME_WIDTH)
    # print(height)
    # print(width)
    #height = int(height)
    #width = int(width)
    # border=30
    try:
        global border
        clip = VideoFileClip(path)
        height = clip.h
        width = clip.w
        new_clip = vfx.crop(clip, x1=border, y1=border,
                            x2=width-border, y2=height-border)
        watermark = VideoFileClip("watermark.gif", has_mask=True).loop().set_duration(
            clip.duration).resize(height=50).margin(right=8, bottom=8, opacity=0).set_pos(("right", "bottom"))
        watermark_video = CompositeVideoClip([new_clip, watermark])
        watermarkpath = "watermarkvideo.mp4"
        print("idhar tak chala")
        watermark_video.write_videofile(watermarkpath, threads=200)
    except:
        watermarkandcrop(path)
   # clip.reader.close()
    # clip.audio.reader.close_proc()

    clip.close()
    del clip
    # new_clip.reader.close()
    # new_clip.audio.reader.close_proc()
    # clip.reader.close()

    # _clip.close()
   # watermark_video.reader.close()
    #  watermark_video.audio.reader.close_proc()

    watermark_video.close()
    del watermark_video
    #del clip
    new_clip.close()
    del new_clip
    #del watermark_video
    return watermarkpath


def addwatermarktogif(path):
    gifclip = VideoFileClip(path)
    logo = (ImageClip("watermark.png")
            .set_duration(gifclip.duration)
            .set_opacity(0.5)
            .set_position(("right", "bottom")))
    print("this got executed")

    final_clip = CompositeVideoClip([gifclip, logo])
    watermarkpath = "watermarkgif.gif"
    final_clip.write_gif(watermarkpath)
    final_clip.close()
    gifclip.close()
    logo.close()
    del final_clip
    del gifclip
    del logo
    return watermarkpath


def cropgif(path):
    global border
    with Img(fp=path) as im:
        # border=30
        im.crop(box=(border, border, im.width-border, im.height-border))
        im.save(fp='crop.gif')
        im.close()
        return "crop.gif"


def uploadtoimgur(path):
    #path = "testpic2.jpg"
    im = pyimgur.Imgur(CLIENT_ID)
    # print(authorization_url)
    #global refresh_token
    # if(refresh_token==""):
    # 3authorization_url = client.get_auth_url('code')
    # print(authorization_url)
    # credentials = client.authorize(, 'pin')

    uploaded_image = im.upload_image(path)
    print(uploaded_image.link)
    return uploaded_image.link


def addwatermark(path, extension):
    photo = Image.open(path)
    watermark = Image.open('watermark.png')
    photo.paste(watermark, (photo.width-175, photo.height-75), watermark)
    # photo.show()
    photo.save('watermarkedimage.'+extension)
    path = "watermarkedimage."+extension
    photo.close()
    return path


def cropImage(img, extension):
    im = Image.open(img)
    #border=int(input("Enter border size :"))
    # border=20
    global border
    width, height = im.size
    print(width)
    print(height)
    im2 = ImageOps.crop(im, 50)
    im2.save("cropimage."+extension)
    path = "cropimage."+extension
    return path
    im.close()
    im2.close()
    # im2.show()


def checkextension(imageurl):

    try:

        if(imageurl.index(".png")):

            return True
    except:
        pass
    try:
        if(imageurl.index(".jpg")):
            return True
    except:
        pass
    try:
        if(imageurl.index(".jpeg")):
            return True
    except:
        pass
    return False


def checkimage(response):
    #link = "https://www.reddit.com/r/rareinsults/comments/d271y6/fancy_extrovert_im_a_big_idiot_and_dont_know_how/"
    try:
        #link = link[:len(link)-1]+".json"
        #r =urlopen(link)
        #jsondata = r.json()
        # data=r.read()
        # print(data)
        jsondata = json.loads(response)
        imageurl = jsondata[0]['data']['children'][0]['data']['url']
        print("url is ", imageurl)
        if(checkextension(imageurl)):
            return imageurl
        else:
            urls = re.findall(r'(https?://\S+)', response)
            newurls = []
            for url in urls:
                if("i.redd.it" in url):
                    newurls.append(url)
            try:
                ind = newurls[0].index("\\n")
                imageurl = newurls[0][:ind]
            except:
                imageurl = newurls[0]
            if(checkextension(imageurl)):
                return imageurl
            else:
                return ""
    except:
        return ""


# checkimage("https://www.reddit.com/r/europe/comments/d41ukv/what_i_an_american_see_as_the_stereotypical/")
# Todo Pass Only Json
def checkgif(response):
    try:
        #link = link[:len(link)-1]+".json"
       # r=urlopen(link)
        # data=r.read()
        jsondata = json.loads(response)
        gifurl = jsondata[0]['data']['children'][0]['data']['secure_media']['oembed']['thumbnail_url']
        print("gifurl is ", gifurl)
        if(gifurl.index(".gif")):
            print("ye execute hua ")
            return gifurl
    except:
        # print('error')
        return ""


def checkvideo(response):
    try:
        # link=link[:len(link)-1]+".json"
        # r=urlopen(link)
        # data=r.read()
        jsondata = json.loads(response)
        videourl = jsondata[0]['data']['children'][0]['data']['secure_media']['reddit_video']['fallback_url']
        print(videourl)
        return videourl
    except:
        # print('error')
        return ""


f = open("links.txt", "r")
outputfile = open("output.txt", "w")
border = int(input("Enter border : "))
for line in f:
    typeoffile = ''
    # link="https://www.reddit.com/r/toptalent/comments/d2131e/streamer_stumbles_across_a_diamond_in_the_rough/"
    # link="https://www.reddit.com/r/europe/comments/d41ukv/what_i_an_american_see_as_the_stereotypical/"
    link = line
    link = link[:len(link)-1]+".json"
    r = requests.get(link, headers={'User-agent': 'mybotislove'})
    data = r.text
    datalink = ""
    datalink = checkimage(data)
    jsonform = json.loads(data)
    subreddit = jsonform[0]['data']['children'][0]['data']['subreddit']
    print("subreddit is ", subreddit)
    title = jsonform[0]['data']['children'][0]['data']['title']
    #title = title.encode('utf-8')
    try:
        print("title is ", title)
    except:
        xyz = title.encode('utf-8')
        title = xyz
        print("title is ", title)
    print(datalink)
    if(datalink != ""):
        print("ye execute hua ")
        # reverse=datalink.reverse()
        ind = datalink.rfind(".")
        extension = datalink[ind+1:]

        f = open('image.'+extension, 'wb')
        f.write(requests.get(datalink).content)
        f.close()
        path = 'image.'+extension
        croppath = cropImage(path, extension)
        # os.remove(path)
        watermarkpath = addwatermark(croppath, extension)
        # os.remove(croppath)
        imgurlink = uploadtoimgur(watermarkpath)
        # os.remove(watermarkpath)
        try:
            writetext = str(title)+";"+imgurlink+";r/"+subreddit+"\n"
            outputfile.write(writetext)

        except:
            writetext = str(title.encode('utf-8'))+";" + \
                imgurlink+";r/"+subreddit+"\n"
            outputfile.write(writetext)
        continue
    datalink = ""
    datalink = checkgif(data)
    if(datalink != ""):

        print("it is a gif")
        f = open('image.gif', 'wb')
        f.write(requests.get(datalink).content)
        f.close()
        path = 'image.gif'
        croppath = cropgif(path)
        # os.remove(path)
        watermarkgifpath = addwatermarktogif(croppath)
        # os.remove(croppath)
        link = upload(watermarkgifpath)
        # os.remove(watermarkgifpath)
        print(link)
        try:
            writetext = str(title)+";"+link+";r/"+subreddit+"\n"
            outputfile.write(writetext)

        except:
            writetext = str(title.encode('utf-8')) + \
                ";"+link+";r/"+subreddit+"\n"
            outputfile.write(writetext)
        continue
    datalink = ""
    datalink = checkvideo(data)
    if(datalink != ""):

        print("it is a video")
        f = open("video.mp4", 'wb')
        f.write(requests.get(datalink).content)
        f.close()
        path = "video.mp4"
        watermarkpath = watermarkandcrop(path)
        # os.remove(path)
        link = upload(watermarkpath)
        # os.remove(watermarkpath)
        try:
            writetext = str(title)+";"+link+";r/"+subreddit+"\n"
            outputfile.write(writetext)

        except:
            writetext = str(title.encode('utf-8')) + \
                ";"+link+";r/"+subreddit+"\n"
            outputfile.write(writetext)

    # time.sleep(5)
outputfile.close()
