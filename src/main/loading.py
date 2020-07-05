import json
from .models import Movie

# you can also keep this inside a view
with open('torrent30_copy.json', encoding='utf-8') as data_file:
    json_data = json.loads(data_file.read())

    for movie_data in json_data:
        movie = Movie.create(**movie_data)
        # movie and genres created
