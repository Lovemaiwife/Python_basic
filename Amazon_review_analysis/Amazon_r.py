#Amazon_review
data = []
count = 0
with open('reviews.txt') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 10000 == 0:
			print(len(data))

length = 0
for letter in data:
	length += len(letter)
print('average length of each review is', length / len(data), 'letters.')

length_100 = []
for review in data:
    if len(review) < 100:
    	length_100.append(review)
print('a total of', len(length_100) + 1, 'reviews are shorter than 100 characters')

while True:
	print('enter the number of review to read reviews shorter than 100 charaters, the maximum number your can enter is', len(length_100) + 1)
	read = int(input('enter 0 to exit:'))
	if read == 0:
		print('exits program of review with <100 characters')
		break
	elif read >= 1 and read <= len(length_100) + 1:
		print(length_100[read - 1])
	else:
		print('data not valid')

good = []
for review in data:
	if 'good' in review:
	 	good.append(review)
print('there are', len(good), 'reviews includes the word "good."')
print(' the first review with "good":', good[0])

