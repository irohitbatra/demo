# 1. Print "Hello Python"
print("Hello Python")

# 2. Perform arithmetical operations: addition and division with user input
num1 = int(input("Enter the first number for addition and division: "))
num2 = int(input("Enter the second number for addition and division: "))
addition = num1 + num2
division = num1 / num2
print("Addition:", addition)
print("Division:", division)

# 3. Find the area of a triangle with user input
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("Area of the triangle:", area)

# 4. Swap two variables with user input
x = input("Enter the first variable to swap: ")
y = input("Enter the second variable to swap: ")
x, y = y, x
print("After swapping, x =", x, "and y =", y)

# 5. Generate a random number
import random
random_number = random.randint(1, 100)
print("Random number:", random_number)
