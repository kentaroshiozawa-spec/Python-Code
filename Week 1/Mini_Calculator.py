while True:
    op = input("Enter operator (+, -, *, /, exit):  ")
    if op == "exit":
        break
    a = int(input("Enter first number:  "))
    b = int(input("Enter second number:  "))
    
    if op == "+":
        print(f"This is the sum of {a} and {b} = {a + b}")
    elif op == "-":
        print(f"This is the difference of {a} and {b} = {a - b}")
    elif op == "*":
        print(f"This is the product of {a} and {b} = {a * b}")
    elif op == "/":
        if b != 0:
            print(f"This is the quotient of {a} and {b} = {a / b}")
        else:
            print("Error: Division by zero is not allowed.")
    elif op == "exit":
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Error: Invalid operator. Please use +, -, *, /, or exit.")
    