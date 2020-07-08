# importing the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "http://127.0.0.1:8000/api/v1/"

# data to be sent to api
data = {
    "id": 1049,
    "url": "https://yts.mx/movies/employee-of-the-month-2006",
    "imdb_code": "tt0424993",
    "title": "FROM sending_requests.py",
    "title_english": "Employee of the Month",
    "title_long": "Employee of the Month (2006)",
    "slug": "emplwsaoyeasflksddsefde-ssofd-the-sadamonth-2006",
    "year": 2006,
    "rating": 5.5,
    "runtime": 103,
    "genres": [
        {
            "title":"Action",
            "title":"Comedy",
            "title":"Romance"
        }

    ],
    "summary": "Slacker Zack Bradley works as a box boy at Super Club, a warehouse club store. It is the lowest in the j rewarded with entrance into the ...",
    "description_full": "Slacker Zack Bradley wor be rewarded with entrance into the ...",
    "yt_trailer_code": "JK-SWgsDp7Q",
    "language": "English",
    "mpa_rating": "PG-13",
    "background_image": "https://yts.mx/assets/images/movies/Employee_of_the_Month_2006/background.jpg",
    "background_image_original": "https://yts.mx/assets/images/movies/Employee_of_the_Month_2006/background.jpg",
    "small_cover_image": "https://yts.mx/assets/images/movies/Employee_of_the_Month_2006/small-cover.jpg",
    "medium_cover_image": "https://yts.mx/assets/images/movies/Employee_of_the_Month_2006/medium-cover.jpg",
    "large_cover_image": "https://yts.mx/assets/images/movies/Employee_of_the_Month_2006/large-cover.jpg",
    "state": "ok",
    "torrents": [
        {
            "url": "https://yts.mx/torrent/download/EE9ED85E654E5297F2C8AAB272C7E66AB62FE48A",
            "hash": "EE9ED85E654E5297F2C8AAB272C7E66AB62FE48A",
            "quality": "720p",
            "type": "bluray",
            "seeds": 5,
            "peers": 1,
            "size": "750.66 MB",
            "size_bytes": 787124060,
            "date_uploaded": "2015-10-31 23:13:49",
            "date_uploaded_unix": 1446329629
        },
        {
            "url": "https://yts.mx/torrent/download/BAF6FC610C91963BB6981B33516D58452DAAF074",
            "hash": "BAF6FC610C91963BB6981B33516D58452DAAF074",
            "quality": "1080p",
            "type": "bluray",
            "seeds": 19,
            "peers": 2,
            "size": "1.50 GB",
            "size_bytes": 1610612736,
            "date_uploaded": "2015-10-31 23:13:50",
            "date_uploaded_unix": 1446329630
        }
    ],
    "date_uploaded": "2015-10-31 23:13:49",
    "date_uploaded_unix": 1446329629
}

# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, data=data, auth=("admin", "admin"))

# before accessing to deserialized object we need to call .is_valid()
# extracting response text
output = r.text

print("HUETA - :%s" % output)
