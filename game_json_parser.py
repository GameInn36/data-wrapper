from igdb.wrapper import IGDBWrapper
from igdb.igdbapi_pb2 import GameResult
import json

wrapper = IGDBWrapper("wuhffr4x99fxpjxkp92msukdhqbl4u", "44e0zgdqkszuraanop58ucrnde1zcv")
file = open("game_ids.txt", "r")

id_query = "("

for id in file:
    id = id.rstrip()
    id_query += id + ","

id_query = id_query[:-1]
id_query += ")"


print(id_query)
'''With a wrapper instance already created'''
# JSON API request

byte_array = wrapper.api_request(
            'games',
            'fields id, name, summary, genres, involved_companies, platforms, first_release_date, cover; limit 100; offset 0; where id = ' + id_query + ";"
          )

my_json = byte_array.decode('utf8').replace("'", '"')
#print(my_json)
#print('- ' * 20)

# Load the JSON to a Python list & dump it back out as formatted JSON
data = json.loads(my_json)
s = json.dumps(data, indent=4, sort_keys=True)
file = open("allgames.json", "w")
file.write(s)
file.close()

exit()

byte_array = wrapper.api_request(
            'games',
            'fields id, name, total_rating; limit 25; offset 0; where first_release_date > 1383645272 & category = 0 & total_rating > 80 & platforms = {34,39}; sort total_rating desc;'
          )
# parse into JSON however you like...

my_json = byte_array.decode('utf8').replace("'", '"')
#print(my_json)
#print('- ' * 20)

# Load the JSON to a Python list & dump it back out as formatted JSON
data = json.loads(my_json)
for game in data:
    if (not game["id"] in game_id_list):
        game_id_list.append(game["id"])



byte_array = wrapper.api_request(
            'games',
            'fields id, name, total_rating; limit 15; offset 0; where first_release_date > 1383645272 & category = 0 & total_rating > 80 & platforms = 167; sort total_rating desc;'
          )

my_json = byte_array.decode('utf8').replace("'", '"')
#print(my_json)
#print('- ' * 20)

# Load the JSON to a Python list & dump it back out as formatted JSON
data = json.loads(my_json)
for game in data:
    if (not game["id"] in game_id_list):
        game_id_list.append(game["id"])