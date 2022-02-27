wc = {} # words count
rp = 0 #review progress
with open('reviews.txt') as f:
	for reviews in f:
		words = reviews.split(' ')
		for word in words:
			if word not in wc:
				wc[word] = 1
			else:
				wc[word] += 1
		rp += 1
		if rp % 100000 == 0:
			print(rp)
for word in wc:
	if wc[word] > 1000:
		print(word, wc[word])
print(len(wc), 'words in the dictionary in total')
while True:
	lookup = input('Please enter the word to lookup, enter q to exit: ')
	if lookup == 'q':
		break
	elif lookup not in wc:
		print('the word is not mentioned in any review')
		continue
	print(wc[lookup])

