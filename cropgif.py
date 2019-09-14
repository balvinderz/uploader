
from PIL import ImageOps
from PIL import Image
from imgpy import Img

#img = "D:\\imgurpythonscript\\testpic2.jpg"
with Img(fp='giftest.gif') as im:
    border=30
    im.crop(box=(border, border, im.width-border, im.height-border))
    im.save(fp='crop.gif')
