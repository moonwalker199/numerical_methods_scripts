# Python3 code for implementation of Newton
# Raphson Method for solving equations

# An example function whose solution 
# is determined using Bisection Method. 
# The function is x^3 - x^2 + 2
import math


def func( x ):
	return math.pow(math.e,x)-4*x

# Derivative of the above function 
# which is 3*x^x - 2*x
def derivFunc( x ):
	return math.pow(math.e,x)-4

# Function to find the root
def newtonRaphson( x ):
	h = func(x) / derivFunc(x)
	while abs(round(h,7)) != 0:
		
		h = func(x)/derivFunc(x)
		
		# x(i+1) = x(i) - f(x) / f'(x)
		
		print("    ".join(list(map(str,[round(x,7),round(func(x),7),round(derivFunc(x),7),round(-1*h,7),round(x-h,7)]))))
		x-=h
	print("The value of the root is : ",
							round(x,5))

# Driver program to test above
x0 = 0.5 # Initial values assumed
newtonRaphson(x0)

# This code is contributed by "Sharad_Bhardwaj"
