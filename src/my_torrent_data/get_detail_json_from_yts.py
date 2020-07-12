

import json
import requests

# For populating your models you can use requsests.POST()
# or serializers, or "python manage.py loaddata torrents.json"


def get_json():
    limit = 50
    page = 1
    all_torrents = []

    while True:
        try:
            response = requests.get(f'https://yts.mx/api/v2/movie_details.json?movie_id={id}&with_images=true&with_cast=true',
                                    params={
                                        'limit': limit,
                                        'page': page,
                                    })
            my_data = response.json()['data']['movies']
            all_torrents.extend(my_data)
            page += 1
            id += 1
        except:
            pass
    return all_torrents


def new_torrent_file(number=1):
    with open(f"torrent{number}.json", "w") as file:
        to_write = get_json()
        json.dump(to_write, file)
        print('Created a new file')


def writing():
    number_of_file = 0

    try:
        # with open('torrent.json', 'a') as f:  # Добавить в файл
        with open('torrent.json', 'w') as file:    # Перезаписать
            to_write = get_json()
            json.dump(to_write, file)

            tell = file.tell()
            # print(tell)
            # if tell > 50000:
            #     new_torrent_file(number_of_file)
            #     number_of_file += 1
    except:
        pass

print(get_json())
writing()
