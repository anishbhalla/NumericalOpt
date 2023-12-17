#Q8) WAP to implement gradient descent method.
import sympy as sp
def gradient_descent(initial_x, learning_rate, num_iterations):
   x = sp.symbols('x')   
   
   f = x**2 + 5*x + 6
   
   df = sp.diff(f, x)
   
   f_prime = sp.lambdify(x, df, 'numpy')
   
   for _ in range(num_iterations):
      gradient = f_prime(initial_x)
      initial_x = initial_x - learning_rate * gradient
      
   return initial_x, f.subs(x, initial_x)

initial_x = 0
learning_rate = 0.1
num_iterations = 1000

min_x, min_value = gradient_descent(initial_x, learning_rate, num_iterations)

print(f"Minimum value is {min_value} at x = {min_x}")