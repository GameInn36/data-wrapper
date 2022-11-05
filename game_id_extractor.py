from igdb.wrapper import IGDBWrapper
from igdb.igdbapi_pb2 import GameResult
import json

wrapper = IGDBWrapper("wuhffr4x99fxpjxkp92msukdhqbl4u", "44e0zgdqkszuraanop58ucrnde1zcv")


game_id_list = []


byte_array = wrapper.api_request(
            'games',
            'fields id, name, total_rating; limit 15; offset 0; where first_release_date > 1383645272 & category = 0 & total_rating > 80 & platforms = 48; sort total_rating desc;'
          )

my_json = byte_array.decode('utf8').replace("'", '"')

data = json.loads(my_json)
for game in data:
    if (not game["id"] in game_id_list):
        game_id_list.append(game["id"])




byte_array = wrapper.api_request(
            'games',
            'fields id, name, total_rating; limit 25; offset 0; where first_release_date > 1383645272 & category = 0 & total_rating > 80 & platforms = {34,39}; sort total_rating desc;'
          )

my_json = byte_array.decode('utf8').replace("'", '"')

data = json.loads(my_json)
for game in data:
    if (not game["id"] in game_id_list):
        game_id_list.append(game["id"])


byte_array = wrapper.api_request(
            'games',
            'fields id, name, total_rating; limit 15; offset 0; where first_release_date > 1383645272 & category = 0 & total_rating > 80 & platforms = 167; sort total_rating desc;'
          )

my_json = byte_array.decode('utf8').replace("'", '"')

data = json.loads(my_json)
for game in data:
    if (not game["id"] in game_id_list):
        game_id_list.append(game["id"])


byte_array = wrapper.api_request(
            'games',
            'fields id, name, total_rating; limit 15; offset 0; where first_release_date > 1383645272 & category = 0 & total_rating > 5 & platforms = {6,167,169}; sort total_rating desc;'
          )

my_json = byte_array.decode('utf8').replace("'", '"')

data = json.loads(my_json)
for game in data:
    if (not game["id"] in game_id_list):
        game_id_list.append(game["id"])


byte_array = wrapper.api_request(
            'games',
            'fields id, name, total_rating; limit 30; offset 0; where first_release_date > 1383645272 & category = 0 & total_rating > 5 & platforms = {6,48,49}; sort total_rating desc;'
          )

my_json = byte_array.decode('utf8').replace("'", '"')

data = json.loads(my_json)
for game in data:
    if (not game["id"] in game_id_list):
        game_id_list.append(game["id"])

print(len(game_id_list))

file = open("game_ids.txt", "w")
for game_id in game_id_list:
    file.write(str(game_id) + "\n")
    
file.close()
exit()


my_json = byte_array.decode('utf8').replace("'", '"')
#print(my_json)
#print('- ' * 20)

# Load the JSON to a Python list & dump it back out as formatted JSON
data = json.loads(my_json)
for game in data:
    print(game["id"])
s = json.dumps(data, indent=4, sort_keys=True)
file = open("games.json", "w")
file.write(s)
file.close()
exit()

byte_array = wrapper.api_request(
            'platforms',
            'fields id, name; limit 500; offset 0; sort id asc;'
          )
# parse into JSON however you like...

platforms_json = json.loads(byte_array)
file = open('platforms.json', 'w')
json.dump(platforms_json, file)
file.close()



byte_array = wrapper.api_request(
            'covers',
            'fields id, url; offset 0; where id=105006;'
          )

print(json.loads(byte_array))

genres_byte_array = wrapper.api_request(
            'genres',
            'fields id, name; limit 100;'
          )


genres_json = json.loads(genres_byte_array)
file = open('genres.json', 'w')
json.dump(genres_json, file)
file.close()


# Protobuf API request
"""
byte_array = wrapper.api_request(
            'games.pb', # Note the '.pb' suffix at the endpoint
            'fields id, name; offset 0; where platforms=48;'
          )
games_message = GameResult()
games_message.ParseFromString(byte_array) # Fills the protobuf message object with the response
"""

