number = int(input("Enter a non-negative integer: "))

factorial = 1

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for current_number in range(1, number + 1):
        factorial = factorial * current_number

    print(f"The factorial of {number} is {factorial}.")