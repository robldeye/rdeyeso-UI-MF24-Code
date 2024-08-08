import sympy as sp

# Define the variable and the function
x = sp.symbols('x')
f = x**10

# Compute the first five derivatives
derivatives = [f]
for i in range(1, 6):
    derivative = sp.diff(derivatives[-1], x)
    derivatives.append(derivative)

# Print the derivatives with proper grammar
for i, derivative in enumerate(derivatives[1:], start=1):
    ordinal = "th"
    if i == 1:
        ordinal = "st"
    elif i == 2:
        ordinal = "nd"
    elif i == 3:
        ordinal = "rd"
        
    print(f"The {i}{ordinal} derivative of f(x) is: {derivative}")