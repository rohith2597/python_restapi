import requests

params = {'param0': 'Rohith', 'param1': 'param1'}


response = requests.post('http://127.0.0.1:5000/json', json=params)

print(response.text)
