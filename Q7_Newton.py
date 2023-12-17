#Q7) WAP to implement Newton Method.

def f(x):
   return x**2 - 4*x + 4
def f_prime(x):
   return 2*x - 4
def f_double_prime(x):
   return 2

x0 = 3

tolerance = 1e-6

max_iterations = 100
   
for i in range(max_iterations):
   x1 = x0 - f_prime(x0) / f_double_prime(x0)
   if abs(x1 - x0) < tolerance:
    break

   x0 = x1
   
print()
print(f"Minimum Value: {f(x0)}")
print(f"Location: {x0}")