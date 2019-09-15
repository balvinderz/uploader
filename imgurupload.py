import requests
from imgurpython import ImgurClient
client_id = "82f73b28d4f67da"  # imgur
secret="4a08aed2e3d2886bc98d25357ba49e057dbc0b28"
refresh_token="7e21b3803f931a0015cbe54c85d58d8a13c00858"
access_token="d3dd23f77b279f48ae93311ab3e6ae1bd3873974"
import time
from selenium import webdriver
def uploadtoimgur(path):
    path = "testpic2.jpg"
    client = ImgurClient(client_id, secret)
    #global refresh_token
    #if(refresh_token==""):
    authorization_url = client.get_auth_url('token')
    #driver=webdriver.Chrome()
    #driver.get(authorization_url)
    print(authorization_url)
    driver=webdriver.Chrome()
    driver.get(authorization_url)
    #credentials = client.authorize(, 'pin')
    #print(authorization_url)
    #request = requests.get(authorization_url)
    
    #print(request.text)
    uploaded_image = client.upload_from_path(path)
    print(uploaded_image['link'])
    return uploaded_image['link']
uploadtoimgur('testpic2.jpg')
