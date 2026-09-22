s1 = input("Enter a string containing digits: ")

digits = []

for character in s1:
    if character.isdigit():
        digits.append(int(character))

if digits:
    digit_sum = sum(digits)
    digit_average = digit_sum / len(digits)

    print("Digits:", digits)
    print("Sum:", digit_sum)
    print("Average:", digit_average)
else:
    print("The string contains no digits.")