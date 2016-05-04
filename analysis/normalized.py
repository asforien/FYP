import csv

answers = {}
subjectLanguages = {}
subjectInterfaces = {}

distributions = {}
subjectResults = {}
numTranscriptions = {}

with open('answers', 'r',) as answerFile:
	reader = csv.reader(answerFile, delimiter=',')

	for row in reader:
		answers[row[0]] = row[1]

with open('subjects', 'r',) as subjectFile:
	reader = csv.reader(subjectFile, delimiter=',')

	for row in reader:
		subjectLanguages[row[0]] = row[1]
		subjectInterfaces[row[0]] = row[2]

with open('transcriptions', 'r',) as transcriptionFile:
	outputFile = open('individual.csv', 'w')
	writer = csv.writer(outputFile, delimiter=',')

	reader = csv.reader(transcriptionFile, delimiter=',')

	for row in reader:
		subject = row[5]
		language = subjectLanguages[subject]
		interface = subjectInterfaces[subject]
		group = language + interface

		q_no = row[4]
		answer = answers[q_no]
		transcription = row[1]

		for t, a in zip(transcription, answer):
			writer.writerow([group, a, 1 if a == t else 0])