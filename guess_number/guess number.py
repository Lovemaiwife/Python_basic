# guess number

import random
low = int(input('Please enter low limit: '))
high = int(input('Please enter high limit: '))

ans = random.randint(low, high)
count = 0
while True:
    count += 1
    guess = int(input('please make a guess: '))
    if guess == ans: 
    	print('You got it!!')
    	print('you have guessed for', count, 'times')
    	break
    elif guess >= ans:
    	print('Try smaller')
    elif guess <= ans:
    	print('Try bigger')
    print('you have guessed for', count, 'times')