import os
import csv
import math

pitch = {}
intensity = {}
syllables = []
feature_vectors = []

for fn in os.listdir('praat'):
	f = open('praat/' + fn, 'r')
	reader = csv.reader(f, delimiter=' ')
	pitch[fn] = [0]
	intensity[fn] = [0]
	next(reader)
	for row in reader:
		if row[1] == '--undefined--':
			row[1] = 0
		if row[2] == '--undefined--':
			row[2] = 0
		pitch[fn].append(float(row[1]))
		intensity[fn].append(float(row[2]))

# pitch normalization
for key in pitch:
	old_pitch = pitch[key][1:]
	f_min = min([x for x in old_pitch if x != 0])
	f_max = max(old_pitch)
	new_pitch = [0]
	for f0 in old_pitch:
		if f0 == 0:
			new_pitch.append(0)
		else:
			new_pitch.append(math.log(f0 / f_min, 10) / math.log(f_max / f_min, 10) * 4 + 1)
	pitch[key] = new_pitch

with open('syllable_alignments.csv') as inputFile:
	reader = csv.reader(inputFile, delimiter=' ')
	for row in reader:
		syllables.append([row[0], row[1], row[2], row[5]]) # filename, start, duration, tone

for s in syllables:
	start = int(float(s[1]) * 100)
	duration = int(float(s[2]) * 100)
	unvoiced = 0

	feature_vector = []

	while pitch[s[0]][start] == 0 and start < len(pitch[s[0]]) - 1:
		start += 1
		unvoiced += 1
		duration -= 1

	for i in range(1, 9):
		time = start + duration * i // 9
		pitch_feature = pitch[s[0]][time]
		feature_vector.append(pitch_feature)

	for i in range(0, 3):
		start = start + duration * i // 3
		end = start + duration * (i+1) // 3
		intensities = intensity[s[0]][start:end]
		intensities = [x for x in intensities if x != -1]
		if len(intensities) == 0:
			intensities = [0]
		average_intensity = sum(intensities) / len(intensities)
		feature_vector.append(average_intensity)

	feature_vector.append(unvoiced)
	feature_vector.append(duration)

	feature_vector.append(s[3])
	feature_vectors.append(feature_vector)

with open('features.csv', 'w') as outputFile:
	writer = csv.writer(outputFile, delimiter=',')

	for fv in feature_vectors:
		writer.writerow(fv)