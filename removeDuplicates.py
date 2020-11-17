import json

print('loading books \n')

booksFile = open('data/books_authors copy.txt')
booksJsonString = booksFile.read()
booksData = json.loads(booksJsonString)

output = 're.json'
bookLength = len(booksData['books'])
totalBookLength = len(booksData['books'])

print(totalBookLength)
bookSet = set()
newBookData = []
i = 0
bothISBNs = 0
isbn10Only = 0
isbn13Only = 0
noISBN = 0

for book in booksData['books']:
	
	bookLength = bookLength - 1

	isbn10 = ""
	isbn13 = ""
	if len(book['isbn_10'])> 0:
		isbn10 = book['isbn_10'][0]
	if len(book['isbn_13'])> 0:
		isbn13 = book['isbn_13'][0]
	isbn10_empty = isbn10 == ""
	isbn13_empty = isbn13 == ""
	outcome = ""
	#if both isbn10 and 13 exist, they've already been added to the db
	if not isbn10_empty and not isbn13_empty:
		outcome = " both ISBNs exist"
		bothISBNs = bothISBNs + 1
	#if they're both empty, dont want to record them
	elif isbn10_empty and isbn13_empty:
		outcome = book
		noISBN = noISBN + 1
	else:
		bookFound = False
		if not isbn10_empty and isbn13_empty:
			isbn10Only = isbn10Only + 1
			#if its already in the set
			if isbn10 in bookSet:
				#we found it
				bookFound = True
			else:
				#otherwise add it
				bookSet.add(isbn10)
			isbn13 = "NONE-"+isbn10	

		elif isbn10_empty and not isbn13_empty:
			isbn13Only = isbn13Only + 1
			if isbn13 in bookSet:
				bookFound = True
			else:
				bookSet.add(isbn13)
			isbn10 = "NONE-"+isbn13 #set it to NONE and it's isbn13
		

		if not bookFound:
			authors = []
			for authorIdInfo in book['authors']:
				if 'key' in authorIdInfo:
					if authorIdInfo['key'] not in authors:
						authors.append(authorIdInfo['key'])
			book['authors'] = authors
			book['isbn_10']= [isbn10]
			book['isbn_13'] = [isbn13]
			newBookData.append(book)
	print(str(bookLength) + ' of ' + str(totalBookLength) + str(outcome))
	
newBookJson = {"books" : newBookData}
newJson = json.dumps(newBookJson)

outputFile = open(output, 'w')
outputFile.write(newJson)
outputFile.close()

booksFile.close()

print("Both ISBNs exist: " + str(bothISBNs))
print("Only ISBN 10 exists: " + str(isbn10Only))
print("Only ISBN 13 exists: " + str(isbn13Only))
print("No ISBNs exist: " + str(noISBN))
