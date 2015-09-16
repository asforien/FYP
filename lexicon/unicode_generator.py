import csv

outp = open('ccdict-unicode', 'w')

with open('ccdict', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter='\t')
	for row in reader:
		outp.write(unichr(int(row[0], 16)).encode('utf8'))
		outp.write(',')
		outp.write(row[1])
		outp.write('\n')