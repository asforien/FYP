import csv
import random

answers = {}

random.seed()

with open('answers', 'r',) as answerFile:
	reader = csv.reader(answerFile, delimiter=',')

	for row in reader:
		answers[int(row[0])] = row[1]

with open('syllable_random.csv', 'w') as outputFile:
	writer = csv.writer(outputFile, delimiter=',')

	for q3 in range(3,18):

		matrix = [[0 for x in range(0,6)] for y in range(0,6)]
		for a in answers[1]:
			t = random.randint(1,6)
			writer.writerow([a, 1 if int(a) == t else 0])

		for a in answers[2]:
			t = random.randint(1,6)
			writer.writerow([a, 1 if int(a) == t else 0])

		for a in answers[q3]:
			t = random.randint(1,6)
			writer.writerow([a, 1 if int(a) == t else 0])