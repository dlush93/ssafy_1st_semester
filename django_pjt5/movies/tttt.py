from .models import Genre
import requests as resq
import json


url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=69570904cbfa7d422a8a753a576d8c32&language=ko-KR'

res= resq.get(url)
js =  json.loads(res.text)
te = js['genres']

for gen in te:
    # print(genre['id'],genre['name'])
    a= Genre.objects.get(id=[gen['id']])
    print(a)
