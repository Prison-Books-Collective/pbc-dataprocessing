import json
import os

for file in os.listdir('authors/'):
	if (file != '.DS_Store'):
		print(file + '\n')
		readFile = open('authors/'+file)
		writeFile = open('authors/sorted_'+file,"w")
		jsonString = readFile.read()
		data = json.loads(jsonString)
		data['authors'] = sorted(data['authors'], key=lambda x : x['id'], reverse=True)
		writeFile.write(json.dumps(data))
		writeFile.close()
		readFile.close()
