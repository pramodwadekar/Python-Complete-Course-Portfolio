import requests
import json
import os
city = input('enter the name of city = ')
url = f'http://api.weatherapi.com/v1/current.json?key=8204eae9ea4a4aaa8d660618232004&q={city}'
r= requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
print(wdic['location']['name'])
w=(wdic['current']['temp_c'])
print(w)
# os.system(f"say 'the current weather in {city} is {w} degrees'")
