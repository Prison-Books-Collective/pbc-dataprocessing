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

getBaseUrl = "http://localhost:8080/getIsbn13?isbn13="
deleteBaseUrl = "http://localhost:8080/deleteBook?id="
updateBaseUrl = "http://localhost:8080/updateIsbn13?id="
booksFile = open('Isbn13WithNone copy.txt')
booksJsonString = booksFile.read()
completeJsonString = '''{"books": ''' + booksJsonString + '''}'''
booksData = json.loads(completeJsonString)

for book in booksData['books']:
	isbn13 = "978"+ book['isbn10']
	url = getBaseUrl+isbn13
	response = requests.get(url)
	if response.status_code == 200:
		responsejson = response.json()
		if responsejson['id'] != book['id']:
			print("BOOK WITH ISBN13 " + isbn13 + " FOUND")
			deleteUrl = deleteBaseUrl + str(responsejson['id'])
			deleteResponse = requests.delete(deleteUrl)
			if (deleteResponse.status_code == 200):
				print("and deleted")
			else:
				print("delete was funky")
	else:
		print("ISBN13 " + isbn13 + " of this book doesn't exist")
		updateUrl = updateBaseUrl + str(book['id'])+ "&isbn13=" + isbn13
		updateResponse = requests.put(updateUrl)
		if updateResponse.status_code == 200:
			print(" UPDATED THE ISBN")
		else:
			print("update went wrong")

