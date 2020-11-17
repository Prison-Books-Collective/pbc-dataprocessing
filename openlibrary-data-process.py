import csv
import sys
input = 'ol_dump_2020-09-30.txt'
output = 'books.txt'
csv.field_size_limit(sys.maxsize)
with open(output, 'w') as outputfile:
    with open(input, 'r') as csvinputfile:
        outputfile.write('{"books": [')
        csvreader = csv.reader(csvinputfile, delimiter='\t')
        for row in csvreader:
            if len(row) > 4:
              if (row[0] == '/type/edition'):
                entry = row[4]

                startTitleIndex = entry.find('''"title":''')
                endTitleIndex = entry.find('''",''', startTitleIndex+10)
                title = entry[startTitleIndex:endTitleIndex+1]
                if (title.count("")> 6):
                  endTitleIndex = entry.find('''"''', startTitleIndex+10)
                  title = entry[startTitleIndex:endTitleIndex+1]

                
                title = title.replace('\\"',r'"')
                  

                startAuthorsIndex = entry.find('''"authors":''')
                endAuthorsIndex = entry.find('''"}],''', startAuthorsIndex)
                authors = entry[startAuthorsIndex:endAuthorsIndex+3]

                if (startAuthorsIndex == -1):
                  authors = '''"authors": []'''


                outputfile.write('{' + title + ", " + authors + '},')
               # outputfile.write(entry + '\n\n')
        outputfile.seek(outputfile.tell()-1)
        outputfile.write(']}')
    print('Finished reading')
print('Finished writing')