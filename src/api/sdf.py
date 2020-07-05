from serializers import MovieSerializer

data = {
    "id": 1049,
    "url": "https://yts.mx/movies/employee-of-the-month-2006",
    "imdb_code": "tt0424993",
    "title": "Employee of the Month",
    "title_english": "Employee of the Month",
    "title_long": "Employee of the Month (2006)",
    "slug": "employee-ssof-the-month-sdfs2006",
    "year": 2006,
    "rating": 5.5,
    "runtime": 103,
    "genres": [
            "Action",
            "Comedy",
            "Romance"
    ],
    "summary": "a record eighteenth time in a row, he will be rewarded with entrance into the ...",
    "description_full": "Slacker Zack Bnto the ...",
    "synopsis": "Slacker nth,into the ...",
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

serializer = MovieSerializer(data=data)
serializer.is_valid()
