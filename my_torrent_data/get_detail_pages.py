import json
import requests

# For populating your models you can use requsests.POST()
# or serializers, or "python manage.py loaddata torrents.json"


def get_json():
    current_id = 1
    all_torrents = []
    all_slugs = []

    for current_id in range(20000, 20170):
        try:
            r = requests.get(
                f'https://yts.mx/api/v2/movie_details.json?movie_id={current_id}&with_images=true&with_cast=true')
            my_data = r.json()['data']['movie']

            my_data_slug = r.json()['data']['movie']['slug']
            if my_data_slug in all_slugs:
                # Delete this movie from the request
                popped = my_data.pop['movie']
            else:
                all_slugs.append(my_data_slug)

            all_torrents.append(my_data)
            current_id += 1
            print(current_id, '---------- current_id')
        except:
            current_id += 1
    return all_torrents


def writing():
    number_of_file = 43

    try:
        # with open('torrent_detail.json', 'a') as f:  # Добавить в файл
        with open(f'torrent_detail{number_of_file}.json', 'w') as file:    # Перезаписать
            to_write = get_json()
            json.dump(to_write, file)
    except:
        pass

writing()
