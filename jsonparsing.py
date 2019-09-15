from urllib.request import urlopen
import json
import requests
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
def checkimage(link):
    #link = "https://www.reddit.com/r/rareinsults/comments/d271y6/fancy_extrovert_im_a_big_idiot_and_dont_know_how/"
    
    link = link[:len(link)-1]+".json"
    r=requests.get(link,headers={'User-agent' : 'mybotislove'})
    data=r.text
    print("idhar pahicha")
    #jsondata = r.json()
    print(data)
    jsondata = json.loads(data)
    
    imageurl=jsondata[0]['data']['children'][0]['data']['url']
    print('idhar pahucha')

    if(checkextension(imageurl)):
        print(imageurl)
        return imageurl
    else:
        print('second try')
        #for key,value in jsondata[0].items():
          #  print(key)
         #   print(value)
        imageurl=jsondata[0]['data']['children'][0]['data']['media_metadata']
        imageurl = str(imageurl)
        #index= imageurl.index("\n")
        #imageurl=imageurl[:index]
        print(imageurl)
        jsondata= json.loads(imageurl)
        for key,value in jsondata.items():
            jsondata= json.loads(value)
            imageurl = jsondata['s']['u']
            if(checkextension(imageurl)):
                print(imageurl)
                return imageurl
            else:
                return ""
        #return imageurl
        #except:
           # urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+',data)
            #print(urls)
    #except:
     #       print('error')
        imageurl =jsondata[0]['data']['children'][0]['data']['media_metadata']
            #pass
    #except:
     #   print('error')
      #  return ""
#checkimage("https://www.reddit.com/r/europe/comments/d41ukv/what_i_an_american_see_as_the_stereotypical/")
#Todo Pass Only Json
def checkgif(link):
    try:
        link = link[:len(link)-1]+".json"
        r=urlopen(link)
        data=r.read()
        jsondata= json.loads(data)
        gifurl = jsondata[0]['data']['children'][0]['data']['secure_media']['oembed']['thumbnail_url']
        print(gifurl)
        return gifurl
    except:
        print('error')
        return ""
def checkvideo(link):
    try:
        link=link[:len(link)-1]+".json"
        r=requests.get(link,headers={'User-agent' : 'mybotislove'})
        data=r.text
        jsondata=json.loads(data)
        videourl = jsondata[0]['data']['children'][0]['data']['secure_media']['reddit_video']['fallback_url']
        print(videourl)
        return videourl
    except:
        print('error')
        return ""
#checkvideo("https://www.reddit.com/r/toptalent/comments/d2131e/streamer_stumbles_across_a_diamond_in_the_rough/")
checkimage("https://www.reddit.com/r/animepiracy/comments/bzzeaw/anistream_mobile_app_release/")
