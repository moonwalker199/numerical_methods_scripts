import math
import numpy as np

def f1(x, y):
    return math.log(x**2 + y) -2 + y

def f2(x, y):
    return math.sqrt(x) + x*y - 0.4

def f1x(x, y):
    return 2 * x/(x**2+y)

def f1y(x, y):
    return 1 / (x**2+y)

def f2x(x, y):
    return 1/(2*math.sqrt(x)) +y

def f2y(x, y):
    return x

def jacobian(x, y):
    """Compute the Jacobian matrix for the system of equations."""
    j11 = f1x(x, y)
    j12 = f1y(x, y)
    j21 = f2x(x, y)
    j22 = f2y(x, y)
    return np.array([[j11, j12], [j21, j22]])

def newton_raphson(x0, y0, tol=0.5e-3, max_iter=20):
    x, y = x0, y0
    print(f"{'Iter':<5} {'x':<10} {'y':<10} {'f1(x,y)':<10} {'f2(x,y)':<10} {'df1/dx':<10} {'df1/dy':<10} {'df2/dx':<10} {'df2/dy':<10} {'delta_x':<10} {'delta_y':<10} {'x_new':<10} {'y_new':<10}")   
    for i in range(max_iter):
        f_val = np.array([f1(x, y), f2(x, y)])
        J = jacobian(x, y)
        try:
            delta = np.linalg.solve(J, -f_val)
        except np.linalg.LinAlgError:
            print("Jacobian is singular.")
            return None, None
        
        x_new = round(x + round(delta[0], 5), 5)
        y_new = round(y + round(delta[1], 5), 5)
        
        print(
            f"{i+1:<5} {round(x, 5):<10} {round(y, 5):<10} {round(f1(x, y), 5):<10} "
            f"{round(f2(x, y), 5):<10} {round(f1x(x, y), 5):<10} {round(f1y(x, y), 5):<10} "
            f"{round(f2x(x, y), 5):<10} {round(f2y(x, y), 5):<10} "
            f"{round(delta[0], 5):<10} {round(delta[1], 5):<10} "
            f"{round(x_new, 5):<10} {round(y_new, 5):<10}"
        )

        # Check convergence
        if np.linalg.norm(delta, ord=2) < tol:
            print(f"Converged after {i+1} iterations.")
            return x_new, y_new

        x, y = x_new, y_new

    print("Did not converge within the maximum number of iterations.")
    return x, y

if __name__ == "__main__":
    # Initial guesses
    x0 = 1.5*2
    y0 = 0

    x_approx, y_approx = newton_raphson(x0, y0)

    
    print(f"Approximate solution: x = {round(x_approx,3)}, y = {round(y_approx,3)}")
