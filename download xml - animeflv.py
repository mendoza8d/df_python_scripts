import requests

URL = "https://www3.animeflv.net/browse"

response = requests.get(URL)
with open('animeflv.xml', 'wb') as file:
    file.write(response.content)