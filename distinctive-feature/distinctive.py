import csv

phonemeFeatures = {}		# Distinctive features for each phoneme
languageInventories = {}	# Phoneme inventories for each language
languageFeatures = {}		# Distinctive features used in each language
featureNames = []			# List of distinctive features
numFeatures = 0

with open('phoible-segments-features.tsv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter='\t')
	featureNames = reader.next()[1:]
	numFeatures = len(featureNames)

	for row in reader:
		segment = row[0]
		phonemeFeatures[segment] = row[1:]

with open('phoible-phonemes.tsv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile, delimiter='\t')

	for row in reader:
		if 't' in row['CombinedClass']:
			continue
		inventory = row['LanguageName'].lower()
		if inventory not in languageInventories:
			languageInventories[inventory] = []
		phoneme = row['Phoneme']
		languageInventories[inventory].append(phoneme)

missingPhonemes = []

for key in languageInventories:
	languageFeatures[key] = ['-'] * numFeatures
	inventory = languageInventories[key]

	for i in range(numFeatures):
		hasNegInstance = False
		hasPosInstance = False

		for phoneme in inventory:
			if phoneme not in phonemeFeatures:
				if phoneme not in missingPhonemes:
					missingPhonemes.append(phoneme)
				continue;
			if phonemeFeatures[phoneme][i] is '+':
				hasPosInstance = True
			elif phonemeFeatures[phoneme][i] is '-':
				hasNegInstance = True

		if hasPosInstance and hasNegInstance:
			languageFeatures[key][i] = '+'

print '\nPhonemes not found in Phoible:'
for phoneme in missingPhonemes:
	print phoneme.decode('utf8'),
print '\n'

with open('distinctive-features.tsv', 'w') as outputFile:
	writer = csv.writer(outputFile, delimiter='\t')
	writer.writerow(['Language'] + featureNames)

	for language in languageFeatures:
		writer.writerow([language] + languageFeatures[language])