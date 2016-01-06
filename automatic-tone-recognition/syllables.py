import csv

vowels = [3, 4, 5, 8, 11, 17, 22, 23, 25, 28, 29, 30, 31, 32, 34]
diphthongs = [22, 23, 25, 31, 32, 34]
finals = [13, 15, 16, 18, 20, 27]
consonants = [6, 7, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 24, 26, 27, 33]

phones = {}
syllables = []
transcriptions = {}
lexicon = {}
phone_repr = [0] * 35

with open('cantonese_matched_full.txt') as inputFile:
	reader = csv.reader(inputFile, delimiter=':')
	for row in reader:
		transcriptions[row[0]] = row[1]

with open('lexicon.txt') as inputFile:
	reader = csv.reader(inputFile, delimiter='\t')
	for row in reader:
		phrase = row[0]
		pronunciations = row[1].split(' ')
		for idx, val in enumerate(phrase):
			lexicon[val] = pronunciations[idx]

with open('CA_alignments.txt', 'r') as inputFile:
	reader = csv.reader(inputFile, delimiter=' ')

	for row in reader:
		fileName = row[0]
		if fileName not in phones:
			phones[fileName] = []
		if row[4] != '1':
			phones[fileName].append((float(row[2]), float(row[3]), int(row[4])))

with open('CA_phones.txt') as inputFile:
	reader = csv.reader(inputFile, delimiter=' ')

	for row in reader:
		phone_repr[int(row[1])] = row[0]

syllabic_consonant_strs = ['m', 'ng']
vowel_strs = ['a', 'e', 'i', 'o', 'u']

for fileName in phones:
	segment_idx = 0
	segments = phones[fileName]

	for symbol in transcriptions[fileName]:
		lexicon_entry = lexicon[symbol]
		tone = lexicon_entry[-1:]

		start = None
		syllable_repr = ''

		try:
			# syllabic consonant
			segment = segments[segment_idx]
			if lexicon_entry[:-1] in syllabic_consonant_strs:
				if segment[2] != 15 and segment[2] != 27:
					continue
				segment_idx += 1
				start = segment[0]
				syllable_repr += phone_repr[segment[2]]
			else:
				# initial
				if lexicon_entry[0] not in vowel_strs and segments[segment_idx][2] not in vowels:

					segment = segments[segment_idx]
					segment_idx += 1
					start = segment[0]
					syllable_repr += phone_repr[segment[2]]

					# dz, gw, kw
					segment = segments[segment_idx]
					if (phone_repr[segment[2]] is 'z' or 
						phone_repr[segment[2]] is 'w'):
						segment_idx += 1
						syllable_repr += phone_repr[segment[2]]

				# nucleus
				segment = segments[segment_idx]
				segment_idx += 1

				# missing initial 'ng'
				if not start and phone_repr[segment[2]] == 'ng':
					start = segment[0]
					syllable_repr += phone_repr[segment[2]]
					segment = segments[segment_idx]
					segment_idx += 1

				if not start:
					start = segment[0]
				syllable_repr += phone_repr[segment[2]]

				# diphthongs
				segment = segments[segment_idx]
				if segment[2] in diphthongs:
					segment_idx += 1
					syllable_repr += phone_repr[segment[2]]

				# final
				segment = segments[segment_idx]
				if (segment[2] in finals and
				(lexicon_entry[-2:-1] not in vowel_strs or
				segments[segment_idx+1][2] not in vowels)):
					segment_idx += 1
					syllable_repr += phone_repr[segment[2]]

			last_segment = segments[segment_idx-1]
			duration = last_segment[0] + last_segment[1] - start

			syllables.append([fileName, start, '{0:.2f}'.format(duration), symbol, syllable_repr, tone])
		except IndexError:
			continue

with open('syllable_alignments.csv', 'w') as outputFile:
	writer = csv.writer(outputFile, delimiter=' ')

	for syllable in syllables:
		writer.writerow(syllable)
