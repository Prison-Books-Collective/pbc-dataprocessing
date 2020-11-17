import json
import os



authorId = "/authors/OL3941664A"
foundAuthor = False
authorsFiles = os.listdir('authors/')
i = 0


while foundAuthor != True and i<len(authorsFiles):
	authorFileName = authorsFiles[i]
	if authorFileName != '.DS_Store':
		print(authorFileName)
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
			print(authors[mid]['id'])

			if(authors[mid]['id'] == authorId):
				book['key'] = author['name']
				foundAuthor = True
				print('found \n')
			if(authors[mid]['id'] > authorId):
				low = mid +1
			else:
				high = mid - 1
		authorsFile.close()
	i = i+1
