# def get_data_from_json():
#     pass
import json
import requests

with open('my_torrent_data/torrents_jsons/torrent30.json', 'r') as f:
    datafile = f.readlines()
    # Use regular expressions?
    print(f.read().find('id'))
    for line in datafile:
       if 'id' in line:
            pass        

# ------------------------- #
delete_list = ["id", "title_english", "title_long"]   
input_file = "my_torrent_data/torrents_jsons/torrent30.json"
output_file = "cleaned_file.json"

with open(input_file, 'r') as f:
    with open(output_file, 'w+') as o:
        for line in f:
            for word in delete_list:
                # replace a word with ""
                line = pass
                # line = line.replace(word, "")
            # replace and write
            o.write(line)
