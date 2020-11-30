#get all books with NONE- in isbn13 
#for each book
	# remove none, append 978
	# search for 978ISBN13
	# if it exists:
		# delete the other one
	# rename ISBN13 to 978

#in mysql - replace 978978 w "" if isbn10 is like 978978% and is more than 10 long
#
import requests
import json

url = "http://localhost:8080/getBooksTitleContaining?targetString=u0"
response = requests.get(url)
if response.status_code == 200:
	responsejson = response.json()
	with open('unicodeTitles.txt', 'w') as outfile:
		json.dump(responsejson, outfile)