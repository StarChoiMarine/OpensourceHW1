def calculate():
    operation = input("Enter the operation (+ or -): ")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if operation == "+":
        print(f"The result is: {num1 + num2}")
    elif operation == "-":
        print(f"The result is: {num1 - num2}")
    else:
        print("Invalid operation. Please enter + or -.")

if __name__ == "__main__":
    calculate()
