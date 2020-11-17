import json
import requests

print('loading books \n')
#removeDuplicates.json - books with BOTH isbns have been added
#removeDuplicates_andcompleteISBN - has books with one isbn all added
#store above two isbns in set, if new data comes in only output isbns that dont match
booksFile = open('removedDuplicates_andcompleteISBNs.json')
booksJsonString = booksFile.read()
booksData = json.loads(booksJsonString)
booksFile.close()

lengthTotal = len(booksData['books'])

currentLength = len(booksData['books'])

url = "http://localhost:8080/addBook"
i = 0
for book in booksData['books']:
	isbn10 = ""
	isbn13 = ""
	if len(book['isbn_10'])> 0:
		isbn10 = book['isbn_10'][0]
	if len(book['isbn_13'])> 0:
		isbn13 = book['isbn_13'][0]
	if (isbn10 != "") and (isbn13 != ""):
		data = {'title': book['title'], 'isbn10': isbn10, 'isbn13': isbn13, 'authors': book['authors']}
		response = requests.post(url, json = data)
		if (response.status_code == 200):
			print(str(currentLength) + " of " + str(lengthTotal) + " added")
		elif (response.status_code == 302):
			print(str(currentLength) + " of " + str(lengthTotal) + " ISBN10: " + isbn10 + " ISBN13: " +isbn13 + " already exists")
		else:
			print(str(currentLength) + " of " + str(lengthTotal) + " something strange happened")
	else:
		print(str(currentLength) + " of " + str(lengthTotal) + " missing isbns")
	i = i + 1
	currentLength = lengthTotal - i




