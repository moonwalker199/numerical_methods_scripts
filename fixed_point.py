def fixed_point_iteration(g, x0, tol):
    x1 = g(x0)
    while abs(x1 - x0) > tol:
        x0 = x1
        x1 = g(x0)
    return x1
def g1(x):
    return -2/(x**2-x)
root = fixed_point_iteration(g1, 0.5, 0.00001)
print("The root is: ", root)