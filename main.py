from urllib.request import urlopen
import json
import time
import requests
from  PIL import Image
from PIL import ImageOps
import pyimgur
from imgpy import Img
from moviepy.editor import *
import moviepy.video.fx.all as vfx
import cv2
import os
CLIENT_ID = "82f73b28d4f67da"
def upload(path):
    url="https://api.gfycat.com/v1/gfycats"
    data={"noMd5" : "true"}
    r=requests.post(url=url,json={"noMd5" : "true"})
    #print(r.text)

    jsondata =json.loads(r.text)
    print(jsondata['gfyname'])
    uploadurl ="https://filedrop.gfycat.com"
    os.rename(path,jsondata['gfyname'])
    #f={gfyname : open(jsondata['gfyname'],'rb')}
    gfyid= jsondata['gfyname']
    print("gif will be @ https://gfycat.com/{}".format(gfyid))
    file= open(jsondata['gfyname'],'rb')
    res=requests.put("https://filedrop.gfycat.com/{}".format(jsondata['gfyname']), file)
    print(res.text)
    linkpath ="https://gfycat.com/"+gfyid
    return linkpath
def watermarkandcrop(path):
    cv2video = cv2.VideoCapture(path)
    height = cv2video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width  = cv2video.get(cv2.CAP_PROP_FRAME_WIDTH)
    print(height)
    print(width)
    height=int(height)
    width=int(width)
    border=30
    clip= VideoFileClip(path)
    new_clip= vfx.crop(clip,x1=border,y1=border,x2=width-border,y2=height-border)
    watermark= VideoFileClip("watermark.gif",has_mask=True).loop().set_duration(clip.duration).resize(height=50).margin(right=8,bottom=8,opacity=0).set_pos(("right","bottom"))
    watermark_video =CompositeVideoClip([new_clip,watermark])
    watermarkpath="watermarkvideo.mp4"
    print("idhar tak chala")
    watermark_video.write_videofile(watermarkpath,threads=200)
    return watermarkpath
def addwatermarktogif(path):
    gifclip = VideoFileClip(path)
    logo = (ImageClip("watermark.png")
        .set_duration(gifclip.duration)
        .set_opacity(0.5)
        .set_position( ("right", "bottom") ))
    print("this got executed")

    final_clip = CompositeVideoClip([gifclip, logo])
    watermarkpath = "watermarkgif.gif"
    final_clip.write_gif(watermarkpath)

    return watermarkpath
def cropgif(path):
    with Img(fp=path) as im:
        border=30
        im.crop(box=(border, border, im.width-border, im.height-border))
        im.save(fp='crop.gif')
        return "crop.gif"
def uploadtoimgur(path):
    #path = "testpic2.jpg"
    im=pyimgur.Imgur(CLIENT_ID)
    uploaded_image=im.upload_image(path)
    print(uploaded_image.link)
    return uploaded_image.link

def addwatermark(path,extension):
    photo = Image.open(path)
    watermark = Image.open('watermark.png')
    photo.paste(watermark,(photo.width-150,photo.height-75),watermark)
    #photo.show()
    photo.save('watermarkedimage.'+extension)
    path = "watermarkedimage."+extension
    return path
def cropImage(img,extension):
    im= Image.open(img)
    #border=int(input("Enter border size :"))
    border=20
    width,height = im.size
    print(width)
    print(height)
    im2= ImageOps.crop(im,50)
    im2.save("cropimage."+extension)
    path = "cropimage."+extension
    return path
    #im2.show()
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
        #data=r.read()
        #print(data)
        jsondata = json.loads(response)
        imageurl=jsondata[0]['data']['children'][0]['data']['url']
        print("url is ",imageurl)
        if(checkextension(imageurl)):
            return imageurl
        else:
            secondtry 
    except:
        return ""
    
        

#checkimage("https://www.reddit.com/r/europe/comments/d41ukv/what_i_an_american_see_as_the_stereotypical/")
#Todo Pass Only Json
def checkgif(response):
    try:
        #link = link[:len(link)-1]+".json"
       # r=urlopen(link)
        #data=r.read()
        jsondata= json.loads(response)
        gifurl = jsondata[0]['data']['children'][0]['data']['secure_media']['oembed']['thumbnail_url']
        print("gifurl is ",gifurl)
        if(gifurl.index(".gif")):       
            return gifurl
    except:
        #print('error')
        return ""
def checkvideo(response):
    try:
        #link=link[:len(link)-1]+".json"
        #r=urlopen(link)
        #data=r.read()
        jsondata=json.loads(response)
        videourl = jsondata[0]['data']['children'][0]['data']['secure_media']['reddit_video']['fallback_url']
        print(videourl)
        return videourl
    except:
        #print('error')
        return ""
f=open("links.txt","r")
outputfile=open("output.txt","w")
for line in f:
    typeoffile=''
    #link="https://www.reddit.com/r/toptalent/comments/d2131e/streamer_stumbles_across_a_diamond_in_the_rough/"
    #link="https://www.reddit.com/r/europe/comments/d41ukv/what_i_an_american_see_as_the_stereotypical/"
    link=line
    link=link[:len(link)-1]+".json"
    r=requests.get(link,headers={'User-agent' : 'mybotislove'})
    data=r.text
    datalink=""
    datalink=checkimage(data)
    jsonform =  json.loads(data)
    subreddit = jsonform[0]['data']['children'][0]['data']['subreddit']
    print("subreddit is ",subreddit)
    title = jsonform[0]['data']['children'][0]['data']['title']
    print("title is ",title)
    print(datalink)
    if(datalink!=""):
       print("ye execute hua ")
       #reverse=datalink.reverse()
       ind= datalink.rfind(".")
       extension = datalink[ind+1:]
       
       f = open('image.'+extension,'wb')
       f.write(requests.get(datalink).content)
       f.close()
       path='image.'+extension
       croppath = cropImage(path,extension)
       watermarkpath =addwatermark(croppath,extension)
       imgurlink=uploadtoimgur(watermarkpath)
       writetext=title+";"+imgurlink+";"+subreddit+"\n"
       outputfile.write(writetext)
       continue
    datalink=""
    datalink= checkgif(data)
    if(datalink!=""):
        continue
        print("it is a gif")
        f=open('image.gif','wb')
        f.write(requests.get(datalink).content)
        f.close()
        path='image.gif'
        croppath =cropgif(path)
        watermarkgifpath=addwatermarktogif(croppath)
        link=upload(watermarkgifpath)
        print(link)
        writetext=title+";"+link+";"+subreddit+"\n"
        outputfile.write(writetext)
        continue
    datalink=""
    datalink= checkvideo(data)
    if(datalink!=""):
        continue
        print("it is a video")
        f=open("video.mp4",'wb')
        f.write(requests.get(datalink).content)
        f.close()
        path="video.mp4"
        watermarkpath = watermarkandcrop(path)
        link=upload(watermarkpath)
        writetext=title+";"+link+";"+subreddit+"\n"
        outputfile.write(writetext)
        
    time.sleep(5)
outputfile.close()
