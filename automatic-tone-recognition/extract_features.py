import os
import csv

pitch = {}
intensity = {}

for fn in os.listdir('praat'):
	f = open('praat/' + fn, 'r')
	reader = csv.reader(f, delimiter=' ')
	pitch[fn] = []
	intensity[fn] = []
	for row in reader:
		pitch[fn].append(row[1])
		intensity[fn].append(row[2])

with open('syllable_alignments.csv') as inputFile:
	reader = csv.reader(inputFile, delimiter=':')
	for row in reader:
		transcriptions[row[0]] = row[1]