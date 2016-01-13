import os
import csv

pitch = {}
intensity = {}
syllables = []
features = []

for fn in os.listdir('praat'):
	f = open('praat/' + fn, 'r')
	reader = csv.reader(f, delimiter=' ')
	pitch[fn] = [0]
	intensity[fn] = [0]
	for row in reader:
		pitch[fn].append(row[1])
		intensity[fn].append(row[2])

with open('syllable_alignments.csv') as inputFile:
	reader = csv.reader(inputFile, delimiter=' ')
	for row in reader:
		syllables.append([row[0], row[1], row[2], row[5]])

for s in syllables:
	start = int(float(s[1]) * 100)
	duration = int(float(s[2]) * 100)

	for i in range(start, start + duration + 1):
		print(pitch[s[0]][i])
	print()

# for i, s in enumerate(syllables):
# 	if (i > 0) and syllables[i][0] == syllables[i-1][0]: 
# 		prev_syllable = syllables[i-1]

# 	curr_syllable = syllables[i]

# 	if (i < len(syllables) - 1) and syllables[i][0] == syllables[i+1][0]: 
# 		next_syllable = syllables[i+1]