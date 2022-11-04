from igdb.wrapper import IGDBWrapper
from igdb.igdbapi_pb2 import GameResult
import json

wrapper = IGDBWrapper("wuhffr4x99fxpjxkp92msukdhqbl4u", "44e0zgdqkszuraanop58ucrnde1zcv")

'''With a wrapper instance already created'''
# JSON API request
byte_array = wrapper.api_request(
            'games',
            'fields id, name, genres; offset 0; where id=48;'
          )
# parse into JSON however you like...


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

