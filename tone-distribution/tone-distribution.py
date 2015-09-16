import csv
import codecs

distributionsBySet = {}
lexicon = {}

with codecs.open('lexicon.txt', 'rb', 'UTF-8') as lexiconFile:
	reader = csv.reader(lexiconFile, delimiter='\t')

	for row in reader:
		print(row[0])
		phrase = row[0]
		pronunciation = row[1]
		tones = ''.join(filter(lambda x: x.isdigit(), pronunciation))

		for word, tone in zip(phrase, tones):
			if word not in lexicon:
				lexicon[word] = ''
			lexicon[word] = tone;

print(lexicon)

with codecs.open('transcriptions.txt', 'rb', 'UTF-8') as inputFile:
	reader = csv.reader(inputFile, delimiter='\t')

	for row in reader:
		fileName = row[0][:23]
		if fileName not in distributionsBySet:
			distributionsBySet[fileName] = [0] * 7

		for word in row[1]:
			tones = lexicon[word]
			for tone in tones:
				distributionsBySet[fileName][int(tone)] += 1

with open('tone-distribution.csv', 'w') as outputFile:
	writer = csv.writer(outputFile, delimiter=' ')

	for audioSet in distributionsBySet:
		writer.writerow([audioSet] + distributionsBySet[audioSet])