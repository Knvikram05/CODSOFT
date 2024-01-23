def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero"

def calculator():
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    
    print("Simple Calculator")

    # Using error handling for user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    operation = input("Choose operation (+, -, *, /): ")

    if operation in operations:
        result = operations[operation](num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid operation. Please choose a valid operation (+, -, *, /).")

# Run the calculator
calculator()
