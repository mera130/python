print("you can do two digit multipication here ")
while True:
    try:
        num1 = float(input("\nEnter first number:"))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 * num2)
    except ValueError:
        break 