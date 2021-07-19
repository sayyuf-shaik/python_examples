import sys

def fibonaci(number):
	if number <= 1:
		return number
	return fibonaci(number - 1) + fibonaci(number - 2)

number = int(sys.argv[1])
total = 0

while fibonaci(total) <= number:
	print(fibonaci(total))
	total += 1


