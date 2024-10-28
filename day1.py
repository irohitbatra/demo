print("Day1: Welcome! Choose an arithmetic operation to perform ")
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")

choice = input("Enter your choice (1/2/3/4): ")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if choice == "1":
    print("Addition:", a + b)
elif choice == "2":
    print("Subtraction:", a - b)
elif choice == "3":
    print("Division:", a / b)
elif choice == "4":
    print("Multiplication:", a * b)
else:
    print("Invalid choice. Please choose 1, 2, 3, or 4.")