import json
import os

for file in os.listdir('authors/'):
	if (file != '.DS_Store'):
		print(file + '\n')
		openFile = open('authors/'+file)
		jsonString = openFile.read()
		openFile.close()
		data = json.loads(jsonString)
		#os.remove('authors/'+file)