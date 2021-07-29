""" This is a basic Python request code where you can just send strings or messages of json format to the server(API handler)""" 


import requests

params = {'param0': 'Rohith', 'param1': 'param1'}

url='http://127.0.0.1:5000/json'
response = requests.post(url, json=params)

print(response.text)
