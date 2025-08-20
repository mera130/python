num = int(input("Enter a number: "))

digits = str(num)
length = len(digits)
total = sum(int(digits[i]) ** (i + 1) for i in range(length))

if total == num:
    print(num, "is a Disarium number ")
else:
    print(num, "is not a Disarium number ")
