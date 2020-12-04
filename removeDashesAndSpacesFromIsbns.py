#get all books with '-' in the isbn10
#for each book
	# remove '-'
	# search for new isbn
	# if it exists:
		# delete book with '-'
	#else
		# update book

#get all books with ' ' in the isbn10
#for each book
	# remove ' '
	# search for new isbn
	# if it exists:
		# delete book with ' '

#get all books with '-' in the isbn13
#for each book
	# remove '-'
	# search for new isbn
	# if it exists:
		# delete book with '-'

#get all books with ' ' in the isbn13
#for each book
	# remove ' '
	# search for new isbn
	# if it exists:
		# delete book with ' '
import json
import requests

file = open('dashes.txt')
data = json.loads(file.read())
file.close()

i = 1
length = len(data)
errors = []
getUrl = "http://localhost:8080/getIsbn13?isbn13="
deleteUrl = "http://localhost:8080/deleteBook?id="
updateUrl = "http://localhost:8080/updateIsbn13?id="

for book in data:
	book["isbn13"] = book["isbn13"].replace('-','')
	response = requests.put(updateUrl+str(book["id"])+"&isbn13="+book["isbn13"])
	
	print(f'{i} out of {length}, ISBN10 {book["isbn10"]} ISBN13 {book["isbn13"]}')
	i = i+ 1

