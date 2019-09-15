import requests
client_id = "2_ge5Nca"
client_secret = "V7idgMVa-xTKKrBAFXGJzBANlFv9xXnIxQTQ7eegui-MUTHIlYmtd0WWU6M-eH1X"


def get_token():
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    url = "https://api.gfycat.com/v1/oauth/token"
    r = requests.post(url, data=str(payload), headers={
                      'User-Agent': "Slow down bot"})

    response = r.json()

    access_token = response["access_token"]
    print(access_token)
    return access_token


get_token()
