import csv
import sys
input = 'ol_dump_2020-09-30.txt'
output = 'authors.txt'
csv.field_size_limit(sys.maxsize)
with open(output, 'w') as outputfile:
    with open(input, 'r') as csvinputfile:
        outputfile.write('{"authors": [')
        csvreader = csv.reader(csvinputfile, delimiter='\t')
        for row in csvreader:
            if len(row) > 4:
              if (row[0] == '/type/author'):
                entry = row[4]

                startName = entry.find('''"name":''')
                endName = entry.find('''",''', startName)
                name = entry[startName:endName+1]

                if (startName == -1):
                  name = '''"name": ""'''

                startId = entry.find('''"/authors/''')
                endId = entry.find('''",''', startId)
                authorId = entry[startId:endId+1]
                outputfile.write('{' + name + ', "id": ' + authorId + '},')
        outputfile.seek(outputfile.tell()-1)
        outputfile.write(']}')
    print('Finished reading')
print('Finished writing')