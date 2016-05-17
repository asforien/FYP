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

		# Group results
		group = language + interface

		if group not in distributions:
			distributions[group] = [[0 for x in range(6)] for y in range(6)]
			numTranscriptions[group] = 0

		numTranscriptions[group] += 1

		for t, a in zip(transcription, answer):
			distributions[group][int(a) - 1][int(t) - 1] += 1

		# Individual results
		if subject not in subjectResults:
			subjectResults[subject] = [0 for x in range(12)]

		for t, a in zip(transcription, answer):
			subjectResults[subject][int(a) + 5] += 1
			if t == a:
				subjectResults[subject][int(a) - 1] += 1

for group in distributions:
	correct = 0
	total = 0
	for row in distributions[group]:
		total += sum(row)
	for i in range(6):
		correct += distributions[group][i][i]
	print(group)
	print("Average score: " + str(correct/total))
	print("Number of subjects: " + str(numTranscriptions[group] / 3))
	print()

with open('distribution.csv', 'w') as outputFile:
	writer = csv.writer(outputFile, delimiter=',')

	for group in distributions:
		writer.writerow([group, numTranscriptions[group] / 3])
		for row in distributions[group]:
			writer.writerow(row)
		writer.writerow("")

with open('individual.csv', 'w') as outputFile:
	writer = csv.writer(outputFile, delimiter=',')

	for subject in subjectResults:
		results = subjectResults[subject]
		scores = [results[x] / results [x+6] for x in range(6)] + [sum(results[0:6]) / sum(results[6:12])]
		writer.writerow([subject, subjectLanguages[subject]] + scores)