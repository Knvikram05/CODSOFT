def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y


def divide(x,y):
    return x / y if y != 0 else "cannot divide by zero"

def Calculator():
    operations = {'+':add , '-': subtract , '*':multiply , '/':divide}
    print ("Simple Calculator")

    #using  error handling method 

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    
    except ValueError:
        print("Invalid input .please Enter valid number")   
        return
    
    operation = input("choose operation ( + , _ , * , / ,):")

    if operation in operations:
        result = operations[operation](num1 ,num2)
        print(f"Result:{result}")
    else:
        print("Invalid operation .please choose a valid operation(+ , - , * , /).")    

#Run the calculator
Calculator()
