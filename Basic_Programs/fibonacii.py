import sys

number = int(sys.argv[1])

a = 0
b = 1
sum = 0
while sum <= number:
	print(sum)
	a = b
	b = sum 
	sum = a + b
	


