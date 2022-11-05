import requests # request img from web
import shutil # save img locally
import json


file = open("allgames_corrected_cover.json", "r")
games_list = json.load(file)

for game in games_list:
    url = game["cover"]
    id = game["id"]
    res = requests.get("https:" + url, stream = True)

    file_name = "images/" + str(id) + ".jpg"

    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')