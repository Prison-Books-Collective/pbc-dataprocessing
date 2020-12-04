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
import re

#url = "http://localhost:8080/getBooksTitleContaining?targetString=u0"
#response = requests.get(url)
#if response.status_code == 200:
#	responsejson = response.json()
#	with open('unicodeTitles.txt', 'w') as outfile:
#		json.dump(responsejson, outfile)
file = open('unicodeTitles.txt')
data = json.loads(file.read())
file.close()

i = 1
length = len(data)
errors = []
url = "http://localhost:8080/updateBook"
for book in data:
	print(f'{i} out of {length}, ISBN10 {book["isbn10"]} ISBN13 {book["isbn13"]}')
	pattern = re.compile('''u0\w{3}''')
	bookTitle = book["title"]
	convertedMatches = []
	for match in pattern.finditer(bookTitle):
		matchStart = match.start()
		try:
			convertedMatches.append((match.group(), chr(int(bookTitle[matchStart+1:matchStart+5], 16))))
		except ValueError:
			errors.append((book["isbn10"], book["isbn13"]))
	if (len(convertedMatches) > 0):
		for match in convertedMatches:
			book["title"] = book["title"].replace(match[0], match[1])
		requests.put(url, json = book)
	i = i+ 1
print(errors)
errorsFile = open('unicodeERRORS.txt', "w")
errorsFile.write(errors)

