import json

print('loading books \n')

booksFile = open('books.txt')
booksJsonString = booksFile.read()
booksData = json.loads(booksJsonString)

print('loading authors \n')

authorsFile = open('authors.txt')
authorsJsonStr = authorsFile.read()
authorsData = json.loads(authorsJsonStr)

output = 'books_authors.json'
print('sorting \n')
authors = sorted(authorsData['authors'], key=lambda x : x['id'])
bookLength = len(booksData['books'])

for book in booksData['books']:
	print(bookLength)
	bookLength = bookLength - 1
	if book['title'].find("'/type/")>0:
		book['title'] = ""
	for authorIdInfo in book['authors']:
		if 'key' in authorIdInfo:
			authorId = authorIdInfo['key']
			foundAuthor = False
			low = 0
			high = len(authors) -1
			mid = 0
			while low <= high and foundAuthor != True:
				mid = low + (high-low)//2

				if (authors[mid]['id'] == authorId):
					authorIdInfo['key'] = authors[mid]['name']
					foundAuthor = True
				if(authors[mid]['id'] < authorId):
					low = mid +1
				else:
					high = mid - 1

newJson = json.dumps(booksData)

outputFile = open(output, 'w')
outputFile.write(newJson)
outputFile.close()

booksFile.close()
