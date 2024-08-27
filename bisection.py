import math
def func(x):
    return math.cos(x)-3*x+1
def bisection(a,b):
 
    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return
  
    c = a
    while (True):
        c = round((a+b)/2,5)
        print("    ".join(list(map(str,[a,b,c,round(func(c),5)]))))
        print()
        if (round(func(c), 3) == 0.0):
            break
        if (func(c)*func(a) < 0):
            b = c
        else:
            a = c
             
    print("The value of root is : ",round(c,3))
     

a = 0
b = 1
bisection(a, b)