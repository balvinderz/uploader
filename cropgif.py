
from PIL import ImageOps
from PIL import Image
from imgpy import Img

#img = "D:\\imgurpythonscript\\testpic2.jpg"
def cropgif(path):
    with Img(fp=path) as im:
        border=30
        im.crop(box=(border, border, im.width-border, im.height-border))
        im.save(fp='crop.gif')
        return "crop.gif"
