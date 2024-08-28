import math
def f1(x, y):
    return ((-2*y-1.958)/y)

def f2(x, y):
    return (math.pow((20.92-x**3)/3,1/3))

def fixed_point_iteration(x0, y0, tol=.5e-4, max_iter=100):
    x, y = x0, y0
    print(f"{'Iter':<5} {'x':<10} {'y':<10}")
    for i in range(max_iter):
        
        x_new = round(f1(x, y),6)
        y_new = round(f2(x, y),6)
        print(
            f"{round(i+1, 5):<5} {round(x_new, 5):<10} {round(y_new, 5):<10}"
        )
        if abs(x_new - x) < tol and abs(y_new - y) < tol:
            return x_new, y_new

        x, y = x_new, y_new

    print("Did not converge within the maximum number of iterations.")

if __name__ == "__main__":
    # Initial guesses
    x0 = 1.3
    y0 = -1.5

    x_approx, y_approx = fixed_point_iteration(x0, y0)

    print(f"Approximate solution: x = {round(x_approx,3)}, y = {round(y_approx,3)}")
