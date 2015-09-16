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
inp = raw_input('Enter Jyutping: ')
m = p.findall(inp)

# Check if input is valid Jyutping
validInput = True

if len(m) is 0:
	validInput = False
	print 'No valid Jyutping found'

for match in m:
	if (match[0] not in onsets or
		match[1] not in nuclei or
		match[2] not in codas or
		match[3] is ''):
			validInput = False
			print 'Input is not valid:', ''.join(match)
			break

if validInput:
	yale = []
	for match in m:
		yale.append(onsets[match[0]][1])
		yale.append(nuclei[match[1]][1])
		yale.append(codas[match[2]][1])
		yale.append(match[3])
	yale = ''.join(yale)

	# Exceptions: aa without coda becomes a, yyu becomes yu
	aa_p = re.compile(r'aa([1-6])')
	jyu_p = re.compile(r'yyu')
	yale = jyu_p.sub('yu', yale)
	yale = aa_p.sub(r'a\1', yale)

	print yale,

	xsampa = []
	for match in m:
		xsampa.append(onsets[match[0]][0])
		xsampa.append(nuclei[match[1]][0])
		xsampa.append(codas[match[2]][0])
		xsampa.append('_' + match[3])
		xsampa.append('.')
	xsampa.pop()

	print ' '.join(filter(None, xsampa))