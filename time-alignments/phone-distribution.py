import csv

distributionsBySet = {}

with open('CA_alignments.txt', 'rb') as inputFile:
	reader = csv.reader(inputFile, delimiter=' ')

	for row in reader:
		fileName = row[0][:23]
		if fileName not in distributionsBySet:
			distributionsBySet[fileName] = [0] * 35
		distributionsBySet[fileName][int(row[4])] += 1

with open('phone-distribution.csv', 'w') as outputFile:
	writer = csv.writer(outputFile, delimiter=' ')

	for audioSet in distributionsBySet:
		writer.writerow([audioSet] + distributionsBySet[audioSet])