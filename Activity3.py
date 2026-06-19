import math

# Method 1: Using built-in library
user_input = int(input("Enter a number: "))
print(f"The factorial is: {math.factorial(user_input)}")

# Method 2: Custom Loop
def get_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


