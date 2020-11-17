import json
import os

print(os.listdir('books/'))

for file in os.listdir('books/'):
	if (file != '.DS_Store'):
		print(file + '\n')
		openFile = open('books/' +file)
		jsonString = openFile.read()
		openFile.close()
		data = json.loads(jsonString)
		#os.remove('books/'+file)