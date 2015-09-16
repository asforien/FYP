import re
import csv

onsets = {}
nuclei = {}
codas = {}

with open('onset.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		onsets[row['Jyutping']] = (row['X-SAMPA'], row['Yale'])

with open('nucleus.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		nuclei[row['Jyutping']] = (row['X-SAMPA'], row['Yale'])

with open('coda.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		codas[row['Jyutping']] = (row['X-SAMPA'], row['Yale'])

p = re.compile(r'([b-df-hj-np-tvwxz]*)([aeiou]{1,3}|yu|m|ng)(ng|[ptkmn])?([1-6])')

outputfile = open('lexicon.txt', 'w')
with open('ccdict-unicode', 'rb') as inputfile:
	reader = csv.reader(inputfile)
	for row in reader:
		outputfile.write(row[0])
		outputfile.write('\t')
		m = p.findall(row[1])

		yale = []

		for match in m:
			yale.append(onsets[match[0]][1])
			yale.append(nuclei[match[1]][1])
			yale.append(codas[match[2]][1])
			yale.append(match[3])
			yale.append(' # ')
		yale.pop()

		yale = ''.join(yale)

		# Exceptions: aa without coda becomes a, yyu becomes yu
		aa_p = re.compile(r'aa([1-6])')
		jyu_p = re.compile(r'yyu')

		yale = jyu_p.sub('yu', yale)
		yale = aa_p.sub(r'a\1', yale)

		outputfile.write(yale)
		outputfile.write('\t')

		xsampa = []
		for match in m:
			xsampa.append(onsets[match[0]][0])
			xsampa.append(nuclei[match[1]][0])
			xsampa.append(codas[match[2]][0])
			xsampa.append('_' + match[3])
			xsampa.append('#')
		xsampa.pop()

		outputfile.write(' '.join(filter(None, xsampa)))
		outputfile.write('\n')