import urllib
import json
from .models import Movie

# you can also keep this inside a view
with open('torrent30_copy.json') as data_file:
    json_data = json.loads(data_file.read())

    # for movie_data in json_data:
    #     movie = Movie.create(**movie_data)
        # movie and genres created

#     for aLine in data_file:
#         for this, the, the_other in someGenerator( aLine ):
#             object= Movie.objects.create( field1=this, field2=that, field3=the_other )
#             object.save()

# def someGenerator( url ):
#     # open the URL with urllib2
#     # parse the data with BeautifulSoup
#     yield this, that, the_other 