#task1
import math

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is", factorial)
#task2
# Improved version using math module

num = int(input("Enter a number: "))
print("Factorial of", num, "is", math.factorial(num))
#task3
# Function to calculate factorial using a loop
def compute_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Take input from the user
num = int(input("Enter a number: "))

# Call the function and print the result
print("Factorial of", num, "is", compute_factorial(num))

#task5
def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print("Factorial of", num, "is", iterative_factorial(num))