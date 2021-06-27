def function():
	print("Inside the function")
	a = 10
	print(a)
	#varaible 'a' can be accesed inside the function since 
	#the scope/namespace exists untill the function terminates
	def inside_function():
		print("Inside the enclosing function")
		print(a)
		b = "b"
	#Throws Error because the inside_function() 
	#namespace ends 
	#So the name is undefined
	print(b)
	inside_function()

function()
