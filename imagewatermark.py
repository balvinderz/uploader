from  PIL import Image
def addwatermark(path,extension)
    photo = Image.open(path)
    watermark = Image.open('watermark.png')

    photo.paste(watermark,(photo.width-150,photo.height-75),watermark)
    #photo.show()
    photo.save('watermarkedimage.'+extension)
