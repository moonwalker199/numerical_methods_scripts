def rk_4th_order(fxy, x0, y0, x_target, h):       
        # x_target : the value of x at which we want to find y
      
    n = int((x_target - x0) / h)  
    y = y0  
    
    for _ in range(n):
        k1 = h * fxy(x0, y)
        k2 = h * fxy(x0 + h / 2, y + k1 / 2)
        k3 = h * fxy(x0 + h / 2, y + k2 / 2)
        k4 = h * fxy(x0 + h, y + k3)
        
        # Update y and x
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x0 += h
    
    return y

#eg
def question(x,y):
  return (y-x)/y+x)

x0=0
y0=1
x_target=1
h=0.1

answer = rk_4th_order(question,x0,y0,x_target,h)
print(f" req. value of y at x={x_target} is {result})

