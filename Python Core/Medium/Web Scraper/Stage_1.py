import requests

url = input()
response = requests.get(url)

try:
    print(response.json()['content'])
except KeyError:
    print('Invalid quote resource!')
