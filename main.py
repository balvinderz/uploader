from urllib.request import urlopen
import json


def checkimage(response):
    #link = "https://www.reddit.com/r/rareinsults/comments/d271y6/fancy_extrovert_im_a_big_idiot_and_dont_know_how/"
    #try:
        #link = link[:len(link)-1]+".json"
        #r =urlopen(link)
        #jsondata = r.json()
        #data=r.read()
        #print(data)
    jsondata = json.loads(response)
    imageurl=jsondata[0]['data']['children'][0]['data']['url']
    print("url is ",imageurl)
    return imageurl
    #except:
        #return ""
#checkimage("https://www.reddit.com/r/europe/comments/d41ukv/what_i_an_american_see_as_the_stereotypical/")
#Todo Pass Only Json
def checkgif(response):
    try:
        #link = link[:len(link)-1]+".json"
       # r=urlopen(link)
        #data=r.read()
        jsondata= json.loads(response)
        gifurl = jsondata[0]['data']['children'][0]['data']['secure_media']['oembed']['thumbnail_url']
        print(gifurl)
        return gifurl
    except:
        print('error')
        return ""
def checkvideo(response):
    try:
        #link=link[:len(link)-1]+".json"
        #r=urlopen(link)
        #data=r.read()
        jsondata=json.loads(response)
        videourl = jsondata[0]['data']['children'][0]['data']['secure_media']['reddit_video']['hls_url']
        print(videourl)
        return videourl
    except:
        print('error')
        return ""

typeoffile=''
link="https://www.reddit.com/r/toptalent/comments/d2131e/streamer_stumbles_across_a_diamond_in_the_rough/"
#link="https://www.reddit.com/r/europe/comments/d41ukv/what_i_an_american_see_as_the_stereotypical/"
link=link[:len(link)-1]+".json"
r=urlopen(link)
data=r.read()
datalink=""
datalink=checkvideo(data)
if(datalink!=""):
    typeoffile="video"
if(typeoffile==""):
   datalink=checkgif(data)
if(datalink!=""):
    typeoffile="gif"
if(typeoffile==""):
   datalink=checkimage(data)
if(datalink!=""):
    typeoffile="image"
if(typeoffile==""):
    print("error")
