def read_lastnlines(fname,n):
	with open('file1.txt') as f:
		for line in (f.readlines() [-n:]):
			print(line)

read_lastnlines('file1.txt',3)