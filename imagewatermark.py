from  PIL import Image
photo = Image.open('testpic2.jpg')
watermark = Image.open('watermark.png')

photo.paste(watermark,(photo.width-150,photo.height-75),watermark)
photo.show()
photo.save('watermarkedimage.png')
