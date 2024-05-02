# Get user input for integer and floating-point numbers
a = float(input("Enter a number (a): "))
b = float(input("Enter another number (b): "))
c = int(input("Enter an integer (c): "))

# Perform arithmetic operations
sum_bc = b + c
difference_ab = a - b
product_ab = a * b
quotient_bc = b / c
modulus_ac = a % c
exponentiation_bc = b ** c

# Print the results
print("b + c =", sum_bc)
print("a - b =", difference_ab)
print("a * b =", product_ab)
print("b / c =", quotient_bc)
print("a % c =", modulus_ac)
print("b ** c =", exponentiation_bc)

# Use built-in functions for numerical operations
absolute_a = abs(a)
rounded_b = round(b)
max_value = max(a, b, c)
min_value = min(a, b, c)

print("Absolute value of a:", absolute_a)
print("Rounded value of b:", rounded_b)
print("Max value:", max_value)
print("Min value:", min_value)

# Import the math module for more advanced math operations
import math

square_root_a = math.sqrt(a)
logarithm_base_10_c = math.log10(c)
factorial_c = math.factorial(abs(c))

print("Square root of a:", square_root_a)
print("Logarithm base 10 of c:", logarithm_base_10_c)
print(f"Factorial of |c| ({abs(c)}):", factorial_c)

