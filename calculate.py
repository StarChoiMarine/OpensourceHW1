def calculate():
    operation = input("Enter the operation (+, -, *, /): ")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if operation == "+":
        print(f"The result is: {num1 + num2}")
    elif operation == "-":
        print(f"The result is: {num1 - num2}")
    elif operation == "*":
        print(f"The result is: {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            print(f"The result is: {num1 / num2}")
        else:
            print("Cannot divide by zero. and this is branch 1")

if __name__ == "__main__":
    calculate()
