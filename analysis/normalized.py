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
	reader = csv.reader(transcriptionFile, delimiter=',')

	for row in reader:
		subject = row[5]
		language = subjectLanguages[subject]
		interface = subjectInterfaces[subject]

		q_no = row[4]
		answer = answers[q_no]
		transcription = row[1]

		# Individual results
		if subject not in subjectResults:
			subjectResults[subject] = [[0 for x in range(6)] for y in range(6)]

		for t, a in zip(transcription, answer):
			subjectResults[subject][int(a) - 1][int(t) - 1] += 1

with open('individual.csv', 'w') as outputFile:
	writer = csv.writer(outputFile, delimiter=',')

	for subject in subjectResults:
		language = subjectLanguages[subject]
		interface = subjectInterfaces[subject]
		group = language + interface

		array = []

		results = subjectResults[subject]
		for row in results:
			array.extend([x / sum(row) for x in row])

		writer.writerow([group] + array)