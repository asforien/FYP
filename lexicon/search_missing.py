import codecs

lexicon = codecs.open('lexicon.txt', encoding='utf-8')
ignore = ''.join(lexicon)
ignore += u'0123456789?()*-",\'\u3002\uFF08\uFF09\uFF1F\uFF0A\uFF0C'
with codecs.open('cantonese_matched_full.txt', encoding='utf-8') as transcribed:
	for row in transcribed:
		for char in row:
			if char not in ignore:
				print char,