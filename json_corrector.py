from igdb.wrapper import IGDBWrapper
from igdb.igdbapi_pb2 import GameResult
import json

def get_genre_name(value):
    for genre in genres_json_list:
        if genre["id"] == value:
            return genre["name"]


wrapper = IGDBWrapper("wuhffr4x99fxpjxkp92msukdhqbl4u", "44e0zgdqkszuraanop58ucrnde1zcv")


file = open("allgames.json", "r")
games_list = json.load(file)


genres_file = open("genres.json", "r")
genres_json_list = json.load(genres_file)

counter = 0
for game in games_list:
    #CORRECT PLATFORM
    platform_list = game["platforms"]
    platform_list_new = []

    for platform in platform_list:
        platform_int = int(platform)
        match platform_int:
            case 34:
                platform_list_new.append("Android")
            case 39:
                platform_list_new.append("iOS")
            case 6:
                platform_list_new.append("PC") 
            case 167:
                platform_list_new.append("Playstation 5")
            case 48:
                platform_list_new.append("Playstation 4")
            case 169:
                platform_list_new.append("Xbox Series X|S")
            case 49:
                platform_list_new.append("Xbox One")

    game["platforms"] = platform_list_new


    #CORRECT GENRES
    genres_list = game["genres"]
    genre_list_new = []
    
    for genre in genres_list:
        genre_name = get_genre_name(genre)
        genre_list_new.append(genre_name)

    game["genres"] = genre_list_new


    #CORRECT DEVELOPER COMPANY
    if "involved_companies" in game.keys():
        involved_companies = game["involved_companies"]
        new_company_list = []

        for company in involved_companies:
            byte_array = wrapper.api_request(
                'involved_companies',
                'fields id, publisher; offset 0; where id = ' + str(company) + ";"
            )

            my_json = byte_array.decode('utf8').replace("'", '"')
            data = json.loads(my_json)
            if(data[0]["publisher"]):
                new_company_list.append(data[0]["id"])
                continue

        game["involved_companies"] = new_company_list 

    counter += 1
    print(counter)










s = json.dumps(games_list, indent=4, sort_keys=True)
file = open("allgames_corrected.json", "w")
file.write(s)
file.close()
