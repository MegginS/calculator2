"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    input_string = input("Enter your equations ")
    tokens = input_string.split(" ")
    
    if "q" in tokens:
        break

    operator = tokens[0]
    num1 = float(tokens[1])

    if len(tokens)>2:
        num2 = float(tokens[2])

    if operator == "+":
        result = add(num1, num2)

    elif operator == "-":
        result = subtract(num1, num2)

    elif operator == "*":
        result = multiply(num1, num2)

    elif operator == "/":
        result = divide(num1, num2)

    elif operator == "pow":
        result = power(num1, num2)

    elif operator == "mod":
        result = mod(num1, num2)

    elif operator == "square":
        result = num1 * num1

    elif operator == "cube":
        result = num1 * num1 * num1

    print(result)

