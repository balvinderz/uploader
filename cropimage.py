from PIL import ImageOps
from PIL import Image

#img = "D:\\imgurpythonscript\\testpic2.jpg"
def cropImage(img):
    im= Image.open(img)
    #border=int(input("Enter border size :"))
    border=20
    width,height = im.size
    print(width)
    print(height)
    im2= ImageOps.crop(im,200)
    im2.save("check.jpg")
    im2.show()
