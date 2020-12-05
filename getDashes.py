import requests
import json
import re

url = "http://localhost:8080/getBooksIsbn13Containing?targetString=-"
response = requests.get(url)
if response.status_code == 200:
	responsejson = response.json()
	with open('dashes.txt', 'w') as outfile:
		json.dump(responsejson, outfile)