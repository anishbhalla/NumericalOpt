# WAP to implement steepest descent method.
import numpy as np
def objective_function(x):
   return x**2 + 4*x + 4
def gradient(x):
   return 2*x + 4
def steepest_descent(initial_guess, learning_rate, tolerance):
   x = initial_guess
   while True:
      grad_value = gradient(x)
       
      if np.linalg.norm(grad_value) < tolerance:
         break # Convergence criteria met
     
      x = x - learning_rate * grad_value
      
   return x, objective_function(x)

# Initial guess, learning rate, and tolerance
initial_guess = np.array([0.0])
learning_rate = 0.1
tolerance = 1e-6

result = steepest_descent(initial_guess, learning_rate, tolerance)

print("Optimal solution: x =", result[0])
