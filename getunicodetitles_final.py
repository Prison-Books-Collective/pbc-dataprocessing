import requests
import json
import re

url = "http://localhost:8080/getBooksTitleContaining?targetString=u0"
response = requests.get(url)
if response.status_code == 200:
	responsejson = response.json()
	with open('unicodeTitles.txt', 'w') as outfile:
		json.dump(responsejson, outfile)