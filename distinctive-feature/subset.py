import csv

targetLanguage = 'vietnamese'
transcriptionLanguages = ['english', 'mandarin', 'malay', 'tamil', 'hindi', 'thai', 'cantonese', 'spanish']

reader = csv.reader(open('distinctive-features.tsv'), delimiter='\t')

for row in reader:
	if  targetLanguage.lower() in row[0].lower():
		columnsToDelete = [i for i, v in enumerate(row) if v is '-']
		columnsToDelete.reverse()
		break

reader = csv.reader(open('distinctive-features.tsv'), delimiter='\t')
writer = csv.writer(open(targetLanguage + '.tsv', 'w'), delimiter='\t')

header = reader.next()
for index in columnsToDelete:
	del header[index]
writer.writerow(header)

for row in reader:
	if row[0] in transcriptionLanguages:
		for index in columnsToDelete:
			del row[index]
		writer.writerow(row)