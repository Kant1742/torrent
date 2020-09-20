Torrent website in Python/Django.

subov.net

Easily populate data using JSON. Get that data you can using YTS API.

Features:
- Populate movies via API;
- Collections;
- Merch;
- Cast;
- Random moives on the main page;
- Latest movies;


How to get all the movies from YTS?

/my_torrent_data/get_detail_pages.py
- Set IDs in the forloop
      for "current_id" in range(20000, 20170):
      (in this case we will get all the movies with IDs from 20000 to 20169
- Change the "number_of_file" in writing()
    You will get JSON file named 'torrent_detail{number_of_file}.json' with all the data
- Send JSON data to url "/api/v1/" with POST method
