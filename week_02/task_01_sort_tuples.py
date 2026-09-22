numbers = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sorted_numbers = sorted(numbers, key=lambda item: item[-1])

print("Original list:", numbers)
print("Sorted list:", sorted_numbers)