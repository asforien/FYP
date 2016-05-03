import csv

answers = {}
subjectLanguages = {}
subjectInterfaces = {}

transcriptions = {}
subjectResults = {}

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

		q_no = int(row[4])
		transcription = row[1]

		# Group results
		group = language + interface

		if group not in transcriptions:
			transcriptions[group] = {1: [], 2: []}

		if q_no == 1 or q_no == 2:
			transcriptions[group][q_no].append(transcription)

with open('majority.csv', 'w') as outputFile:
	writer = csv.writer(outputFile, delimiter=',')

	for group in transcriptions:
		writer.writerow([group])

		writer.writerow("1")
		for transcription in transcriptions[group][1]:
			writer.writerow(transcription)
		writer.writerow("")

		writer.writerow("2")
		for transcription in transcriptions[group][2]:
			writer.writerow(transcription)
		writer.writerow("")