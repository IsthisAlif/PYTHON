# Python calculator

operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    result = round(result, 2)
    print(result)
elif operator == "-":
    result = num1 - num2
    result = round(result, 2)
    print(result)               
elif operator == "*":
    result = num1 * num2
    result = round(result, 2)
    print(result)
elif operator == "/":
    result = num1 / num2
    result = round(result, 2)
    print(result)
else:
    print("Invalid operator!")