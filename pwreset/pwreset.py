pw = input('please set up your password:')
chance = 0
while chance < 3:
	pw_try = input('please enter your password:')
	if pw_try == pw:
		print('success logged on')
		break
	else:
		if chance >= 0 and chance < 2: 
		    print('incorrect password', 2-chance, 'more times')
		elif chance == 2:
		    print('failed, account locked')
	chance = chance + 1	