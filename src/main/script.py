import json
''' Предположим я так могу сделать для каждого элемента в файле, затем
найти позицию id и вставить перед ним название модели main.movie, перед жанрами вставить
название модели main.genres, перед торрентами - main.quality и т.д
Затем все, что получилось записать в новый файл, а оттуда сделать loaddata


Я знаю как выглядит нужный мне json, как получить все поля (id, description...)
и как вставить перед ними необходимое мне название модели для loaddata.
По сути есть готовое решение через этот скрипт, только я еще хочу все же попробовать
через сериализацию. Мне кажется, так должно быть гораздо лучше. Иначе это просто хуета
'''

from django.core import serializers


with open('torrent30_copy.json') as f:
    data = json.load(f)
    # i = 0
    # tell = f.tell()
    # try:
    #     while True:
    #         print(data[i]["id"])
    #         print(tell)
    #         i += 1
    # except:
    #     pass


# Creating a new file with all the data
# with open('gotovoe.json', 'w') as f:
#     json.dump(data, f)

    # for i in data:
    #     print(data[i]["id"])
    # print(data[1]['id'])



    # for line in f.readlines():
    #     if '"id"' in line:
    #         print(line.strip())
        # удалять не надо, лучше выбирать из того файла что нужно, это просто возможность
        # if '"title_long"' in line:
            # del line['title_long']
            # print(line.strip())
    # print(f.readlines()[3])
