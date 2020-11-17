import json
import os

for file in os.listdir('books/'):
	if (file != '.DS_Store'):
		print(file + '\n')
		booksFile = open('books/'+file)
		booksJsonString = booksFile.read()
		booksData = json.loads(booksJsonString)

		output = file[:-4]+'_authors.txt'

		for book in booksData['books']:
			for authorIdInfo in book['authors']:
				authorId = authorIdInfo['key']
				foundAuthor = False
				authorsFiles = os.listdir('authors/')
				i = 0
				print("\n\n AUTHOR INFO \n\n")
				print(authorId)
				print('\n\n')

				while foundAuthor != True and i<len(authorsFiles):
					authorFileName = authorsFiles[i]
					if authorFileName != '.DS_Store':
						authorsFile = open('authors/'+authorFileName)
						authorsJsonString = authorsFile.read()
						authorsData = json.loads(authorsJsonString)
						
						authorsData['authors'] = sorted(authorsData['authors'], key=lambda x : x['id'], reverse=True)
						authors = authorsData['authors']
						low = 0
						high = len(authors)-1
						mid = 0
						while low <= high and foundAuthor != True:
							mid = low + (high-low)//2
							if(authors[mid]['id'] == authorId):
								book['key'] = authors[mid]['name']
								foundAuthor = True
								print('found \n')
							if(authors[mid]['id'] > authorId):
								low = mid +1
							else:
								high = mid - 1
					i = i+1

		outputFile = open(output, 'w')
		outputFile.write(booksData)
		outputFile.close()
		print('saved \n')

		booksFile.close()
