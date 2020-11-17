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

                name = entry[startTitleIndex+10:endTitleIndex]
                name = name.replace('"', "'")
                name = name.replace("\\", r"")

                title = '''"title": "''' + name + '''"''' 

                startAuthorsIndex = entry.find('''"authors":''')
                endAuthorsIndex = entry.find('''],''', startAuthorsIndex)
                authors = entry[startAuthorsIndex:endAuthorsIndex+1]

                isbn_10_start = entry.find('''"isbn_10":''')
                isbn_10_end = entry.find('''"]''', isbn_10_start)
                isbn_10 = entry[isbn_10_start: isbn_10_end+2]

                isbn_13_start = entry.find('''"isbn_13":''')
                isbn_13_end = entry.find('''"]''', isbn_13_start)
                isbn_13 = entry[isbn_13_start: isbn_13_end+2]

                if (startAuthorsIndex == -1):
                  authors = '''"authors": []'''

                if (isbn_10_start == -1 or isbn_10_end == -1 or len(isbn_10) < 25):
                  isbn_10 = '''"isbn_10": []'''

                if (isbn_13_start == -1 or isbn_13_end == -1 or len(isbn_13) < 28):
                  isbn_13 = '''"isbn_13": []'''
                  
                outputfile.write('{' + title + ", " + authors + ", " + isbn_10+ ", " + isbn_13+'},')
        outputfile.seek(outputfile.tell()-1)
        outputfile.write(']}')
    print('Finished reading')
print('Finished writing')