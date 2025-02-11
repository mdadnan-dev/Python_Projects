operator = input('''Enter an operator
 "Addition (+)"
 "Subtraction (-)"
 "Multiplication (*)"
 "Division (/)"
 "Remainder (%)"
 "Power Of (**)" :  ''')

num1 = float(input("Enter a number : "))
num2 = float(input("Enter a number : "))

if operator == '+':
    result = num1 + num2
    print(result)

elif operator == '-':
    result = num1 - num2
    print(result)

elif operator == '*':
    result = num1 * num2
    print(result)

elif operator == '/':
    result = num1 / num2
    print(result)

elif operator == '%':
    result = num1 % num2
    print(result)

elif operator == '**':
    result = num1 ** num2
    print(result)

else:
    print(f"Invalid operator {operator},\nPlease use a valid operator from the options")