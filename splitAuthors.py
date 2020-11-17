import csv
import sys
input = 'ol_dump_2020-09-30.txt'
output = 'authors/authors.txt'
smallFile = None
csv.field_size_limit(sys.maxsize)
with open(input, 'r') as csvinputfile:
    csvreader = csv.reader(csvinputfile, delimiter='\t')
    i = 0
    count= 0 
    for row in csvreader:
        if len(row) > 4:
          if (row[0] == '/type/author'):
            if i % 75000 == 0:
                if smallFile:
                    smallFile.seek(smallFile.tell()-1)
                    smallFile.write(']}')
                    smallFile.close()
                smallFileName = 'authors'+str(count)+'.txt'
                count = count + 1
                smallFile = open(smallFileName, "w")
                smallFile.write('''{"authors":[''')
            i = i + 1
            entry = row[4]

            startName = entry.find('''"name":''')
            endName = entry.find('''",''', startName)

            name = entry[startName+9:endName]
            name = name.replace('"', "'")
            name = name.replace("\\",r"")
            name = '''"name": "''' + name + '''"''' 


            if (startName == -1) or (len(str(name))<10):
              name = '''"name": ""'''

            startId = entry.find('''"/authors/''')
            endId = entry.find('''",''', startId)
            authorId = entry[startId:endId+1]
            smallFile.write('{' + name + ', "id": ' + authorId + '},')
    if smallFile:
        smallFile.seek(smallFile.tell()-1)
        smallFile.write(']}')
        smallFile.close()
print('Finished reading')
print('Finished writing')