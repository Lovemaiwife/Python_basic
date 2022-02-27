import os

# read file
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			good, price = line.strip().split(',')
			products.append([good, int(price)])
		print(products)
	return products

# user input
def user_input(products):
	while True:
		good = input('please enter the name of the good: ')
		if good == 'q':
			break
		price = input('please enter the price of the good: ')
		products.append([good, int(price)])
	print(products)
	return products

# analyze and print
def analyze(products):
	cost = 0
	for product in products:
		print(product)
		cost += product[1]
	print('you bought a total of', len(products), 'items')
	print('Total cost is', cost, 'dollars')
	print('average cost is', cost / len(products), 'dollars')

# write file
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for product in products:
			f.write(product[0] + ',' + str(product[1]) + '\n')
	print('file_write is completed')

def main():
	filename = input('Please enter file name to read or create file: ')
	if os.path.isfile(filename):
		print('file found')
		products = read_file(filename)
	else:
		print('cannot not find exsiting file, creating new file.')
	products = user_input(products)
	analyze(products)
	write_file(filename, products)

main()