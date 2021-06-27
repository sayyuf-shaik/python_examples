#Armstrong Number: Any number that is order of n, 
#where n is number of digits
#abcd.. = pow(a, n) + pow(b, n) + pow(c, n) + pow(d, n) + .. = abcd..
#Example: 153 = 1*1*1 + 5*5*5 + 3*3*3 = 153
# 120 = 1*1*1 + 2*2*2 + 0*0*0 = 120
def count_digits(number):
	count = 0
	while number != 0:
		number = number//10
		count = count + 1
	return count

def armstrong(number):
	#Count the digits
	count = count_digits(number)
	armstrong_number = 0
	while number != 0:
		remainder = number % 10
		armstrong_number = armstrong_number + remainder ** count
		number = number // 10
	return armstrong_number
	
number = int(input("Enter the number:"))
print(f'Armstrong Number: {True if armstrong(number) == number else False}')
