#Q10) WAP to implement Taylor polynomial.
import math

def factorial(n):
   if n == 0:
      return 1
   return n * factorial(n - 1)

def taylor_coefficient(func, point, degree, derivative_order):
    return func(point) / factorial(derivative_order)
    
def taylor_polynomial(func, degree, point, var='x'):
    x = point
    taylor_poly = sum(taylor_coefficient(func, point, i, i) * (x - point)**i for i
    in range(degree + 1))   
    return taylor_poly

def sin_function(x):
    return math.cos(x)

degree_of_polynomial = 3
center_point = 0

taylor_poly = taylor_polynomial(sin_function, degree_of_polynomial, center_point)

print("Taylor Polynomial:", taylor_poly)