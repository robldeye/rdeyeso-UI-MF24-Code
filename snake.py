import sympy as sp

# Define the variable and the function
x = sp.symbols('x')
f = x**10

# Compute the first five derivatives
derivatives = [f]
for i in range(1, 6):
    derivative = sp.diff(derivatives[-1], x)
    derivatives.append(derivative)

# Print the derivatives
for i, derivative in enumerate(derivatives[1:], start=1):
    print(f"The {i} derivative of f(x) is: {derivative}")