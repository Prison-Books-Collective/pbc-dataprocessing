#get all books with NONE- in isbn13 
#for each book
	# remove none, append 978
	# search for 978ISBN13
	# if it exists:
		# delete the other one
	# rename ISBN13 to 978

import requests
import json

getBaseUrl = "http://localhost:8080/addZine"
zineFile = open('zines.txt')
zines = zineFile.readlines()

for zine in zines:
	code = zine[0:3]
	
	title = zine[4:]
	data = {'title': title, 'threeLetterCode': code}
	response = requests.post(getBaseUrl, json = data)
	if (response.status_code== 200):
		print("added " + code)
	else:
		print ( "didnt add " + code)

