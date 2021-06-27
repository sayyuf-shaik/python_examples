def factorial(number):
	#Logic to caluculate the factorial
	#5! = 5*4*3*2*1 = 120
	#for loop, decrease the number, multiply it and store the number
	product = 1
	for n in range(number):
		product = product * (number - n)
		#print(f"{product}")
	return product

number = int(input("Enter the number:"))
print(f'{number}! = {factorial(number)}')
