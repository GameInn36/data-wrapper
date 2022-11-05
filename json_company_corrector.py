from igdb.wrapper import IGDBWrapper
from igdb.igdbapi_pb2 import GameResult
import json


wrapper = IGDBWrapper("wuhffr4x99fxpjxkp92msukdhqbl4u", "44e0zgdqkszuraanop58ucrnde1zcv")


file = open("allgames_corrected_company.json", "r")
games_list = json.load(file)


counter = 0
for game in games_list:
    #CORRECT publisher COMPANY
    if "cover" in game.keys():

        byte_array = wrapper.api_request(
                'covers',
                'fields id, url; offset 0; where id = ' + str(game["cover"]) + ";"
            )

        my_json = byte_array.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        if (len(data) != 0):
            game["cover"] = data[0]["url"]
        else:
            game.pop("cover")
    counter += 1
    print(counter)






s = json.dumps(games_list, indent=4, sort_keys=True)
file = open("allgames_corrected_cover.json", "w")
file.write(s)
file.close()
