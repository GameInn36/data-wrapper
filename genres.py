from igdb.wrapper import IGDBWrapper
from igdb.igdbapi_pb2 import GameResult
import json

wrapper = IGDBWrapper("wuhffr4x99fxpjxkp92msukdhqbl4u", "44e0zgdqkszuraanop58ucrnde1zcv")

'''With a wrapper instance already created'''
# JSON API request

byte_array = wrapper.api_request(
            'genres',
            'fields id, name; limit 100; offset 0; sort id asc;'
          )

my_json = byte_array.decode('utf8').replace("'", '"')
#print(my_json)
#print('- ' * 20)

# Load the JSON to a Python list & dump it back out as formatted JSON
data = json.loads(my_json)
s = json.dumps(data, indent=4, sort_keys=True)
file = open("genres.json", "w")
file.write(s)
file.close()

exit()