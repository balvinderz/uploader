import pyimgur
CLIENT_ID = "82f73b28d4f67da"
path = "testpic2.jpg"
im=pyimgur.Imgur(CLIENT_ID)
uploaded_image=im.upload_image(path)
print(uploaded_image.link)
