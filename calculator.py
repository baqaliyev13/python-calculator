operator = input("enter an operator (+ - * /)")

def add(a, b):
    return a + b 

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def subtract(a, b):
    return a - b


num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))


if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    print(f"{operator} is not a valid operator")


print(f"Result is {result}:")