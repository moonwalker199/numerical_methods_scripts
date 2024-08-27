# Python3 implementation of Bisection
# Method for solving equations

import math


MAX_ITER = 1000000

# An example function whose solution
# is determined using Regular Falsi Method. 
# The function is x^3 - x^2 + 2
def func( x ):
	return (x**3-3*x+1)

# Prints root of func(x) in interval [a, b]
def regulaFalsi( a , b):
	if func(a) * func(b) >= 0:
		print("You have not assumed right a and b")
		return -1
	
	c = a # Initialize result
	
	for i in range(MAX_ITER):
		
		# Find the point that touches x axis
		c = (a * func(b) - b * func(a))/ (func(b) - func(a))
		print("    ".join(list(map(str,[round(a,5),round(func(a),5),round(b,5),round(func(b),5),round(c,5),round(func(c),5)]))))
		# Check if the above found point is root
		if round(func(c), 5) == 0.0:
			break
		
		# Decide the side to repeat the steps
		elif func(c) * func(a) < 0:
			b = round(c,6)
		else:
			a = round(c,6)
	print("The value of root is : " , round(c,3))

# Driver code to test above function
# Initial values assumed
a =0
b = 1
regulaFalsi(a, b)