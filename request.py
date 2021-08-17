# This code is from the postman software it reads image as bytes and transfer to the flask server

import requests

url = "http://192.168.0.100:5000/v1"

img=open("test_v1.jpg",'rb').read()
payload=img
headers = {
  'Content-Type': 'image/jpeg'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
