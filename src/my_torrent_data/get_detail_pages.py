import json
import requests

# For populating your models you can use requsests.POST()
# or serializers, or "python manage.py loaddata torrents.json"


def get_json():
    current_id = 1
    all_torrents = []

    try:
        for current_id in range(1, 4):
            r = requests.get(
                f'https://yts.mx/api/v2/movie_details.json?movie_id={current_id}&with_images=true&with_cast=true')
            my_data = r.json()['data']['movie']
            all_torrents.append(my_data)
            current_id += 1
    except:
        print('HANDLE AN EXCEPTION', current_id)
    return all_torrents



# def new_torrent_file(number=1):
#     with open(f"torrent_detail{number}.json", "w") as file:
#         to_write = get_json()
#         json.dump(to_write, file)
#         print('Created a new file')


def writing():
    number_of_file = 0

    try:
        # with open('torrent_detail.json', 'a') as f:  # Добавить в файл
        with open('torrent_detail.json', 'w') as file:    # Перезаписать
            to_write = get_json()
            json.dump(to_write, file)

            # tell = file.tell()
            # print(tell)
            # if tell > 50000:
            #     new_torrent_file(number_of_file)
            #     number_of_file += 1
    except:
        pass

get_json()
writing()
