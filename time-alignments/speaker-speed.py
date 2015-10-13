import csv

numSyllables = {}
durations = {}

with open('ground-truth.csv', 'rb') as inputFile:
	reader = csv.reader(inputFile, delimiter=' ')

	for row in reader:
		fileName = row[0]
		numSyllables[fileName] = len(row[1])

with open('durations-full', 'rb') as inputFile:
	reader = csv.reader(inputFile, delimiter=' ')

	for row in reader:
		fileName = row[0].replace('.mp3', '')
		durations[fileName] = float(row[1])

with open('speaker-speed.csv', 'w') as outputFile:
	writer = csv.writer(outputFile, delimiter=' ')

	for audio in numSyllables:
		writer.writerow([audio] + [numSyllables[audio] / durations[audio]])