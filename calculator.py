print("Simple Calculator")
print("Choose operation: +  -  *  /")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number (e.g., 5 or 9.8)")

try:
    num1 = get_number("Enter first number: ")
    op = input("Enter operator (+, -, *, /): ").strip()
    num2 = get_number("Enter second number: ")

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero!")
            result = None
    else:
        print("Error: Invalid operator! Please use +, -, *, or /")
        result = None

    if result is not None:
        print(f"Result: {result}")

except KeyboardInterrupt:
    print("\nOperation cancelled by user")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

input("Press Enter to exit...")