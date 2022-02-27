def read_file(filename1):
	output = []
	with open(filename1, 'r', encoding='utf-8') as f:
		for line in f:
			if 'Allen' + '\n' in line or 'Tom' + '\n' in line:
				name = line.strip()
			else:
				output.append(name + ': ' + line)
	return output

def write_file(filename2, output):
	with open(filename2, 'w', encoding='utf-8') as f:
		for line in output:
			# string = ''
			# for x in line:
			# 	string += x
			f.write(line)

def main():
	read_file('input.txt')
	output = read_file('input.txt')
	write_file('output.txt', output)

main()