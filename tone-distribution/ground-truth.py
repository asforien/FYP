import csv
import codecs

answers = {}
lexicon = {}

with codecs.open('lexicon.txt', 'rb', 'UTF-8') as lexiconFile:
	reader = csv.reader(lexiconFile, delimiter='\t')

	for row in reader:
		phrase = row[0]
		pronunciation = row[1]
		tones = ''.join(filter(lambda x: x.isdigit(), pronunciation))

		for word, tone in zip(phrase, tones):
			if word not in lexicon:
				lexicon[word] = ''
			lexicon[word] = tone;

with codecs.open('transcriptions.txt', 'rb', 'UTF-8') as inputFile:
	reader = csv.reader(inputFile, delimiter='\t')

	for row in reader:
		fileName = row[0]
		answers[fileName] = ''
		for word in row[1]:
			tone = lexicon[word]
			answers[fileName] += tone

with open('ground-truth.csv', 'w') as outputFile:
	writer = csv.writer(outputFile, delimiter=' ')

	for audioSet in answers:
		writer.writerow([audioSet] + [answers[audioSet]])