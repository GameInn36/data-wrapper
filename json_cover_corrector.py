from igdb.wrapper import IGDBWrapper
from igdb.igdbapi_pb2 import GameResult
import json

def get_genre_name(value):
    for genre in genres_json_list:
        if genre["id"] == value:
            return genre["name"]


wrapper = IGDBWrapper("wuhffr4x99fxpjxkp92msukdhqbl4u", "44e0zgdqkszuraanop58ucrnde1zcv")


file = open("allgames_corrected.json", "r")
games_list = json.load(file)


genres_file = open("genres.json", "r")
genres_json_list = json.load(genres_file)

counter = 0
for game in games_list:
    #CORRECT publisher COMPANY
    if "involved_companies" in game.keys():
        game["publisher"] = game.pop("involved_companies")

        byte_array = wrapper.api_request(
                'companies',
                'fields id, name, changed_company_id; offset 0; where id = ' + str(game["id"]) + ";"
            )

        my_json = byte_array.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        if (len(data) != 0):
            game["publisher"] = data[0]["name"]
        else:
            game.pop("publisher")
    counter += 1
    print(counter)










s = json.dumps(games_list, indent=4, sort_keys=True)
file = open("allgames_corrected_company.json", "w")
file.write(s)
file.close()
